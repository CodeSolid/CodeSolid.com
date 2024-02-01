---
title: "CodeSolid Newsletter 12/13/2022"
date: "2022-12-13"
categories: 
  - "newsletter"
coverImage: "Newsletter.jpg"
---

Hello, CodeSolid Subscriber,

I hope you’re doing well.

It’s time for another review of what’s new on CodeSolid and around selected parts of the rest of the Python Interwebs.

## New On CodeSolid

On CodeSolid, our new author, Bashir Alam, has worked very hard on our Pandas Series, with two recent articles on Pandas:

[How to Visualize Data Using Pandas](https://codesolid.com/how-to-visualize-data-using-pandas/)  
If you’ve ever wondered why you need to add Matplotlib or Seaborn explicitly to do simple data visualization, the answer is that you don’t!  This excellent article surveys the built-in plotting features of Pandas.  

[Data Cleaning in Pandas](https://codesolid.com/data-cleaning-in-pandas/)  
Bashir Alam’s second CodeSolid article on data cleaning covers several different techniques.  Naturally, it covers filling in or deleting missing data.  Also, it covers many other data manipulation techniques, such as fixing strings using the apply method, renaming single columns, and many others.

[Data Analysis Starter Project](https://codesolid.com/python-data-analysis-starter-project/)  
My writing output has been down a bit recently, but with the Pandas Series in full swing, I wanted to publish instructions for installing the basic requirements, so we wouldn’t have to write them over and over again for every article.  This article covers how to do it using either Pip or Conda.

## Around The Web

[Pygris - Geographic Datasets](https://walker-data.com/pygris/)  
Pygris is a new package just announced by a friend on LinkedIn for loading US Census Bureau Tiger/Line cartographic shape files into GoeDataFrames.  This makes it easier to work with Census Geographic data.

[Ignore all Web Performance Benchmarks, Including This One](https://blog.miguelgrinberg.com/post/ignore-all-web-performance-benchmarks-including-this-one)  
Full disclosure, this article dates back to 2020, but I found it recently cited on Reddit.  Miguel Grinberg is well known as the pre-emininent author who works with Flask, so I was inclined to read through it despite the warning to ignore it. I was interested to see that Falcon did very well, getting top marks overall and when run with both on every web server it was run on against other frameworks.  Falcon seems to be getting a lot of good press lately, and I like how Falcon APIs are structured as simple objects with obvious HTTP verb handlers, e.g. “on\_get”.

[What’s the Hardest Challenge When Writing Unit Tests](https://www.reddit.com/r/Python/comments/zckje7/what_is_the_hardest_challenge_when_writing_unit/) (Discussion)  
I enjoyed this Reddit discussion about some of the challenges of testing. By way of chiming in with my answer just for my readers, the challenges I’ve faced on different projects are:  

- Not having unit tests at all / no management support for adding them.  I’ve found the best way to overcome this is to suggest starting small and then show the results – finding bugs that otherwise would have been uncovered in production.

- Tests that differ from the production stack.  I know, I know:  Unit tests are supposed to use mocks, right?  However, I’ve often encountered issues where we end up debugging why the behavior of the mocks / in memory-database / what-have-you don’t match what we’re seeing in production or spending time on mocking when a fast and performant way to run against a live system is available to us.  I often find myself mixing unit tests and a set of easily-disabled “integration tests” that require more developer intervention.

  
For all of these challenges, I’d still rather work on a system with tests than without them.

[FastAPI Template](https://bitestreams.com/blog/fastapi_template/)  
Although I often find myself building things from scratch, I like the idea of this kind of “everything-and-the-kitchen-sink” project, putting together a variety CI/CD, containers, database migrations, etc.  The author deserves some credit for putting in the time to put this together.

Just for Fun:  [Hybrid Programming](http://stupidpythonideas.blogspot.com/2018/04/hybrid-programming.html)  
If you’ve been around the industry for a while, you may have noticed a huge discrepancy between the “best practices that everyone follows”, and the code you actually inherited on your job!  This is a satirical update of the article “Abject Oriented Programming”, which is also worth a read (linked in the article).  Enjoy!
