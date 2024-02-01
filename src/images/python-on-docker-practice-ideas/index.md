---
title: "Python Practice:  More Python on Docker Project Ideas"
date: "2022-04-24"
categories: 
  - "docker"
  - "python-practice"
coverImage: "this-is-engineering-woman-smaller.jpg"
---

After I wrote my article on [How To Use Docker and Docker Compose With Python](https://codesolid.com/how-to-use-docker-with-python/), it struck me that I had only begun to scratch the surface of the cool projects that might flow out of that idea.

With this in mind, I thought I'd write briefly about some of these project ideas. Usually, I'm not particularly eager to do "coming soon" posts. However, this is such a rich area for exploration that I thought it would make a good "Python Practice Ideas" article and turn into a laundry list of things I might write about. We may see some of these added to the [Python Docker Examples](https://github.com/CodeSolid/python-docker-examples) repo soon, or maybe one of our readers will get to these ideas ahead of us.

So here, then, in no particular order, are several more ideas for Python Practice projects on Docker.

## Setting Up Python Tests Independently of Code

An everyday use case for Docker Compose is relatively easy to set up. It consists of treating the container that contains the production code that one is running as a base container. It's then straightforward to have a set of unit tests built into another container. Those unit tests might run on the host machine. A more common scenario is that the production and test containers will collectively serve as the whole "ready-to-debug" developer environment.

## Showing How To Debug Python Containers

Speaking of debugging, debugging into containers is an area that might lead to some excellent articles and starter projects. On the last project I worked on, where we routinely debugged into containers professionally, I used PyCharm as an IDE. I relied on its excellent support for debugging in docker with a Docker Compose configuration. Unfortunately, however, this feature is part of the PyCharm Professional Edition, which might effectively put it out of reach of users who haven't made that purchase.

There are at least two workarounds for this. The first workaround is not to pick an IDE where you're nickel-and-dimed for features; instead, work through the recently improved VS Code documentation on setting up [Python Debugging in Containers](https://code.visualstudio.com/docs/containers/debug-python).

If suggesting that PyCharm nickels and dimes you sounds harsh, I should point out that I was much more of a Jetbrains fanboy until learning that my expensive all-products-pack didn't include pre-release software. So it's "all-products" except the ones you don't get.).

The other workaround is to show a general remote-debugging configuration using the Enhanced Python Debugger, [epdb](https://pypi.org/project/epdb/). The benefit of remote debugging is that it works not only in Docker but also in Kubernetes and anywhere else one might be able to open up a port. Of course, it appears that this other workaround also won't work for PyCharm, since remote debugging is also a paid feature:

![](images/Remote_Debugging_with_PyCharm___PyCharm.jpg)

Perhaps the best approach here is to skip PyCharm altogether and limit the discussion to VS Code.

## Other Containers to Help With Postgres and Django Development

The original example I gave for [Postgres plus Django](https://codesolid.com/how-to-use-docker-with-python/#htoc-running-django-and-postgres-using-docker-compose) provided a pretty easy-to-use starter application for Django plus Postgres. Still, I could add a great deal more to that example. Another container that would be useful in that context would be a pgAdmin container connected to the same Postgres database to which Django connects. Of course, the common workflow is to set up and run migrations using Django, but I've found it's often helpful to be able to view the database entities themselves. Moreover, one can use PgAdmin to do backups and restores of the development database, so it's a tool worth having.

Another container example could take the Postgres plus Docker Compose idea in a different direction. This would involve comparing two major Python ORM products: Djangos versus SQLAlchemy. I suspect that for most Django developers, the choice is moot since their natural (and correct!) inclination is to go with the easy, built-in Django ORM. Still, it might be fun to compare the two on a feature-by-feature basis.

## Containers for Remote Shared Python Development Environments

I am always interested in different ways I might share code with readers and allow beginners to Python to work with this code in a hands-on way. Many of the examples I've relied on have used JupyterBook (c.f. codesolid.github.io), which provides excellent integration with Google Colab.

However, another viable option here might have been something like Github Codespaces or Gitpod.io. Both of these options allow for the configuration of a full VS Code environment in a Docker container. For a shared development environment for a Python course or the like, this might prove to be a more useful option than JupyterBook, since it allows teaching a decent (free) IDE with a full-featured debugger.

## Interfacing Python and C++ or C

A research and writing area I would really like to devote more time and attention to on this blog are the many ways that one can interface and optimize Python with C or C++ code. Doing this work inside a container that supports both C++ and Python development would definitely be a plus, because C++ development is notoriously platform-specific. Focusing on the different approaches to this problem that are available while trying to support all the platforms a user might try it on would really be too much, I think, so a C++ plus Python container could at least lock down the platform side of the equation.

That said, there are _at least_ four approaches to the problem that one could explore:

- [Ctypes](https://docs.python.org/3/library/ctypes.html). This approach should be reasonably simple to demonstrate but only handles simple cases of "calling a C DLL from within Python."
- [CPython C Extensions](https://docs.python.org/3/extending/extending.html) are a mechanism for extending CPython only, but that's not a significant limitation, given that this is the implementation that most of us have in mind when we think about Python.
- [Cython](https://cython.org/) is the mechanism for interfacing C and C++ with Python that I'm most excited about digging into. It forms the basis for scikit-learn, and it seems to have the most recommendations when users ask about it on r/Python. It does take us "outside" of the CPython world somewhat, inasmuch as it provides a superset of CPython that allows compiling Cython-enhanced Python code to C. This, of course, has gotten all the nerd receptors in my nervous system firing like crazy.
- [Using the Numpy C API](https://numpy.org/doc/stable/user/c-info.html) - I suspect that this solution will be pretty specific to Numpy, but given that Numpy is the basis for Pandas, SciPy, and a zillion other wonderful things, as "limited choice" options go this should still be pretty interesting.

## Serverless C++? You Know You Want Some

As we've discussed before in the context of reviewing [Python careers](https://codesolid.com/career-paths-for-python-programmers/), AWS Lambda functions are one of the areas where Python is heavily used. We've covered [Python Lambda functions](https://codesolid.com/python-and-aws-lambda-functions/) in a basic way, but in addition to hosting functions written in native Python (or JavaScript, or what have you), AWS Lambda also supports running functions based on [custom containers](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html).

Creating and launching such a container to run Python would be an interesting exercise in itself, but would not add much value beyond what one can do simply by deploying a Python AWS Lambda function in the usual way, without a custom container. However, the ability to interface with C++ in the last section suggests that we could provide some support -- albeit in a very custom way -- for running C++ code in AWS Lambda.
