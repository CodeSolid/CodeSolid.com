---
title: "Why Is Python Popular?"
date: "2022-01-24"
categories: 
  - "python"
  - "python-for-beginners-posts"
coverImage: "popularity.jpeg"
---
# Why Is Python Popular

Python is popular because it is simple to learn and use, with a syntax that makes it as easy to understand as plain English. This ease of use together with highly optimized libraries written in C has made it a favorite in the scientific community, especially for data science and machine learning.

Python is not just popular -- as of late 2021 it has taken the top spot as the #1 programming language. That's not bad at all for a language that began its life at the end of the 1980s. As we entered 2022, the TIOBE index named Python the Language of the Year for the 2021.

Python has reached this position because it is an outstanding general-purpose programming language, yet for all its strengths, it's not perfect for every situation. There are many use cases where Python is the best choice, but there are also a few areas where it makes no sense at all to work in Python.

In this article, we dig into what we think are the features that made Python as popular as it is, while at the same time being clear about its limitations and the areas where it is not a good fit.



## Ease Of Use: The Developer Is the User

Although it supports a wide range of programming styles from simple linear scripts to object-oriented and functional idioms, Python was always easy to use and simple by design. Guido van Rossum created Python after his experience working on a less popular language called ABC, which was a major influence on Python. Like Python, it featured statement grouping by indentation, variable assignments without an explicit type definition, and infinite precision arithmetic.

To give just one example, in Java, to open a file and load the contents to a string, one needs to:

- Import classes from java.io
- Define a class
- Define a main method
- Write a try / finally block
- Write the code to open and load the file
- Compile the code using javac
- Run the code using java

In Python, one runs the following two-line file using the python executable:

```python
with open('filename.txt', 'r') as f:
    text = f.read()
```

Thanks to its integration with the shell, in IPython one can shorten that even further to this:

```python
In [1]: text = !(cat pathinfo.py)
```

In fairness, Java is faster than Python in the case of long-running processes, but the development cycle is much longer. As a friend of mine who I met working on a Java product quipped recently, "Java is a strongly typed language. You type, and you type, and you type."

The rapid development cycles that Python allows mean you can easily go from editing a large file, to opening a Python terminal to test out a quick code snippet, back to the source file to use the snippet you wrote.

For me, the question that best explains the popularity of Python is to ask "Who benefits?" from the language. On fast server back-ends like Java and C#, it's a web consumer. For front ends, still dominated by JavaScript, it's also a user of the web page. For tasks that involve a high degree of interaction on topics that already have complex domains (scientific computing, [data science](https://codesolid.com/how-to-practice-python-data-science-and-pandas/), machine learning), the main beneficiary of the language is the person using it. Python tends to win easily in these cases, since all else being equal, people will select a tool that's easy to use.

## Readability

Before learning Python, my background as a developer began with C, then C++, Java, and some other languages. When I first learned about Python and heard that it used indentation as a block delimiter, I thought that made no sense. Whitespace is significant? That's crazy -- you can't even see it!

Looking back on that position, I now see things completely differently. In the first place, any decent Python editor or IDE will keep track of the indentation for you. Secondly, I've often reviewed Java code where the indentation either misled me as to the developer's intent, or was so completely unrelated to the real structure of the code as to be unreadable.

It's true that having a language that forces consistent indentation is only one aspect of readability, and Python does have features that can sometimes lead to inconsistent code (like the many ways one can declare a simple string variable). Overall, though, I think Python is probably the most readable language I've worked with.

Moreover, Python achieves that readability in the context of a scripting language. This may seem unremarkable to you, but it probably won't if you've spent much time in Perl or bash. (If you haven't worked in it, the fact that the creator of Perl was fond of saying it stood for "Pathologically Eclectic Rubbish Lister" should tell you all you need to know about its readability).

## NumPy and the Influence of the Scientific Community

Perhaps attracted by its ease of use and readability, Python captured the attention of the scientific community early on. [The productive collaboration](https://web.archive.org/web/20190219031439/https://www.computer.org/csdl/mags/cs/2011/02/mcs2011020009.html) between the Python core development team and the scientific community between 1995 and 2005, and the attraction of developing on an open platform, led to the development of several important libraries, including NumPy and SciPy. The ability to code C extensions meant that these numeric tools could overcome the [speed limitations of Python](https://codesolid.com/is-python-slow/). Later on, Python also was used to create tools for symbolic math. [SageMath](https://sagemath.org) especially was created as a "viable free open source alternative to Magma, Maple, Mathematica and Matlab." Sage's interface for doing symbolic math is a web-based notebook interface similar to Jupyter Notebook.

In addition to Symbolic Math, a very fruitful recent outgrowth of the work on NumPy has been Pandas. Wes McKinney developed Pandas beginning in 2008, originally as a tool to perform quantitative analysis on financial data. However, the tool was later more broadly adopted for general data science tasks. Pandas added useful abstractions to NumPy's n-dimensional arrays. The most important of these is the DataFrame, a two-dimensional, indexed wrapper around NumPy arrays.

Pandas allowed for read/write interoperability with many popular data sources like SQL data sources, JSON, CSV, Excel and others. It also allowed for slicing, sub-setting, data cleaning, and many other critical operations on in-memory data sets. Together with IPython Notebooks (later "[Jupyter Notebooks](https://codesolid.com/jupyter-notebook-a-complete-introduction/)") and powerful plotting tools like Matplotlib and Seaborn, Pandas provided a powerful tool for interactive data analysis and visualization.

Pandas allowed for efficient data science work on the desktop, but that was not the end of the story. This to some extent enabled the further elaboration of scalable, Python-based Machine Learning tools like TensorFlow and PyTorch, which allowed for running Machine Learning Jobs on various GPU / CPU configurations. This in turn spawned cloud base Notebook / Machine Learning offerings such as Google's CoLab and Amazon's SageMaker.

Python is not entirely ubiquitous in the data science community, where R still holds significant mind share and Julia has made some inroads. However, I think it's not a stretch to say that it's the dominant language in use today. One of the things that struck me during my brief sojourn learning R was that it was a great language for raw statistical analysis, but left a lot to be desired as a general purpose programming language.

## Other Important Use Cases

Beyond the scientific community, there are other areas where Python is an important language. One such area is cloud computing, where -- at least on AWS -- it holds the same sort of dominant position as it does in data science. AWS does significant "dogfooding" of their Python cloud API, botocore, which is [developed in tandem](https://github.com/aws/aws-cli/blob/develop/requirements.txt) with the AWS command line tool. Botocore, in turn, is the core dependency on which the current version of the AWS Python API, boto3, depends.

As you might expect when you reflect on the players involved, other cloud platforms tend to favor their own more or less proprietary languages. .NET and PowerShell are favorites at Microsoft, and Google does a lot of work in Go, for example.

Nevertheless, Google and Microsoft still actively maintain Python APIs. For all these platforms, Python is an important language to support. As we discussed earlier, one way to think about Python is as a highly readable and productive scripting language. For that reason, system administrators and DevOps engineers do a lot of work in the language. Because much of the cloud computing business boils down to the somewhat unglamorous task of migrating applications, there's plenty of DevOps in the mix on such projects.

Another area where Python seems to be gaining in popularity is back-end web development. For a long time, my sense was that Python was a niche player here compared to some other back end stacks, but that seems to have shifted recently. For example, some Google trends searches I conducted recently showed Python Django well ahead of both ASP.net and Java Spring. Comparisons with Node are a bit harder to evaluate, given that it's also the predominant front end build tool.

In part, it may be that Python's popularity elsewhere is driving developer interest in the language. Another factor at play here is that more and more web applications now run in Docker containers, which might each use a single CPU [or a portion of one](https://www.batey.info/cgroup-cpu-shares-for-kubernetes.html). This erases the advantage for multicore machines that platforms like Spring formerly enjoyed. Today, single process backend platforms like Django, Flask, and NodeJS have become more feasible.

## Areas Where Python Is Not Popular

As we've seen, there are several areas where Python is either a dominant language or a strong contender. There is, however, at least one use case for which Python is definitely not well suited: user interface development.

On web front ends, -- notwithstanding the history of Java Applets, ActiveX Controls, and now Web Assembly -- JavaScript wins. Full stop.

JavaScript is also somewhat important on mobile platforms, where tools like React Native can be use for cross-platform development. More commonly, however, the winner on native mobile platforms are Java and Kotlin for Android, and Swift and Objective-C for iOS.

Even on the desktop, Python has not made major inroads as a user interface language (at least for non-terminal apps). It is hindered in this area by the lack of good tooling for creating binary distributions.

Another area where Python plays a somewhat minor role is embedded computing, which is dominated by C. However, I have seen cases where the embedded code was written in C, but driven by a Python test bed.

## Closing Thoughts

I began to program seriously in 1990, and at the time, the cool kids were learning C and C++. A lot has happened since, but it was not until I learned Python that I got a taste of the same kind of joy I had when I was first learning C. Your mileage may vary, of course, but for my part, I was very excited to see Python enjoying the number one spot last year. In any case, I can share with you that in addition to being popular, Python is also great fun!  
  
And perhaps with that fun, we've found the best explanation for Python's success.

## You May Also Like

[Python Dataclass: Easily Automate Class Best Practices](https://codesolid.com/python-dataclasses/)
