---
title: "Is PyPy a Faster Version of Python?"
date: "2022-02-07"
categories: 
  - "python"
  - "python-tools"
coverImage: "pypy_logo.jpeg"
---

Today I spent some time taking a look at PyPy. I had expected it to be much faster than the "standard" version of Python, also known as CPython. However, I also wanted to account for speed differences when it comes to NumPy, a commonly used Python library written in C.

PyPy is faster than CPython when comparing raw Python performance -- roughly 3.5 times to 6 times faster in the tests we did. However, for operations using NumPy, PyPy can actually perform more slowly than CPython. Where Python integrates with NumPy, the results can even be more substantial.

## Other Python Implementations

What most people mean when they think of Python is actually a specific implementation of Python, which is known as CPython. CPython is the reference implementation of Python, and it's the most widely used version, but there are several other implementations available.

- **Jython**. Jython was an early implementation of Python on the Java Virtual Machine (JVM). Jython currently lists 2.7.2 as the most recent version, and the last commit for many of the top level directories in the Jython repository took place several years ago. So I believe this is more of a historical curiosity at this point than a useful tool.
- **IronPython**. Of course, with Python running on the JVM, it was only a matter of time before someone would try to do the same thing on the .NET platform as well. IronPython does look like it has been more actively maintained than Jython, so it's not so far behind. There's currently an alpha version of Python 3.4 that came out in 2021 -- but that's still not modern. In the CPython world, 3.4 is already marked as [End of Life](https://www.python.org/downloads/release/python-3410/).
- **Cython**. In this discussion, Cython is a bit of an outlier, since it's not really a different Python implementation. Instead, Cython is really CPython with a set of extensions for interfacing Python with C. It also features an optimizing compiler for compiling either standard Python code or -- for even more of a performance boost -- Python with Cython type declarations. In the latter case, the optimizing compiler can generate code that does not need to incur the overhead of dynamic types.
- **Stackless Python.** This was an attempt to add "microthreads" (called "tasklets" in Stackless Python). Tasklets wrap callable functions. On the face of it, this looks a lot like what CPython has done more recently with asyncio, but I've yet to find or investigate how these two really compare.
- **MicroPython**. This is a version of Python 3 that includes a subset of the standard library and is designed to run on constrained environments like microcontrollers.
- **PyPy**. Not to be confused with PyPi.org, the Python Package Index, PyPy is the name for an implementation of Python based on RPython, which was an attempt to provide generic support for building dynamic languages. The RPython site lists [several other projects](https://rpython.readthedocs.io/en/latest/examples.html) based on this tool -- but PyPy is probably the most famous offshoot in this breed.

PyPy makes the claim that it is a faster version of Python than CPython, and that it's highly compatible with it. In kicking the tires on PyPy, we set out not to exhaustively prove or disprove that claim one way or another, but simply to get a sense of how well it held up for some code to which we had ready access.

## A Simple Test Case

To get an idea of how compatible PyPy was with CPython, I decided to take a project I had that -- in fairness -- was not exactly a huge benchmark or anything, but at least had a few packages including some minimal, C-based data science goodies in the mix. I made a copy of my Jupyter notebook and requirements.txt from the [Python Lists versus Arrays](https://codesolid.com/python-lists-vs-arrays/) article I wrote recently.

In addition to relying on Jupyter and NumPy, which I thought would do at least a basic test of compatibility, this project already had several simple benchmarks coded up that I could run through PyPy to see how the performance compared.

## PyPy First Impressions: Some Installation Issues

As I do now with most Python tools, I used PyEnv to see if there was a supported version of PyPy that I could install. At the time of this writing, the most recent version available is pypy3.8-7.3.7, so I installed and set it as a local version using pyenv:

```bash
pyenv install pypy3.8-7.3.7
pyenv local pypy3.8-7.3.7
```

PyPy installed with no issues, and so I next created a virtual environment with it, activated it, and tried installing the requirements.txt I had from my article. At this point, I ran into a problem when building pyzmq (the Python client for zeromq). The solution I found was to change the C++ standard library being used in the build, as follows:

```
export CFLAGS="--stdlib=libc++"
```

  
It's unclear why CPython didn't run into the same issue, but I confirmed that it had gotten through the zeromq build seamlessly without that fix.

## Evaluating PyPy Performance

Once this was resolved, I decided to install Jupyter and NumPy independently of the earlier requirements.txt. At this point, I was able to re-run the benchmarks I ran in the Lists vs Arrays article. I won't repeat much of the detailed code here since I already published it there, but here is a summary comparison.

<table><tbody><tr><td>Benchmark</td><td>Time in CPython</td><td>Time in PyPy</td><td>Difference</td></tr><tr><td>10000 x 10000 numbers in list iterated</td><td>0.82558875</td><td>0.236211458</td><td>3.50 times faster</td></tr><tr><td>10000 x 10000 numbers in array iterated</td><td>1.369477958</td><td>0.228980292</td><td>5.98 times faster</td></tr><tr><td>Python sum on a list of 256,000 numbers</td><td>0.597</td><td>0.29</td><td>2.06 times faster</td></tr><tr><td>Python sum on a bytearray of 256,000 numbers</td><td>0.544</td><td>0.633</td><td>1.16 times slower</td></tr><tr><td>Python sum on numpy array 256,000 numbers</td><td>4.8544</td><td>74.7397</td><td>15.40 times slower</td></tr><tr><td>Numpy sum on numpy array 256,000 numbers</td><td>0.05</td><td>0.056</td><td>1.12 times slower</td></tr></tbody></table>

## Some Final Thoughts

This comparison of PyPy and CPython should be taking as a starting point only. It's fair to point out that not only was it very limited in scope, the version of CPython I used was probably much more recent (though in fairness, I did pick what appeared to be the latest PyPy version in PyEnv as a basis for comparison). If you're interested in a much more complete set of benchmarks, see the [Python Speed Center](https://speed.python.org/about/). However, I confess that even there, I don't find the results to be compelling enough to move off of the reference implementation, CPython.

I did find the build issues that I ran into with PyPy to be a bit of an annoyance -- all the more so because my test case was relatively simple. I'd be curious to see if any major projects are running on PyPy. My own feeling is that unless there's a really compelling reason to move off of it, I would stick with either the reference implementation (CPython), or perhaps take the sort of mixed Python and C approach that Cython facilitates. While it's fun to kick the tires on alternative implementations of Python, the benefits in the case of PyPy don't seem to be worth the risks.

## You May Also Like

[Learning C++ and Python: The Perfect Duo for Success](https://codesolid.com/learning-c-and-python-the-perfect-duo-for-success/)

[How to Profile Python Code](https://codesolid.com/how-do-i-profile-python-code/)
