---
title: "CodeSolid Newsletter, 11/29/2022"
date: "2022-11-28"
categories: 
  - "newsletter"
---

Dear CodeSolid Subscriber,

Hello again.  US readers, I hope you had an awesome Thanksgiving.  Oh, let’s not be exclusive about this:  I hope you had an awesome Thanksgiving no matter where you are.  Thanksgiving was Thursday.

As many of you know, I’ve been wrestling a bit with the frequency of this newsletter.  Once per week is hard to maintain while writing new content, but “hardly ever” isn’t a very good publication schedule either.  I think every two weeks fits the bill, so we’ll try that on for a little while.

## New On CodeSolid

Recent weeks find me writing a lot about Pandas tools and a bit about alternatives such as Polars.

[Large Data Sets in Python:  Pandas and the Alternatives  
](https://codesolid.com/large-data-sets-in-python-pandas-and-the-alternatives/)As many of you are probably aware, Pandas is not strictly speaking a big data tool, so for truly massive data sets, something like Spark or Hadoop, or a data warehousing solution like BigQuery, Redshift or the like is generally more appropriate.  However, Pandas still works for data sets up to a few gigabytes in size – and this article looks at how to optimize Pandas at this scale as well as another really exciting tool, Polars.

[Using SQL With Pandas:  PandasSQL, and IPython-SQL with DuckDB](https://codesolid.com/sql-with-pandas/)  
As you may know, Pandas can natively read and write SQL tables as though they were just another data source.  Beyond that, there are third-party libraries that let you use SQL to query Pandas DataFrames.  One product that supports this brilliantly is DuckDB, which a friend of mine mentioned to me as a general-purpose OLAP tool.  The Pandas support was one unexpected bonus of DuckDB.  The other fringe benefit was the picture I could use to accompany the article.  Let’s face it – few things are cuter than a baby duck!

## New Around the Web

[How we run our Python tests in hundreds of environments really fast](https://blog.sentry.io/2022/11/14/how-we-run-our-python-tests-in-hundreds-of-environments-really-fast/)  
This article shows how one team sped up their Python test suite, which needed to run hundreds of tests against different frameworks and different Python versions.

[Python Asyncio:  The Complete Guide](https://superfastpython.com/python-asyncio/)  
Jason Brownlee of Superfast Python has published a complete guide to programming using the asyncio module.

[Pandas DataFrame Visualization Tools  
](https://pbpython.com/dataframe-gui-overview.html)Chris Moffitt of Practical Business Python has written this interesting review of several different tools for viewing Pandas Datasets.

(Just for fun)  [Vent:  I’m tired of the 1001 Libraries of Virtual Environments](https://www.reddit.com/r/Python/comments/z1v0f1/vent_im_tired_of_the_1001_libraries_of_virtual/)  
If you really want to get a Python discussion board chiming in, just talk about whether all you need is venv and Pip or Conda (or hey what about Poetry?).  
  
I have to admit that I’m also a beneficiary of this confusing state of affairs since my own article on [Conda vs. Pip](https://codesolid.com/conda-vs-pip/) is one of my five most popular articles of all time this month.
