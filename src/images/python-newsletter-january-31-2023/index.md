---
title: "Python Newsletter, January 31, 2023"
date: "2023-01-31"
categories: 
  - "newsletter"
---

Hi From CodeSolid!

Wow, I’ve noticed a lot of new folks have been signing up for this newsletter lately, so let me take this opportunity to welcome the newcomers and repeat my thanks to ALL of you who’ve signed up for my weekly CodeSolid + Stuff Around The Internet Newsletter.

## New and Featured On CodeSolid

[Alternatives to Pandas:  Polars](https://codesolid.com/alternatives-to-pandas-python-polars/)  
Polars is a fast, modern library that’s similar to Pandas. Polars features a two-dimensional DataFrame object made up of one-dimensional columns, or “Series” objects.  As we wrote in [Large Datasets in Python:  Pandas and the Alternatives](https://codesolid.com/large-data-sets-in-python-pandas-and-the-alternatives/), the Polars library outperforms Pandas, especially on larger data sets.  This follow-up article compares the Pandas and Polars API in more depth.  Coming from Pandas, we found Polars quite intuitive and worth checking out!

[Selecting Data in Pandas](https://codesolid.com/selecting-data-in-pandas)  
Bashir Alam has once again provided an outstanding guest post, this time covering the many methods and operators for selecting data.  Some of these used to strike me as a bit obtuse and hard to remember, but that was before I had the privilege of editing this article.  If you’re like me and thought you might be doing it wrong, check out this article. 

## Books

I recently picked up the Kindle edition of [CPython Internals:  Your Guide to the Python 3 Interpreter](https://www.amazon.com/CPython-Internals-Guide-Python-Interpreter-ebook/dp/B0BCNSDSYP/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=), which is a great book if you’ve ever wondered how the Python language works at a low level.  This book begins with instructions on building the C code (which you can also find online) but goes beyond that by taking you through the parser and compiler and making changes to the code yourself.  It’s not for the faint of heart, but I find it quite fun!  I may post a more in-depth review at some point.

## Around the Web

[PEP 704 - Require Virtual Environments for Package Installers](https://www.reddit.com/r/Python/comments/10l5mmk/pep_704_require_virtual_environments_by_default/)  
Python has many great features and one unruly, awful, drunken elephant in the room:  dependency management.  I like this PEP’s approach of installing into a Virtual environment by default, but as other users have pointed out, one way or the other, we need to finally get this right.

[Resource Abstractions to be Deprecated in AWS Boto3  
](https://www.reddit.com/r/Python/comments/10gl90s/resource_abstractions_to_be_deprecated_in_aws_sdk/)If you’ve worked in boto3 (Amazon’s Python client for AWS services), you may know that there are generally two interfaces, an easy-to-use, object-oriented one (the resource abstraction), and one that is closer to the Restful API calls that is more difficult to understand and debug.  This post is bad news if you’re using boto3 heavily.  If you are, now’s the time to weigh in.

[JupySQL:  Better SQL In Jupyter](https://ploomber.io/blog/jupysql/)  
In response to my article on Using DuckDB with Pandas and IPython-SQL, a JupySQL developer asked me to mention JupySQL.  I haven’t had time to work up an article on this yet, but I think it adds some cool features.

[Reddit Discussion on Python Optimizers](https://www.reddit.com/r/Python/comments/10gbt8w/some_reasons_to_avoid_cython/)  
In this thread, the original poster shared a link to an article about reasons to avoid Cython.  One of the things I like about Reddit is seeing the back and forth and the many alternate suggestions that arise when such an issue gets raised.  Although the controversy can sometimes be daunting (I know, as I’ve had my tail feathers ruffled once or twice), the back and forth can often teach you a lot more than the original post can.  This thread is an excellent example of that.
