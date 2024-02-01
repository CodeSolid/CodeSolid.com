---
title: "Fast S3 Updates with Golang and Goroutines"
date: "2019-02-23"
categories: 
  - "miscellaneous"
---
# Fast S3 Updates with Golang and Goroutines
I recently wrote a go program to optimize my S3 uploads for this blog. The idea was to write a program that would only upload the files that have changed (rather like RSync) rather than bulk uploading the whole site each time. Although there are third-party tools to do this, I wanted to learn more about the golang AWS API while at the same time getting a chance to run some goroutine benchmarks. To see the code and the benchmarks I did, read on!

## Is This Trip Necessary?

After writing this article, I discovered that a simpler approach to this is to use the AWS CLI. The AWS CLI has a "sync" command which allows you to sync files and directories. I'm leaving this article here, however, as it still shows some interesting techniques in Go.

## Some Preliminaries

The AWS API for golang exposes an S3 service that we'll use both for querying the files already in the Amazon cloud and uploading the new or changed files. Let's see that and quickly look at all the imports we'll be using:

```go
// main.go

import (
    "bytes"
    "crypto/md5"
    "fmt"
    "io/ioutil"
    "log"
    "net/http"
    "os"
    "path/filepath"
    "strings"

    "github.com/aws/aws-sdk-go/aws"
    "github.com/aws/aws-sdk-go/aws/credentials"
    "github.com/aws/aws-sdk-go/aws/session"
    "github.com/aws/aws-sdk-go/service/s3"
)

/* getS3Session returns the AWS session with our configuration.
   For our purposes this could have gone in getS3Service,
   but in case we end up relying on other AWS clients
   it's handy to have the session available separately.
*/ 
func getS3Session() *session.Session {
    // Use shared credentials ($HOME/.aws/credentials),
    // but set the region
    return session.Must(session.NewSession(
        &aws.Config{
            Region:      aws.String(getConfiguration().region),
            Credentials: credentials.NewSharedCredentials("", "default"),
        }))
}

/*
    getS3Service returns a service we use to query our bucket 
    and to put new / changed files.
*/
func getS3Service() *s3.S3 {
    return s3.New(getS3Session())
}
```

The function getS3Session relies on a configuration function to set up our program. This is simply a struct to keep whatever settings we need, which you'd need to change up to match your local path and S3 bucket name. Since this was a personal project, we chose a configuration object over a set of command-line parameters. Here's the code for our configuration type/function.

```go
type config struct {
    region         string /* AWS region to use for session */
    bucket         string /* S3 bucket where are files are stored */
    localDirectory string /* Local files to sync with S3 bucket */
}

func getConfiguration() *config {
    configuration := config{
        region:         "us-east-2",
        bucket:         "codesolid.com",
        localDirectory: "/home/john/source/codesolid/public/"}
    return &configuration
}
```

## Program Design

Our strategy will be simple. If we can build a map of remote S3 object (file) names to file checksums, any local files that either aren't in the map or who are in the map but have a different checksum need to be uploaded. We're concerned with new or updated files -- any deletes are ignored, and we can handle them separately.

So our first function builds the map of remote files to checksums.

```go
/**
getAwsS3ItemMap constructs and returns a map of keys (relative filenames)
to checksums for the given bucket-configured s3 service.  
It is assumed  that the objects have not been multipart-uploaded, 
which will change the checksum.
*/
func getAwsS3ItemMap(s3Service *s3.S3) (map[string]string, error) {

    var loi s3.ListObjectsInput
    loi.SetBucket(getConfiguration().bucket)

    obj, err := s3Service.ListObjects(&loi)

    // Uncomment this to see what AWS returns for ListObjects
    // fmt.Printf("%s\n", obj)

    var items = make(map[string]string)

    // Based on response from aws API, map relative filenames to checksums
    // The "Key" in S3 is the filename, while the ETag contains the 
    // checksum
    if err == nil {
        for _, s3obj := range obj.Contents {
            eTag := strings.Trim(*(s3obj.ETag), "\"")
            items[*(s3obj.Key)] = eTag
        }
        return items, nil
    }

    return nil, err
}
```

Next, we need to walk our local directory that contains the corresponding files we'll want to check for updates. Since we'll be walking the directory tree and opening each file, in turn, to run a checksum on it, there's a lot of file input going on that makes the task a good fit for optimizing with GoRoutines.

I confess that I did it wrong in an early draft of this approach. By using shared memory which needed to be synchronized to add the files to a list, I made the program slower than without the goroutines (as my benchmarks showed)! Once I used channels and moved the building of the list to the main goroutine, the benchmarks improved significantly for the goroutine version compared to the same code without goroutines and channels.

I paid the price for ignoring the [Go Blog's](https://blog.golang.org/share-memory-by-communicating) advice:

**\*\***_\*"Do not communicate by sharing memory; instead, share memory by communicating."\*_**\*\***

Before we get to the benchmarks, let's look at the final version of the code. Let's start our discussion with the traditional, synchronous version without go-routines or channels.

```go
/*
fileWalkWithoutGoroutine walks the local directory using golang's
filepath.Walk.  Ignoring directories, for each file we get 
the checksum of the relative file path from the awsItems map.
We then pass the full filename and checksum to testFileNoGoroutine,
which returns either an empty string if the file doesn't need to be 
uploaded, or a non-empty string if there's no checksum (file not on the remote) 
or if the checksum doesn't match the local file (file has changed).

Return the list of files to be uploaded as a list.
*/
func fileWalkWithoutGoroutine(awsItems map[string]string) []string {
    var files int
    var filesToUpload []string
    blogDir := getConfiguration().localDirectory
    filepath.Walk(blogDir, func(path string, info os.FileInfo, err error)   error {
        if err != nil {
            return err
        }
        if !info.IsDir() {
            files++
            relativeFile := strings.Replace(path, blogDir, "", 1)
            checksumRemote, _ := awsItems[relativeFile]

            filename := testFileNoGoroutine(path, checksumRemote)
            if len(filename) > 0 {
                filesToUpload = append(filesToUpload, filename)
            }
        }
        return nil
    })

    return filesToUpload
}

/**
    testFileNoGoroutine returns a blank string if the given 
    filename does not need to be updated (checksum blank or does 
    not match local file), or a non-blank filename if the 
    
*/
func testFileNoGoroutine(filename string, checksumRemote string) string {
    if checksumRemote == "" {
        return filename
    }

    contents, err := ioutil.ReadFile(filename)
    if err != nil {
        return ""
    }
    sum := md5.Sum(contents)
    sumString := fmt.Sprintf("%x", sum)
    // checksums don't match, mark for upload
    if sumString != checksumRemote {
        return filename
    }
    return ""
}
```

Now, let's look at the same code using goroutines and channels. This time, as we walk the local directory, we call `testFile` repeatedly as a goroutine. In `testFile`, instead of returning a string as in our earlier program, we pass the filename or a blank string back on the channel that we passed from `fileWalk`.

In fileWalk, we keep a count of the files we walked in `numfiles`, and when we're done walking the files, we read from the channel we passed to `testFiles` `numfiles` times to build our list of files to return.

```go
func fileWalk(awsItems map[string]string) []string {
    blogDir := getConfiguration().localDirectory
    ch := make(chan string)
    var numfiles int
    filepath.Walk(blogDir, func(path string, info os.FileInfo, err error) error {
        if err != nil {
            return err
        }
        if !info.IsDir() {
            numfiles++
            relativeFile := strings.Replace(path, blogDir, "", 1)
            checksumRemote, _ := awsItems[relativeFile]

            go testFile(path, checksumRemote, ch)
            //fmt.Println(path, info.Size())
        }
        return nil
    })

    var filesToUpload []string

    var f string
    for i := 0; i < numfiles; i++ {
        f = <-ch
        if len(f) > 0 {
            filesToUpload = append(filesToUpload, f)
        }
    }

    return filesToUpload
}

func testFile(filename string, checksumRemote string, ch chan<- string) {

    if checksumRemote == "" {
        ch <- filename
        return
    }

    contents, err := ioutil.ReadFile(filename)
    if err == nil {
        sum := md5.Sum(contents)
        sumString := fmt.Sprintf("%x", sum)
        // checksums don't match, mark for upload
        if sumString != checksumRemote {
            ch <- filename
            return
        } else {
            // Files matched
            ch <- ""
            return
        }
    }
}
```

## Benchmarking the Two Versions

We'll leave aside the main method and the code to upload the files for the time being, but at this point we have code that tells us just what files need to be uploaded.

To see how much of a performance boost we get from the goroutine version, we write some simple benchmarks in main\_test.go. Here's our main\_test.go file, with some non-benchmark tests we wrote excluded.

```go
// main_test.go
package main

import (
	"log"
	"os"
	"testing"
)

var awsItems map[string]string

/* Set up the awsItems map that we'll need */
func TestMain(m *testing.M) {

	s3Service := getS3Service()
	var err error
	awsItems, err = getAwsS3ItemMap(s3Service)
	if err != nil {
		log.Fatal(err)
	}

	// call flag.Parse() here if TestMain uses flags
	os.Exit(m.Run())
}

func BenchmarkFilewalkGoroutine(b *testing.B) {
	for n := 0; n < b.N; n++ {
		fileWalk(awsItems)
	}
}

func BenchmarkFilewalkWithoutGoroutine(b *testing.B) {
	for n := 0; n < b.N; n++ {
		fileWalkWithoutGoroutine(awsItems)
	}
}
```

I stumbled on the [prettybench](https://github.com/cespare/prettybench) utility one time, which I like to use to improve the output of Go benchmark tests. Using that tool to format the output gives:

```bash
$ go test -v -bench=. | prettybench
goos: linux
goarch: amd64
pkg: aws
PASS
benchmark                             iter     time/iter
--------- ---- ---------
# Fast S3 Updates with Golang and GoroutinesBenchmarkFilewalkGoroutine-4            50   27.26 ms/op
BenchmarkFilewalkWithoutGoroutine-4     50   32.82 ms/op
ok  	aws	3.543s
```

Of course, we're running an SSD drive here, and Go is hecka fast to begin with, but even with that, the goroutine version improves the performance by about 20%. I'll publish an update to this article or a link to the GitHub version with the upload code and the rest of the program soon, but for now, it's late, so I think I'll use my AWS go file upload utility one last time to push this article to the cloud! Cheers.

## You May Also Enjoy

[Python Format Strings: Beginner to Expert](https://codesolid.com/python-format-strings/)

[Simple Vagrant Ansible Local Example](https://codesolid.com/vagrant-ansible-local/)
