---
title: "Pip vs Pipenv: Which is better and which to learn first?"
date: "2022-01-07"
categories: 
  - "python-tools"
coverImage: "programmer.jpeg"
---

Pipenv and pip are both excellent tools for installing and managing Python dependencies that are widely adopted and work extremely well.

Learning pip well first is the choice we recommend. Pip is established and widely known, so many teams prefer pip and venv to manage dependencies and virtual environments. Pipenv makes a few things simpler, but for every thing it simplifies, it makes other things more complex than they need to be.

We'll show you why creating virtual environments and using pip to install packages is not difficult. This will highlight some strengths of pip as compared to pipenv. Then, we'll go on to discuss the problems with pip that pipenv tries to solve, but fair warning -- the more we dug into pipenv, the more we longed for the simplicity of pip!


## Getting Started with Pip and Virtual Environments

Compared to pipenv, pip is more tightly integrated with Python. Many Python distributions now include pip by default, so you don't need to do anything extra to get it. You can run the `pip --version` to see if it's on your path and which version of Python it's using. (Note that for python3, in some distributions it may be called "pip3").

If you don't have pip or notice a problem, [installing it is straightforward](https://pip.pypa.io/en/stable/installation).

The command, `pip install`, will install a pip package globally so that all your Python projects will have it available, but since this can cause many version conflicts if you work on different projects and is difficult to reason about when you work on a team, it is strongly discouraged. Instead, pip is usually used to install packages into a virtual environment. The python "venv" module can be used to create the virtual environment.

## Your First Virtual Environment in Under Five Minutes

Here are two commands I've used many, many times -- I generally run this at the start of every Python project I work on. This will go quickly, I promise, but you should write these lines down somewhere!

```bash
# create a virtual environment in the .venv directory:
% python3 -m venv .venv

# Make the virtual environment active (Linux / Mac)
% source .venv/bin/activate

# OR

# Make the virtual environment active (Windows)
.venv\Scripts\activate.bat
```

At this point, you're all set to start working with your new virtual environment, and you can safely use pip to install packages into it. There's one last housekeeping item we should take care of first, though. If you're working in a git repository, it's recommended to add these lines to your .gitignore file:

```bash
# Ignore common virtual environment names anywhere in project
**/venv
**/.venv
```

## Using Pip to Install Packages Into a Virtual Environment

With our virtual environment installed and activated, we can now start installing packages into it that we can use. Let's say we want to install pandas. There are several ways to go about this. Let's start with the simplest:

```bash
% pip install pandas

...
Successfully installed numpy-1.22.0 pandas-1.3.5 python-dateutil-2.8.2 pytz-2021.3 six-1.16.0
```

This will take a minute or two to install. Before we go further into this, let's take a moment to celebrate our first victory.

## Testing the Pip Install Results

Did this work? Let's see....

```
% python
...
>>> import pandas as pd
>>> import numpy as np
```

As you saw, the last line showed the dependencies that were installed. (Note that your versions will be different, depending on when you try this). For the current virtual environment, you can always list all the installed packages and their dependencies using pip freeze".

```bash
% pip freeze
numpy==1.22.0
pandas==1.3.5
python-dateutil==2.8.2
pytz==2021.3
six==1.16.0
```

## How to Use "requirements.txt"

When we installed pandas, we just used `pip install pandas` and that was enough to get the latest version, which turned out (at the time of this writing) to be 1.3.5. For learning purposes, just working with the latest official release of a package is probably sufficient.

However, on a team working on a production product, or even as a lone developer with a project that has a significant amount of code, you need a way to create and document a reproducible build. Many teams use a file -- usually called requirements.txt -- for this purpose. A requirements.txt file contains packages to be installed, one per line. You install it using the following command:

```bash
pip install -r requirements.txt
```

## Creating requirements.txt and Using Pinned Requirements

There are at least two ways to create a requirements.txt file. The easiest is to simply redirect the output of pip freeze:

```
pip freeze > requirements.txt
```

  
A benefit of this approach is that it shows all the requirements for the projects, and all of them are pinned. A pinned requirement is like the line we saw we ran pip freeze earlier: "pandas==1.3.5". The double equals sign between the package name and version number tells pip, "give me exactly this version". Though it's less common, you can also use a pinned requirement on the command line, i.e., "`pip install pandas==1.3.5`". This is useful, for example, to reproduce a bug that you know to be in a specific version. As we saw, though, the more common use at the command line is simply "pip install SomeProject".

Pip also supports many other operators and combinations that are used far less frequently than pinned versions, such as `pip install "SomeProject>=1.2,<2"`. Here you want some version greater than or equal to 1.2, but less than 2.

## Should You Create requirements.txt Using Pip Freeze?

Redirecting pip freeze is a time-honored approach and one you'll see often documented, but it does have a problem. Let's say three months from now, the team no longer needs pandas, and you're asked to remove it from the build. So you go in and remove the line `pandas==1.3.5`. That makes sense, right? Well, I agree it does make sense, but the issue is that it still leaves in all the dependencies that pandas relied on that also got installed.

For this reason, many teams will instead just create their requirements.txt file manually, by adding one pinned, top-level package at a time. For our example, requirements.txt would look like this:

```bash
pandas==1.3.5
```

This approach ensures that for production builds at least, if pandas is removed, neither it nor its dependencies will be installed. (Some developers will use another package, pip-autoremove, to uninstall sub-dependencies locally, but another tactic is to simply rebuild the local virtual environment from time to time from requirements.txt).

## Problems that Pipenv Tries to Solve

Pipenv tries to solve some problems with using requirements.txt and Python virtual environments in the traditional way that we've described above.

We've already seen two of these problems. First, ipenv's documentation claims that "You no longer need to use `pip` and `virtualenv` separately. They work together."  
  
Well, that's true as far as it goes, and I have to admit I thought it was a feature until I committed "`python3 -m venv .venv`" and "`source .venv/bin/activate`" to finger memory. But rather than put your virtual directory in .venv or some other reasonable place that is _exactly where you told it to put it_ (you know, like a useful tool), it puts them into a hashed directory under your user home directory. To prevent that behavior, you need to set an environment variable:

```bash
export PIPENV_VENV_IN_PROJECT="enabled"
```

I understand that some tools are opinionated, but to my way of thinking, not having a command-line switch, `--local` or the like, is not just opinionated -- it's "my way or the highway".

Another problem we've glimpsed in our discussion of pip that pipenv solves is that of separating the user's initial intent to just install the latest package from a pinned version of what was already built. Pipenv does this by separating having two separate files, a "Pipfile" that contains general project information including a "packages" section for our intended dependencies, together with a Pipfile.lock file which contains the actual versions installed and their dependencies. It also includes a handy command, `pipenv graph`, to show top-level dependencies and what they depend on. If we just install pandas as we have been doing, here's how it looks:

```bash
% pipenv graph  
pandas==1.3.5
  - numpy [required: >=1.21.0, installed: 1.22.0]
  - python-dateutil [required: >=2.7.3, installed: 2.8.2]
    - six [required: >=1.5, installed: 1.16.0]
  - pytz [required: >=2017.3, installed: 2021.3]
```

You can also see the dependency graph using pip itself, but it requires installing a separate package, [pipdeptree](https://pypi.org/project/pipdeptree/). So in due fairness to pipenv, having this capability integrated into the tool is a nice touch.

## Pip-tools vs Pipenv

Since pipenv and pip-tools have some overlap in terms of functionality, we should compare them briefly. Both pip-tools and pipenv are used to manage packages and dependencies, but they take different approaches. pip-tools is a more traditional approach that uses a requirements.txt file to track dependencies. (It can create the requirements.txt complete with pinned requirements from a requirements.in file). The requirements.txt file is then used to install packages via the pip command-line tool.

By contrast, pipenv takes a "live" approach to dependency management. It automatically generates a Pipfile, which tracks both production and development dependencies. This file can then be used to install all required packages with a single command. In addition, as we've seen, pipenv can also be used to create virtual environments, which is helpful for isolating different projects. Ultimately, the choice between pip-tools and pipenv depends on personal preferences and project requirements.

## Final Thoughts

Pipenv does contain some interesting convenience functions that pip lacks, and the attempt to build them into a single tool was a worthwhile effort. On balance, however, and especially for Python beginners, the tool of choice that we recommend for Python package management is pip.

As we've seen, most of the effort that one needs to get started creating and activating a virtual environment just using basic Python boils down to learning a couple of simple command-line instructions. From that point, using pip to install packages into those environments is not complex at all.

To be sure, pipenv does have some convenience functions that are not built in to pip, but these come at a cost of a tool that is overly complex and opinionated. With pip, you have everything you need to get started out of the box, and you pay for complexity with third-party tools when you need it. With pipenv, you have to fight the tool at the beginning, and that's not what we want. After all, a package manager is meant to get out of the way and let us get on with the business of coding in Python.
