---
title: "CodeSolid Python Newsletter:  November 1, 2022"
date: "2022-11-01"
categories: 
  - "newsletter"
---

Hello!

  
Here is your quick update from CodeSolid Python. We'll continue sending these once a week or so for now. In the future, we'll see how it goes depending on the writing schedule on the website, vacations, and other life events.

##   
New On CodeSolid

[Matplotlib vs. Seaborn](https://codesolid.com/matplotlib-vs-seaborn/)  
Author Aizhamal Zhetigenova has done another excellent article for us on Matplotlib and Seaborn.  Unlike many comparison articles, this is not a simple pros and cons list but a full coding tutorial that covers six different graph types in both tools, creating legends, and more.

  
[Python Errors: Exception Handling from Beginner to Expert](https://codesolid.com/python-errors/)  
After my recent post on custom exceptions in Python, I decided to take a step back with a broader look at handling exceptions in Python. This article features a beginner-suitable tutorial on exception handling and an opinionated look at error-handling best practices.

##   
Cool Stuff Around The Web  
 

[Modin: A Fast Drop-In Replacement for Pandas](https://modin.readthedocs.io/en/stable/)  
Modin is the first of two fast Pandas alternatives a friend sent along this week.  This one leaves the Pandas API functionality in place to minimize code changes but swaps out the single Python + NumPy backend with a distributed solution using either Ray or Dask.  According to their documentation, having a different backend allows your DataFrames to scale from a few megabytes to over a terabyte.

[Pola.rs: Lightning-fast DataFrame Library for Rust and Python](https://www.pola.rs/)  
As a Python blogger, I feel that I must confess that I’m also a big fan of Rust. Pola.rs is written in Rust and sports similar APIs across  Rust and Python.  Looking over the documentation for the Polar.rs API, it looks much more intuitive than Pandas.  This is especially true when it comes to selecting data. The published benchmarks also look very impressive, not only against Pandas but against Modin as well.

[Web Automation:  Don’t Use Selenium, Use Playwright](https://new.pythonforengineers.com/blog/web-automation-dont-use-selenium-use-playwright/)  
Speaking of alternatives, Shantnu Tiwari makes a case on his blog for Playwright, a web testing tool that features a test generator you can use to interact with a site in a browser while generating functioning Python test code for the test scenario for you.

[A Curve-Fitting Algorithm in NumPy and Python](https://github.com/abnerbog/levenberg-marquardt-method)  
Abner Bogan shared the code for an implementation of the Levenberg-Marquardt curve-fitting algorithm. I include it here partly as a testament to the power of having some excellent animated graphics in your repository’s README file.  Beyond that, I’d love to try this code out at some point.  Curve fitting is an issue I think about every time I look at my web traffic data, which features mini-spikes weekly and a more major one whenever a post takes off.  The curve-fitting algorithms I've used don't handle this very well.

[Algorithms and Data Structures in Python](https://github.com/SamirPaul1/DSAlgo)  
Student Samir Paul has pushed a large repository of Data Structures and Algorithms implemented in Python.  With some included Leetcode solutions, I’m sure this was a learning exercise and resume piece, but I thought it was worth pointing out just based on what was a substantial effort.
