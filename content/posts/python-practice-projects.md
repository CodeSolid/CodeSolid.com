---
title: "What Are Good Projects To Practice In Python?"
date: "2022-02-06"
categories: 
  - "python-practice"
coverImage: "woman-programmer-smaller.jpeg"
---

The best Python practice projects depend on your interests and career choice, your goals for practice, and your skill level. But since we all can use some help brainstorming ideas and resources, this series of articles on Python Practice Projects can help you get started on the next big thing.


## Introduction: Why Is This a Series?

A friend of mine and fan of the site reached out to me recently and asked me if I had ideas for Python Projects he could do to improve his skills, now that he'd been through an introductory Python text. I also see that question asked a lot on the [r/Python](https://www.reddit.com/r/Python/) discussion on Reddit. I see some version of the question scroll by at least once per week.

It's a great question, as doing real work in a language is one way to really learn it well. The trouble is, though almost everyone is familiar with the cliché, "practice makes perfect", learning the truism doesn't teach us _what_ to practice, or even give us much guidance on where to look. This problem is even more acute once you get past the beginner stage. In my article on [How to Practice Python](https://codesolid.com/how-to-practice-python/#setting-up-your-environment-for-success), I counsel beginners to have a resource to learn from to guide their practice, and I'm able to provide a link to two good resources to use. But what if you don't want to buy the book, or what if you've picked up a good introductory course or book on Python and practiced what you can through that, then what?

## The Plan

Since the point of the series will be to brainstorm ideas for Python projects and exercises to help you in your practice, I don't expect each issue to necessarily follow the same format, but here are some ways a typical article might be structured.

- **Exercises for beginners**. This section will definitely overlap the kinds of exercises you can expect to find in a Python book.
- **Online resources**. This will include links and discussion of what online resources you can use to help you learn or Practice Python. Where others have told us they've found something helpful to them, we'll pass those ideas along.
- **Ideas for projects**. These may be original ideas for Python projects at different levels or links to projects that others have done. We absolutely want to give some love back to the community in these posts, so if you have a project you think is interesting, let us know in the comments, and we'll try to include it.
- **Python knowledge questions**. Honestly, I really don't like articles that are just exhaustive lists of interview questions -- especially because they presuppose some blogger knows the intimate details of how everyone runs an interview using some blogging crystal ball. That said, having a few "brain-teaser" Python questions thrown into the mix will also be entertaining.
- **"Guest" posts**. This blog is at the point where I'll soon want to begin hiring authors to help me bring you more great Python content, and I think when it comes to brainstorming ideas for Python projects, it's important to have more than one brain at work on the problem, so this will likely be where I'll ask for the first posts. This could mean writing the series issue that week, or providing solutions to selected exercises, or both.

## Issue #1

### A Beginner Exercise

**String Formatting**. One of the most important aspects of any programming language is the ability to format strings. On a very basic level, this involves being able to concatenate strings and use string formatting tools, perhaps the most popular of which in modern Python programming is the [Formatted--string literal](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals), or "f-string".

Using f-strings is fairly easy, but this exercise is to practice attractively formatting tabular data for the screen, which may involve spacing the data for the longest row, different forms of justification, decimal alignment (it may help to use "round" on numeric columns), etc.

For this exercise, imagine or create a few rows of tabular data. For example, If you need ideas, take a look at this list of [CSV files](https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html) -- you can load one of these using Python's [CSV module](https://docs.python.org/3/library/csv.html). Once you have some CSV loaded in memory, how can you format it, so it looks good on the display? (By display here we simply mean STDOUT, but a variation on this exercise is to generate a formatted HTML table).  
  
What about the next CSV file? For a more advanced program, consider how you might apply an array of format strings or some other mechanism to format and output any CSV nicely. How might you organize a module to do this using functions or classes?

### An Intermediate / Advanced Exercise

Here's an intermediate to advanced exercise that I admit I haven't gone through myself -- yet. Unlike languages like C, C++, and Golang, Python doesn't natively support compiling files to executables and shipping pre-built binaries to customers. On a recent Python Reddit thread, this was one of the most popular answer to the question, [What are the top features you wish Python had](https://www.reddit.com/r/Python/comments/scbotw/what_are_the_top_features_you_wish_python_had/)?

The mission for the exercise is to try to build some Python executables of various degrees of complexity, on one or more top platforms you can readily access. The Reddit thread lists a variety of tools you can try to do this with -- though some are platform specific.

Some things you might try to build are:

- A simple command line application or tool, perhaps one you find personally helpful or useful.
- A "windowing" app using QT for Python.
- A web server application based on Flask that runs in a single executable.
- A Jupyter Notebook "clone" that runs as an executable.

### Seen Around The Web

For more project ideas, here are a couple of links to get you started.

If you are brand new to Python or need to brush up quickly on some syntax, one of my favorite sites for every language I'm learning is [w3schools.com](https://www.w3schools.com/python/default.asp). They always have great tutorials that give you an overview of the language.

You might find several intermediate/advanced project ideas in this thread about [what tasks Python devs have recently automated at work](https://www.reddit.com/r/Python/comments/slqxbt/what_have_you_recently_automated_at_work_using/).

## What Are You Working On?

Are you working on a cool project, task, or learning goal? We'd love to hear about what you're doing and, we may feature you in a later article too! Drop us a line in the comments!

## You May Also Enjoy

- [Random Python: Secrets and Random Values Made Easy](https://codesolid.com/random-python-secrets-and-random-values-made-easy/)
- [Python Format Strings: Beginner to Expert](https://codesolid.com/python-format-strings/)
