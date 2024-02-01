---
title: "Building a Docker Golang Container"
date: "2021-11-25"
categories: 
  - "docker"
---
This is nice.

$$
\frac{(5-2) x 180}{5} = 108^o
$$

One of the main benefits of blogging about software is that it allows me to dust off and improve skills that I otherwise might not get too much opportunity to practice during my day job as a Java peasant. (If you don't know, Java Peasants work in object factories).

Along these lines, I've set myself a goal of creating a non-trivial build pipeline for Kubernetes, consisting of a Go API server, a front-end server running Nginx, and perhaps an auth server (FusionAuth). The database layer is TBD but may not run in Kubernetes (except perhaps in development).

## From Simple to Complex

There's an old axiom called Gall's Law that I'm quite fond of:

_A complex system that works is invariably found to have evolved from a simple system that worked._

I like Gall's Law so much because it reflects how I work. In this case, knowing that I ultimately wanted a bunch of containers running as Kubernetes pods, I started in the simplest way I could, with a basic container build. We'll need a simple Go app with which to test the build:

A go.mod is always a good starting point:

go.mod:

```go
module gorilla/example
```

We can point this to a repository later if we need to – for now, it's enough to prime the Go 1.11+ module system.

We'll be needing a go application to serve. Here's a tasty little morsel of a Go application. Yes, the port is hard-coded (oh the horror), but this is Hello World, not rocket surgery:

```go
// main.go

package main

import (
	"net/http"
	"github.com/gorilla/mux"
)

func main() {

	r := mux.NewRouter()

	r.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Write([]byte("Hello world."))
	})

	http.ListenAndServe(":9000", r)
}
```

The gorilla library lets us have sophisticated routes later on, but for now, it just tests that we can resolve modules as we're building. It also lets us use "gorilla" in our container names – and heck, given a chance, why wouldn't we want to do that! If it's not apparent from the code, this will stand up a web server, serving up a time-honored message on port 9000.

OK, so now we have an app. You can build it or run it locally if you want, but that's no fun. We want to put it in a docker container and get it running from there.

## A Naive Approach

We want a Dockerfile to build a container from our app. Keeping in mind Gall's Law, we want to start with something simple that works, even if it's not production-ready at this point. (Don't worry, we'll improve it later in the article).

```docker
# Dockerfile

FROM golang
WORKDIR /app
ADD go.* /app/
ADD *.go /app/
RUN go build -o main . 
ENTRYPOINT ["/app/main"]
```

The FROM line grabs the latest GOLANG container from Dockerhub. In the next few lines, we copy our go source and mod.go into our working directory, /app, on the container. Finally, we RUN go build to build our source into an executable named "main," then with "ENTRYPOINT," we set the executable to be what the container runs when it starts.

Let's build it and see if it works. From the directory containing the Dockerfile, run:

```bash
docker build -t golang-gorilla:latest .
```

If all goes well, this will build an image, tagging it with the name "golang-gorilla:latest".

Next, let's use this image to start a container, so our gorilla can serve up web requests.

The following command runs the golang-gorilla image in detached mode ("-d"), naming the container "gorilla." As an example, we'll map the container port (9000) to a different host port (8080):

```bash
docker run --name gorilla -p8080:9000 -d golang-gorilla
```

Once this is running, you can point a browser http://localhost:8080, or run this:

```bash
curl localhost:8080
```

This should output:

```bash
Hello world.
```

To see it running in the container:

```bash
docker exec -it gorilla curl http://localhost:9000
```

## What’s Wrong with the Naive Approach, and How To Fix It

So if our gorilla is off in the forest happily greeting visitors with "Hello world," what's the problem? Well, honestly, there is no problem for a toy app like this, but for a real production app, we want to solve two issues. First, we're basing our image on "golang" to build and run our image. That makes the resulting image file much larger and more complex than it needs to be. Once we start storing it in Dockerhub or a similar repository, the download will take longer than it has to.

Let's see how bad the problem is. Docker images will tell us some basic facts about an image, including the size:

```bash
docker images golang-gorilla
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
golang-gorilla      latest              67edf2eee9fa        8 hours ago         782MB
```

Wow! Almost a gigabyte. Talking gorilla notwithstanding, all we really have so far is Hello world. We can do better.

The second problem is that to build our image, we first copied our source code to it! We can prove to ourselves that it's still there:

```
docker exec -it gorilla ls /app
go.mod	go.sum	main  main.go
```

This means that if anyone gets access to our server, in addition to the other havoc they can wreak, they're going to have access to all our code. At this point, we don't care, of course, because the code's in the article anyway, but for a production application, that's not what we want.

Fortunately, recent versions of docker have an elegant and straightforward solution to this problem.

## Multi-stage Builds

We want to be able to build our application with a first step, then copy only the files we need to the image. Since version 17.05, docker has shipped with a feature called multi-stage builds. This is a feature that allows us to create a build using an initial image, then package the results into a much smaller – and much more secure – final image.

It works by allowing multiple "FROM" clauses, which can be based on entirely different images. Earlier images can be as large as we want for our build tools, but we can copy the results to a more compact image as a final step. We can give the steps names in the FROM clause to make this process even more accessible.

To see how this works, let's take our original code and modify our Dockerfile.

```docker
# File: Dockerfile
# Supports multi-stage build

FROM golang as builder
WORKDIR /app
COPY * /app/
RUN env GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o server .

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /app/server .
ENTRYPOINT ["/root/server"] 
```

I've also set up the build command with some environment variables I found I needed for Alpine. This time, we're calling our executable "server." Two remaining differences in the first part from before are that we've named the result "builder", and we have no ENTRYPOINT (yet).

In the second part, we're basing our image on Alpine, a Linux distribution that's popular in the Docker community for its small size and consequent "low attack surface." We set the WORKDIR and simply copy the server executable we built in the first step to it. Naming the first step allows us to refer to it by name ("–from=builder"). Finally, the second step runs the resulting server.

Let's build it as before, but we'll call it mini-gorilla since we expect it to be smaller.

```
docker build -t mini-gorilla:latest .
```

Did we save any space?

```
docker images mini-gorilla
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mini-gorilla        latest              5ae087964c8d        53 seconds ago      13.2MB
```

Wow, from 782 Mb down to 13.2 Mb. That's pretty good! Our original image was about 59 times as big as our second attempt.

Let's run our new mini-gorilla container, giving it a new name and port:

```
docker run --name gorilla2 -p9000:9000 -d mini-gorilla
```

Is our app still working? Let's check our server:

```
curl localhost:9000
Hello world.
```

All good. But what about our source code? Is that anywhere to be found in our container?

```
docker exec -it gorilla2 find / -name *.go
```

No output – that's good, nothing to see here, folks!

So there we are – we've done the simplest docker go build that will work at all, and we've improved on it somewhat with a multi-stage build, all using simple docker commands.

I've stood up a [Github repo](https://github.com/JohnLockwood/golang-docker) with the source code for you if you want to check it out (so to speak).

Some commands you can use in your environment to clean up are:

```
# Stop containers
docker stop gorilla
docker stop gorilla2

# Remove containers
docker rm gorilla 
docker rm gorilla2 

# Remove images
docker  image rm golang-gorilla:latest
docker image rm mini-gorilla:latest
```
