---
title: "What Is a Python Package?"
date: "2022-01-20"
categories: 
  - "python"
coverImage: "this-is-engineering-woman-smaller.jpg"
---

A Python package is simply a directory, usually containing Python modules (source files with the .py extension). It frequently will include a special marker file**,** `__init__.py`. Packages can easily be created and used locally, and published packages can be installed using pip.

Learning to install public packages and create packages locally is not difficult, though I've noticed that even experienced developers coming from other languages can have a tough time at first with how Python modules, packages, and import statements work.

This article is a tutorial that's meant to cover Python packages, modules, and import statements in enough depth for a beginner to intermediate Python developer. The goal is to answer common questions people have about these topics. We also will strive to explain everything clearly and step by step, to show you errors you might see along the way and how to solve them, and to illustrate how things work with simple examples.


## What's the Difference Between a Python Package and a Module?

Before we get into how to install packages and how to import packages and modules, let's make sure we're clear on some terminology in Python:

A **module** in Python is simply a text file with the extension ".py" that contains Python source code. It can consist of classes, functions, and variables.

A **package** is a directory that creates a namespace, usually to house a collection of modules, while a module is just a simple python source code file. You can define and create packages locally, or install packages that other developers have published. Published packages generally live on [PyPi.org](https://pypi.org) (The "Python Package Index"). The most common tool for installing packages is pip, which downloads and installs packages from PyPi directly.

A **library** is a common term that people use for a group of functions or classes you can use. In Python, when someone talks about a library, they may mean a package, but they also may even have in mind a module, for example, "the Python 'math' library".

The **import** statement in Python allows you to use functions, classes, and variables that are defined in Python packages and modules. We have several examples showing how this is done in the next section.

## How do I use the Import Statement in Python?

The import statement is like an awesome Swiss army knife. It can be used to import whole packages, individual modules, and even functions or variables contained in a package or module.

To see how this works, let's say you have a directory, package\_demo, with contents that looks like this:

```bash
.
├── package1
│   ├── __init__.py
│   ├── mymodule.py
├── package2
│   └── __init__.py
├── package3
│   └── hello.py
├── package4
└── pathinfo.py
```

Now, let's assume you're running Python 3.3 or later, and from the package\_demo directory you run `python3`. In the interactive terminal, the following commands will work (for example):

```python
# import the module hello from package3. Following this 
# statement, you call functions in the module like this:
# package3.hello.greet()

import package3.hello

# Import the pathprint module from package1, 
# and alias the module as mm.  With this alias, the greet function 
# above would be called as mm.greet()
import package1.mymodule as mm

# Import 2 packages with no modules to speak of in them.  
# This works, but at least in the case of package4, it isn't useful since there's no code in the package.

import package2
import package4

# Import a module from the current directory

import pathinfo

# Import a package that's not local, but we know comes with Python
# Packages that come 
# This allows us to call json.loads, json.dumps, etc.

import json

# Import only a specific function from a package
# Now we can drop the json and simply call "loads"

from json import loads
```

## Understanding ModuleNotFoundError

The ModuleNotFoundError is probably the most common error related to packages and modules you may encounter. This error occurs when an import statement does not work, and though it says ModuleNotFoundError, you'll get the same error whether you're trying to import a package or a module.

Given the scenario above, all the following would likely produce a ModuleNotFoundError

```python
# Try to import a local directory that doesn't exist:

import package5

# Import a package that's published and pip can install but you likely 
# don't have installed on your system.

import hellosetup


# Import another name Python can't resolve

import some_crazy_random_name
```

So, broadly speaking, ModuleNotFoundError happens when you try to import any other name that is not:

- Available locally relative to the working directory
- A package that's available by default
- A package you installed with pip

A more precise way to state it is that Python failed to find the module or package on the paths in the `sys.path` list. We'll discuss `sys.path` in greater detail below after we discuss the recommended way to install Python packages.

## How to Install Python Packages

The most commonly used tool to install packages in Python is pip. Pip has come with Python installs by default [since version 3.4](https://docs.python.org/3/whatsnew/3.4.html#whatsnew-pep-453).

### Making Sure Your Pip Version Is Correct

For Python 3.x releases, it's a good idea to check first that your pip version is pointing to Python 3. The "`pip --version`" command will show you:

- The version of pip
- Where it's installed
- What version of Python it's using

If any of those things points to a Python 2 release, it's a good idea to try using the command `pip3` instead of `pip` for the discussion that follows.

### How to Install Packages (The Right Way)

Most experienced Python developers will recommend that rather than installing packages globally, you create a virtual environment. Python virtual environments are basically a way to create and activate a local copy of some core Python tools. With a virtual environment (or "venv") active, any Python packages you install will be isolated from the rest of your system.

In the next section, we'll discuss why we want to do this. For now, let's just focus on the how. Using Python virtual environments consists of a few steps. If you're a beginner, these may look hard when you first read them, but if you practice them a few times you'll soon do them automatically.

#### 1\. Creating the Virtual Environment:

First, we create the environment. Usually I'll do this in a new directory, or in any case, one that doesn't already have a virtual environment. For example:

```bash
mkdir my_project
cd my_project
python3 -m venv .venv
```

What we're doing in the last line is telling python to run the module (-m) named venv, and place the results in a directory named .venv. Beginning the directory name with a period like this makes it hidden on Mac and Linux, but you can also just call it `venv` if you want.

Our next step is to activate the virtual environment. This is different on Windows than it is on Mac / Linux.

#### 2\. Activating the Virtual Environment:

On Windows:

```bash
.venv\scripts\activate
```

On Linux / Mac

```bash
source .venv/bin/activate
```

Python gives us a clue that the environment is now active. The terminal command prompt will change to show the virtual environment is active by adding `(.venv)` to the beginning of the prompt. Here's a simplified view showing how it looks on my machine:

```bash
package_demo % 
package_demo % source .venv/bin/activate
(.venv) package_demo %
```

#### 3\. Using the Virtual Environment:

You can now run python commands, run pip install, etc., as you normally would, but whatever you do will be isolated to your virtual environment. For example, let's suppose you have a website you want to test, so you want to install the requests package.

```bash
# Install the package
% pip install requests  
...
Successfully installed requests-2.27.1

# Use it.
% python

>>> import requests

# Make sure your favorite web site is up and running:
>>> requests.get("https://codesolid.com").status_code == 200
True
```

#### 4\. Deactivating the Virtual Environment:

If you need to get back to a normal shell prompt, entering the command `deactivate` will do it. You can go back in and reactivate it any time, just do what you did in Step 2.

### Dependency Hell -- Why We Set Up Virtual Environments

If you install a lot of Python packages globally on your system, you may sooner or later run into an issue that the Python community affectionately calls "dependency hell". (Well, OK, I guess the "hell" part means we're not that affectionate about it). Creating a virtual environment is one way to lessen the chance of ending up in that Bad Place.

Dependency hell comes in a variety of not-so-delicious flavors:

- You work on one project written with an older version of Pandas, and have another project where you need features in the latest version. If you upgrade Pandas for the second project, you might break the first.
- You install package B, which says it depends on a version of Package A that's less than version 2. Now you want to install package C, but package C relies on Package A version 2.5.

Working with a virtual environment, the chances that you'll end up in dependency hell are a lot lower than if you install everything globally. It can still happen, it's just a lot less frequent and easier to manage if it only affects a single project, and not everything on your computer.

## How Python Finds Packages

When we discussed importing packages, dealing with ModuleNotFoundError, and creating virtual environments, you may have been wondering how Python even finds modules and packages. We noticed that if we are in the terminal in a given directory, we can import files in that directory, and packages that are subdirectories. When we talked about venv, we said we installed the "requests" package into the virtual environment only, but what does that mean? Where exactly did the code for that package end up?

The answer is that when Python runs, it sets up a variable named `path` in the `sys` module that it uses to resolve imports. The variable is nothing more than a list of paths. Here's a very simple program we can use to explore this `sys.path` variable to learn more about the Python defaults:

```python
# pathinfo.py

"""
pathinfo:

Uses pretty-print to print the sys.path variable.  sys.path contains 
a list of the places where Python will try to resolve imports. 
"""

import sys
import pprint

pprint.pprint(sys.path)
```

Let's see what this outputs. For context, the `package_demo` directory on my machine is located at `/Users/johnlockwood/package_demo`, and the pathinfo.py module (in this case a simple Python script) is in that directory. If I run it, with my virtual machine active, here's how it looks:

```bash
python pathinfo.py 
```

Output:

```bash
['/Users/johnlockwood/package_demo',
 '/Users/johnlockwood/.pyenv/versions/3.10.1/lib/python310.zip',
 '/Users/johnlockwood/.pyenv/versions/3.10.1/lib/python3.10',
 '/Users/johnlockwood/.pyenv/versions/3.10.1/lib/python3.10/lib-dynload'
 '/Users/johnlockwood/package_demo/.venv/lib/python3.10/site-packages']
```

So let's break this down to show where Python is looking to find modules and packages to run:

1. The **current working directory**. Note that the first entry is in the list is the full path to the current directory in my terminal. When we were importing modules and packages relative that were in the current directory, this is the path that allows Python to resolve them.
2. The **python standard library**. The second and third entries are interesting. The second, python310.zip, is a file that doesn't exist on my machine. This may have been the original source on my machine, or a way to hot-patch it, but as of now, I can only guess. The third directory, "`lib/python3.10`", is where Python keeps the standard runtime library files and packages. When you find that "`lib/python<version>`" directory on your machine, you can learn a lot just by examining the contents. For example, remember when we used "python -m venv <directory\_name>" command earlier to create a virtual machine? Well, you can read the source for the venv module we used in the "venv" package (directory) inside "`lib/python<version>`".
3. **Compiled C binaries for the standard library**. The third directory that ends with "`lib-dynload`" contains additional standard library code, but the files here are not source files, they are highly performant binary files written compiled from C code. In some cases, a whole package is here (.e.g., "math"), but sometimes the source is split between a Python wrapper and a some optimized code in C (e.g., "json").
4. **The directory where pip will install packages in the virtual environment**. The directory that ends with "`.venv/lib/python3.10/site-packages`" is where Python installed our requests library and its dependencies when we installed the "`requests`" package earlier. This is exactly what we wanted -- we set up the virtual environment to escape from dependency hell. When I use "`deactivate`" to exit from the virtual environment, if I run the pathinfo.py script again, this virtual environment "`site-packages`" directory is replaced with the global `site-packages` directory.

```bash
(.venv) ... package_demo % deactivate

... package_demo % python pathinfo.py 

# Other lines as before, then:

 '/Users/johnlockwood/.pyenv/versions/3.10.1/lib/python3.10/site-packages']
```

Note that on Windows, you'll find different directories for your installed Python version. The Python standard library files are located in "`Lib`", while the C binaries appear to be mostly in "`libs`", with additional DLLs (dynamic link libraries) in the "`DLLs`" directory.

## Changing the Python Path and Controlling Where Pip Installs Packages (Case Study)

One of the projects I've worked on recently was for a company that had strict security requirements, so their build environment for production builds did not allow connecting to external sites (including PyPi.org). I was tasked with creating an AWS Lambda function in Python that relied on some third party packages. How was this done?  
  
Because the production build system could access our source repository, but could not connect to PyPi, the solution I was simply to do the pip install using the pip "`--target`" switch. Unlike the default option and the venv solution, which sets up different reasonable defaults for a target directory, the `--target` command line option allows you to specify precisely any arbitrary directory where you want to install things. We could therefore check in dependencies along with code, by running "`pip install --target . <some_dependency>`" in the current directory. Since Python can also load packages in the current directory, the Lamba function handler had no problem in importing these packages.

On reviewing the code, a colleague suggested we make it clear that these were third party dependencies by installing these third party packages into a subdirectory called "`dependencies`". To understand how this was accomplished, remember that `sys.path` is just a list, so we can modify it. As long as we modify it ahead of the import call, this works just fine. For example:

```
# handler.py

""" AWS Lambda handler function """

# Must do this part first:
import sys
sys.path.append("./dependencies")

# Now import whatever other packages are needed
import requests

# remaining handler code
```

Another way to add a path to the locations where Python looks for packages is to set an environment variable, `PYTHONPATH`, but this should only be done as a temporary solution in a local environment.

Changing the Python path is not something you'll need to do often, and it should be a last resort tool that you reserve for special cases. Nevertheless, it's useful to know.

## How Do I Publish a Package in Python?

Let's say that you've created a local package that contains more than just some test files as we've shown here, but some code you want to publish for others to use. There are several tools in the Python ecosystem to facilitate building and publishing packages.

The most mainstream choice for many years -- and still going strong today -- is the combination of Setuptools for building and packaging and Twine for publishing the package. If you're interested in this option, we have a complete tutorial on how to do it in our article, [Python Package Example: Setuptools](https://codesolid.com/python-package-example-setuptools/).

Another awesome tool in this space is [Python Poetry](https://python-poetry.org/) -- and we really need to write an article on this tool as well. Poetry is a simple and elegant dependency manager and package builder and publishing tool in one -- so you can think of it as a single tool that does the work of the Python venv module, pip, Setuptools, and twine. I have written a lot about pip and venv because I know that they are core tools that continue to be used on many projects, so beginners should be aware of them. However, if I were beginning a serious Python package development effort today and had a choice of tools, I'd probably start with Poetry.

Two tools that have gained somewhat less traction are [Bento](https://cournape.github.io/Bento/) (for building packages) and [Flit](https://flit.readthedocs.io/) (which supports both building the package and publishing it to PyPi).

## Final Thoughts and Source Code

Spending a little time working with Python packages is worth it and will make you an expert in no time. I hope this article helped save you a bit of time and added to your understanding of Python internals. This article was mostly discussion / demo, but if you'd like to grab pathinfo.py and the directory and code structure we used for the "package-demo" example, the source is available in the day-11 directory of our repository, [100 Days of Python](https://github.com/JohnLockwood/100-days-of-python).
