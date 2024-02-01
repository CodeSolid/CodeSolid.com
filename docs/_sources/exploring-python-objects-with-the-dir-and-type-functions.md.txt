---
title: "Exploring Python Objects with the dir and type functions"
date: "2021-12-26"
categories: 
  - "python"
---
# Exploring Python Objects with the dir and type functions
Two of my favorite functions for interactively exploring Python objects are dir and type. Calling the dir function with no attributes returns information about what's defined in the current module -- either by default when you start the python interpreter, or because you've done imports, defined variables and functions and classes, etc. Calling dir and passing in a named entity in Python returns the attributes of the object it is called on. In both cases, the results are returned as an ordered list, and python pprint can be used to "pretty print" the output.

The type function is much simpler, and returns the type to which the object belongs.

Experimenting with these two functions, I recently came up with an interesting Python puzzler that I posted as a poll on LinkedIn.

![](/images/exploring-python-objects-with-the-dir-and-type-functions/ObjectQuiz.png)

Python Object Quiz -- Which of these is not an object in Python?

## The Solution

Think you know the answer? Want to check your answer against mine? Check out our YouTube video where we explain how to get the result using "dir" and "type".

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZM7iA9p-3qs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## You May Also Like

[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)
