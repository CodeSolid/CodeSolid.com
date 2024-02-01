---
title: "The Function In Python: An Introductory Tutorial"
date: "2022-06-22"
categories: 
  - "python-functions"
coverImage: "programmer-hands-small.jpg"
---

Writing effective functions is a crucial skill to master, in Python or in any programming language. Learning to write and use Python functions is like playing the game of Go or Chess. Understanding the game's basic rules is simple enough, and you can quickly master these after a short introduction. However, learning to play well can be a challenging, lifetime adventure.

If you're a new programmer, learning to write functions is the first leap you'll take away from treating Python as a "quick and dirty" scripting language to a sophisticated general-purpose language that lets you write robust, maintainable code.

Table of Contents

- [Introduction](#htoc-part-i-python-function-tutorial)
    - [What Is a Function in Python?](#htoc-what-is-a-function-in-python)
    - [Python Functions: Some Examples](#htoc-python-functions-some-examples)
    - [Keyword Arguments and Positional Arguments](#htoc-keyword-arguments-and-positional-arguments)
    - [Default Parameters](#htoc-default-parameters)
    - [Return Values](#htoc-return-values)
    - [Early Returns from a Function](#htoc-early-returns-from-a-function)
    - [Multiple Return Values from a Python Function](#htoc-multiple-return-values-from-a-python-function)
    - [Functions with No Return Value](#htoc-functions-with-no-return-value)
- [You May Also Enjoy](#htoc-you-may-also-enjoy)

## Introduction

Welcome to this tutorial on functions in Python! In this tutorial, you will learn how to define and use functions in Python.

Functions are essential to any programming language, as they allow you to reuse code and compartmentalize your program into logical blocks. In Python, functions are defined using the `def` keyword, and are called using the function name followed by parentheses.

Writing good functions is a crucial first step to becoming an effective Python programmer.

### What Is a Function in Python?

As with everything in programming, the best way to understand functions is by example, but before we get to those, let's begin with a formal definition.

A Python function is named, callable group of statements. Functions accept zero or more arguments and may return a result. This very broad definition captures what the language allows.

More strictly speaking, a function is a subroutine that returns a result. Still, Python is like most other languages, in that it doesn't distinguish between "subroutines" (or procedures), which don't return a result, and functions, which do return a result. They are defined the same in Python and called in roughly the same way.

As in most programming languages, therefore, the definition of a function in Python is quite broad, and certainly a good deal broader than it is in mathematics, where a function maps a value to a result in a deterministic way.

In addition to functions as defined here, Python also supports unnamed, anonymous lambda functions and callable objects that can serve as functions but are defined differently. There are also different types of methods that one can define on Python clases. (See [Python Classes Zero To Expert: A Tutorial With Exercises](https://codesolid.com/getting-started-with-python-classes/), for more on this topic). For the purposes of this article, however, we'll focus primarily on simple functions declared outside of a class.

### Python Functions: Some Examples

You define a function in Python with the following syntax:

```python
def function_name(parameter_1, ..., parameter_n):
    statement_1
    ...
    statement_N
    optional return value
```

The items you pass to a function are called parameters when they appear in the function's definition. They are called arguments when passed as part of a call to a function. To call a function, you type the function name followed by the arguments you want to pass to the function in parentheses. You already know how to do this:

```python
# Calling a function

print("Hello world")
```

Multiple parameters, if any, are separated by commas.

The print function is a good example of the "looseness" of the definition of a function because it doesn't return a result. We call print for to get the "side effect" of displaying a result on the screen.

Let's look at some simple examples of function definitions and how we might call them. We first define a function like print that we call for its side effects, and then we define another that fits a stricter, mathematical idea of what a function does.

```python
def log_info(message):
    """A function with one parameter called for side effects only.  No return value."""
    print(f"INFO: {message}")
    
def add(n1, n2):
    """A function with two parameters and a return value"""
    return n1 + n2

log_info("A function with side effects")

# Save a return value to a variable:
result = add(2,2)
log_info("2 plus 2 equals " + str(result))

# What about the side-effects only function. What does it "return"?
log_result = log_info("What if a function returns no result?")
log_info(f"log_result is None? {log_result is None}")
```

Output:

INFO: A function with side effects
INFO: Two plus two equals 4
INFO: What if a function returns no result?
INFO: log\_result is None? True

### Keyword Arguments and Positional Arguments

Python has a very rich and flexible syntax for passing arguments to a function. In fact, it's so rich and flexible that we've published a whole separate article on [Python Function Arguments](https://codesolid.com/python-function-arguments-and-parameters-examples/) that goes over all the rules and special cases.

To briefly summarize some of the main points without getting into all the detailed syntax and special cases, if you have a plain function with a set of parameters, you can in general specify those parameters either by keyword or by position.

Let's suppose for example that you're tired of looking up string formatting codes for displaying different numbers in base 2, base 16, and so forth. You decide to write a function that takes a decimal number and a string representing a base you want to display it as, and returns a string. The bases you want to be able to pass to it are "hex" for hexadecimal, "bin" for binary, "oct" for octal, and "dec" for decimal.

```python
def int_to_string(number: int, target_base: str) -> str: 
    """Format an integer as a string, in one of the bases given by the keys in supported"""
    supported = {"hex": "{0:0x}", "bin": "{:0b}", "dec": "{0:0d}", "oct": "{0:0o}"}
    assert target_base in supported.keys()
    return supported[target_base].format(number)
```

The implementation details are unimportant for now. The main point is that, given a simple Python function like this, we can pass a number in the first position, and a string in the second position:

```python
# Call a function using positional arguments
result = int_to_string(10, "hex")
print(result)
```

Output:

```bash
a
```

Being able to call a function by position like this is common to many, many programming languages. In Python, we can alternatively call the function by keyword, specifying the name of the parameter, an equals sign and a value. If we do this we can pass the arguments out of order if we like:

```python
# Call a function using keyword arguments
result = int_to_string(target_base="bin", number=10)
print(result)
```

Output:

```bash
1010
```

You can also mix positional arguments and keyword arguments, but the rule for that is that if you do so, any positional arguments must come first. This is as you might expect, since in that case, order matters!

### Default Parameters

Later parameters in a function parameter list can be created as default parameters. For example, maybe we designed `int_to_string` to be flexible, but since we deal with hexadecimal values a lot, we really wanted to make that a default. To do this, place the default value in an equals sign after the parameter definition, for example:

`def int_to_string(number: int, target_base: str**="hex"**)` ...

With this change in place, we can still override the default to get octal or other formats, but if we leave off the parameter, we get hex:

```python
# Call a function using a default parameter
result = int_to_string(255)
print(result)
```

Output:

```bash
ff
```

### Return Values

As we saw above in `int_to_string`, values can be returned from a function using the "return" keyword, followed by a variable or expression. The return value can then be set to a variable or used in another expression. Function calls can also be nested, with the innermost call's return value passed to the next innermost, and so forth. In practice, you should avoid having too much nesting because after awhile the code starts to become unclear, but the choice of when an intermediate variable improves readability is somewhat arbitrary. Here's an example where we nest the return of `str` to the `len` function, and print that value.

```python
print(len(str(12345))) # Prints 5
```

Output:

```bash
5
```

If the nesting begins to get confusing, you can clarify the explicit steps by creating variables if you wish.

```python
number_as_string = str(12345)
length = len(number_as_string)
print(length)
```

When to keep things concise and when to make them explicit is often a judgment call, but usually, if there's any complexity in the code that would make it difficult to understand otherwise, splitting it out into separate steps is a good idea. When in doubt, err on the side of clarity. The goal always should be to make the code readable, not clever.

### Early Returns from a Function

A function can have more than one return statement. There's some debate as to whether that's a good idea or not, but many developers feel it makes sense if you already know the answer. Let's suppose you have a function that takes a list of sales objects and counts those with a total value greater than $100.00. If the list is either null or empty, it makes no sense to continue, since the answer has to be zero. In that case, an early return at the top of the function might make perfect sense:

```python
def count_sales_over_one_hundred(sales):
    """Assert example"""
    if not sales:
        return 0
    # Do count otherwise...
```

We'll show another way we could have handled this condition a bit later in our discussion of asserts.

### Multiple Return Values from a Python Function

You can easily return multiple values from a Python function by separating them with a comma. Strictly speaking, you're really returning one Python tuple this way, and the comma serves as an operator that creates the tuple.

Let's say you wanted to modify your `count_sales_over_one_hundered` function to return both the total count of sales over one hundred dollars, as well as the count of sales under ten dollars. Once you've gone through the list, your return statement might look like this:

`return count_high_dollar, count_low_dollar`

### Functions with No Return Value

When your program calls a function in Python, generally speaking, one of three things will happen:

- The function will return a value to the caller. If it returns a value, that value should (generally) be handled by the caller in some way.

- The function will not return a value with an explicit return call, and will simply run through the last line of code in the function, then return None (implicitly) to the caller.

- The function will throw an exception. The caller may handle the exception, for example by logging or otherwise reporting the error. If the exception is unhandled or re-raised by the caller, the program will exit.

## You May Also Enjoy

[Python Format Strings: From Beginner to Expert](https://codesolid.com/python-format-strings/)  
  
[Python Dataclass: Easily Automate Class Best Practices](https://codesolid.com/python-dataclasses/)

[Python Indexing and Slicing](https://codesolid.com/python-indexing-slicing-exercises/)

[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)
