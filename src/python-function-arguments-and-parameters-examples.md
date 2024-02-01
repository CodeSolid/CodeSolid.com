---
title: "Python Function Arguments: The Complete Guide"
date: "2021-12-27"
categories: 
  - "python-functions"
---
# Python Function Arguments: The Complete Guide
## Introduction

Python functions have a relatively simple syntax that is very beginner-friendly. If you're at the start of your Python journey, you'll want to focus your practice on the basic syntax for defining and calling functions. However, as you go deeper into the language, you'll learn that compared to other programming languages, Python has a very rich and flexible syntax for how to define functions.

The great news about this flexibility is that -- if used properly -- it supports functions that are both easy to use from the caller's point of view and maintainable (changeable) over time without breaking existing code. The downside of all this flexibility, of course, is that it can take a little work to master the many options that are available. This is especially true now since Python 3 has added many great enhancements, such as keyword-only arguments (Python 3.0) and positional-only arguments (Python 3.8).

The goal of this article is to start with the simplest information about Python function arguments and some basic background on Python functions that we hope beginners will find useful. Following this, we gradually introduce many, many examples of the Python function calling convention. We will introduce many Python examples of Python parameters and arguments that show how to use both basic and advanced features.

Note that for an even more gentle introduction to functions, however, you might also consult [The Function in Python: Complete Tutorial and Best Practices](https://codesolid.com/the-function-in-python-complete-tutorial-and-best-practices/).



## Function Parameters and Arguments for Beginners

If you're a beginner and are unfamiliar with Python functions, this section is for you. Note that this isn't a complete beginner discussion of Python functions, because we want to focus for now on parameters and arguments.

What's the difference? Well, although the terms "argument" and "parameter" are sometimes used interchangeably -- and I'm as guilty of this as anyone. However, strictly speaking, a function is designed to take zero or more _parameters_, which the caller then passes as _arguments_.

In other words: parameters appear in function definitions, while arguments are what you pass when you call the function.

Parameters have names, but the name the caller uses to call the function can be different, or -- if you're calling the function with a literal value -- you may not have a name on the caller side at all.

To make this more concrete, let's take a very simple example.

```python
# Define a function with one parameter, with the name "name"
def greet(name):
    print(f"Hello, {name}.")

# Pass a literal as an argument
greet("World")

# Call the function with one argument using a different name
my_name = "John"
greet(my_name)
```

Output:

```bash
Hello, World.
Hello, John.
```

## Using Keyword Arguments Instead of Positional Arguments

A function with positional parameters can also be called either by position or by using keyword arguments. In this case, nothing more is needed when defining the function.

```python
def greet(message, name, punctuation):
    '''simple demo of "plain" function parameters'''
    print(f"{message}, {name}{punctuation}")

# We can call it via plain positional arguments
greet("Hello", "World", ".")

# We can call it in order or out of order using keyword arguments
greet(name="John", message="Nice example for out of order calling", punctuation="!")

# We can mix positional arguments and keyword, but positional must come first:
greet("Hello", punctuation="!", name="programmer")
```

Output:

```bash
Hello, World.
Nice example for out of order calling, John!
Hello, programmer!
```

## Type Hints

Python introduced type hints in Python 3.5, and their use is encouraged. Type hints are a way to document the type of a function's parameters, and some third party tools may use this information to display an error if the function is called with an argument of the incorrect type. Note that the Python runtime does not enforce type checking for type hints.

We're not dealing with type hints in detail here, and we don't use them in the examples shown here only to make the code as simple as possible. But for non-tutorial code, they really are a best practice that we recommend.

For now, we content ourselves with a simple definition and example may suffice.

Type hints follow the syntax:

```
argument_name:type_name
```

For example, rewriting our greet function with named arguments, it looks like this.

```python
def greet(message: str, name: str, punctuation: str):
    '''simple demo of "typed" parameters'''
    print(f"{message}, {name}{punctuation}")
    
# The call (and output) look the same:
greet("Hello", "world", "!")
```

## Default Parameters

The Python documentation lists default parameters as one of the most common, useful use cases for Python functions.

Default parameters are added by simply using an equals sign after the argument name. Note that, unlike assignment expressions, PEP8 recommends no space before and after the equals sign, so use:

```
argname=default
```

not

```
argname = default
```

Our `greet` example is a simple case where a default argument would have improved the function. Since we usually want to greet folks enthusiastically, let's add an exclamation point default.

```python
def greet(message, name, punctuation="!"):
    '''simple demo of a function with a single default parameter'''
    print(f"{message}, {name}{punctuation}")


# You can use the default, or override it.

# Use the default for someone you like
greet("Hello", "best friend")

# Override the default for your nemesis
greet("Oh, hi", "lame person", "...")
```

Output:

```bash
Hello, best friend!
Oh, hi, lame person...
```

## Default Parameters Are Only Evaluated Once

A subtle but important point about default parameters is that they are evaluated only once, not every time the function is called. So for mutable values like lists, dictionaries, etc., this may cause unexpected results. Let's take as an example a function that tries to append an item to a list (The function below is not one you should really write since it doesn't do add anything to a list's "append" method, but it's useful as an illustration):

```python
def append_one_item_to_list(item, item_list=[]):
    '''try to add an item to the list and create the list if it does not exist'''
    item_list.append(item)
    return item_list

list_one_number = append_one_item_to_list(42)
print(list_one_number)

dog_list = append_one_item_to_list('Golden Retriever')
print(dog_list)
```

Output:

```
[42]
[42, 'Golden Retriever']
```

## Using None as a Default Argument for Mutable Values

To solve the problem we of default arguments only being evaluated once, use None to represent the mutable value, and write your fuction this way:

```python
def append_one_item_to_list(item, item_list=None):    
    '''add an item to the list and create the list if it does not exist'''
    if not item_list:
        item_list = []
    item_list.append(item)
    return item_list

list_one_number = append_one_item_to_list(42)
print(list_one_number)

dog_list = append_one_item_to_list('Golden Retriever')
print(dog_list)

# We can still add items to a list that's already created, 
# of course.  Here the fact that we're just wrapping list.append becomes really obvious.

stooges = ['Moe', 'Larry']
more_stooges = append_one_item_to_list('Curly', stooges)

print(more_stooges)
```

Output:

```
[42]
['Golden Retriever']
['Moe', 'Larry', 'Curly']
```

## **Variable Parameters in Python: \*args and \*\*kwargs**

Whether passed by position, by keyword, or a mixture of both, so far we've looked at functions that support a fairly fixed number of arguments. That is to say, any parameters without a default must be supplied. If you don't supply an argument for a non-default parameter, it's an error. Let's see our greet function again and see what happens.

```python
# CAUTION:  This code generates an error!
def greet(message, name, punctuation="!"):
    """simple demo of a function with a single default parameter"""
    print(f"{message}, {name}{punctuation}")

greet("Hi there")
```

Output:

```bash
TypeError                                 Traceback (most recent call last)
...

TypeError: greet() missing 1 required positional argument: 'name'
```

In Python, as in some other languages, it's also possible to supply a variable number of positional or keyword arguments. By convention, variable positional arguments are denoted by a parameter named \*args, and keyword arguments are specified usually by a parameter called \*\*kwargs. I say "by convention" because strictly speaking, the names don't matter as much as the asterisks at the beginning of the name, but the convention is very firmly entrenched, so it's best to just stick with the names \*args and \*\*kwargs.

## **Variable Positional Arguments Only**

At the risk of making you hungry, let's imagine you wanted a function to print all your favorite things to eat, one food per line. However, because your appetite changes from day to day, sometimes you want to print only one thing to eat, but on other days you wanted to print out a one or two things, some days you want to print out a whole list.

Let's see how we can support this with variable positional arguments:

```python
def print_foods(*args):
    """prints one or more foods passed as a single list or as one or more positional arguments"""
    for food in args:
        print(food)

print("Calling with one argument")
print_foods("Soup")

# New line
print()

print("Calling with three arguments")
print_foods("Soup", "Sandwich", "Coffee")
```

Output

```bash
Calling with one argument
Soup

Calling with three arguments
Soup
Sandwich
Coffee
```

## **Calling Variable Positional Arguments with a List**

What if you had a long list of foods or even a set (or any other iterable)? Would you have to manually copy out the arguments? Not at all. Here's how you would do it, with a fun thing that's usually called a "splat" operator in Python, which once again is an asterisk: "\*".  
  
It works pretty much the same way as the spread operator in JavaScript (...), so if you like that name better, I won't stop you. Whatever you call it, this operator turns the iterable you prefix it with into a set of arguments for the function call.

```python
# A Pythonic feast

traditional_thanksgiving_list = ["Turkey", "Gravy", "Mashed Potatoes", "etc."]

vegan_thanksgiving_tuple = ("Impossible Burger Meat Loaf", "Mushroom Gravy", "Turnips", "etc.")

# Note the * at the beginning here, the splat operator
print("TRADITIONAL:")
print_foods(*traditional_thanksgiving_list)

# New line
print()
print("VEGAN:")
print_foods(*vegan_thanksgiving_tuple)
```

Output

```bash
TRADITIONAL:
Turkey
Gravy
Mashed Potatoes
etc.

VEGAN:
Impossible Burger Meat Loaf
Mushroom Gravy
Turnips
etc.
```

## **Variable Keyword Arguments**

In Python, just as you can pass a variable number of arguments by position, you can also pass a variable number of keyword arguments. This is done with the \*\*kwargs parameter. Inside the function itself, kwargs is passed as a dictionary, as we demonstrate below.

```python
def print_main_course(**kwargs):
    """prints a main course for each keyword argument.
      
       We assume the argument name is a 'meal' 
       and the value is the 'main course'
       
       For example: print_main_course(breakfast="eggs")
    
       Internally this would be passed to the function as 
       a dictionary, equivalent to this:
       
       kwargs = {"breakfast": "eggs"}       
    """
    
    # Iterate the dictionary
    for meal, main_course in kwargs.items():
        print(f"The main course for {meal} is {main_course}")

print_main_course(breakfast="Bagel", lunch="Chili", dinner="Sandwich")
```

Output:

```
The main course for breakfast is Bagel
The main course for lunch is Chili
The main course for dinner is Sandwich
```

## **Positional Arguments Still Come First**

As you may recall from [Part One](https://codesolid.com/python-function-arguments-and-parameters-examples), positional arguments come before keyword arguments. This is true for variable keyword arguments as well. If we try to define variable keyword arguments before positional arguments, we get an error.

```python
# BAD CODE! This code generates a syntax error, proving that
# you can't give chuck_norris an argument!

def broken_function(**kwargs, chuck_norris):
    pass
```

Output:

```bash
  File "<filename>", line 4
    def broken_function(**kwargs, chuck_norris):
                                  ^
SyntaxError: invalid syntax
```

## Keyword-Only Parameters

In Python 3.0 and later, anything following any variable length positional arguments must be specified by keyword. Passing them by position does not work.

```python
def print_person_info(name, *args, codes_in_python):
    """Given a person with a name, print the person's name, the name of any of their 
       children as *args, and whether they code in python."""
    
    verb = "does" if codes_in_python else "does not"
    children = ", ".join(args)
    print(f"{name} is a parent of {children} and {verb} code in Python.")
    
# This code is fine, pass final argument by keyword
print_person_info("John", "Helen", codes_in_python=True)

# BAD CODE.  This code displays an error: 
print_person_info("John", "Helen", False)
```

Output:

```bash
John is a parent of Helen and does code in Python.

---------------------------------------------------------------------------
# Python Function Arguments: The Complete Guide...

TypeError: print_person_info() missing 1 required keyword-only argument: 'codes_in_python'
```

## **Keyword-Only Parameters Without Variable Positional Arguments**

We saw above that in Python, any parameters following a variable positional argument become keyword-only parameters. But what if we wanted to force a some parameters to be keyword-only without supporting variable positional arguments?  
  
In this case, we use a slight variation on the \*args syntax. Here, we make it clear that there are no variable arguments allowed by simply denoting the end of the positional arguments with an unnamed, bare "\*".

```python
def print_person_info(name, *, codes_in_python):
    """Print a person's name, and whether they code in python.

         codes_in_python must be passed by keyword
    """
    if codes_in_python:
        print(f"{name} codes in Python.")
    else:
        print(f"{name} is missing out on the fun.")
    
# This code is fine, pass final argument by keyword
print_person_info("John", codes_in_python=True)

# BAD CODE:  generates an error
print_person_info("John", False)
```

Output:

```bash
John codes in Python.

--------------------------------------------------------------------------
# Python Function Arguments: The Complete Guide...

TypeError: print_person_info() takes 1 positional argument but 2 were given
```

## **Positional-only Parameters**

In addition to supporting keyword-only parameters, newer versions of Python (from 3.8 onwards), support having parameters that must be specified by position. One of the stated reasons for the change (in [PEP 570](https://www.python.org/dev/peps/pep-0570/)) was that it allowed a function's authors to change the name of positional parameters without breaking existing callers. It's especially useful when a function supports a keyword argument but also accepts a positional one.  
  
Positional-only parameters are specified by introducing a forward-slash character, "/", into a function's definition. Parameters before this special character must be specified by position.  
Let's return to our simple greet function from the start of the article to see how this would work.

```python
def greet_flexible(name):
    """accepts a standard argument, positional or keyword"""
    print(f"Hello, {name}!")

# OK, call by position
greet_flexible("Moe")

# Also OK, call by keyword
greet_flexible(name="Larry")

def greet_positional(name, /):
    """accepts a standard argument, positional only!"""
    print(f"Hello, {name}!")
    
# OK, positional!
greet_positional("Curly")

# BROKEN - Try to call positional-only parameter using a keyword argument
greet_positional(name="Shemp")
```

Output:

```bash
Hello, Moe!
Hello, Larry!
Hello, Curly!

---------------------------------------------------------------------------
# Python Function Arguments: The Complete Guide...

TypeError: greet_positional() got some positional-only arguments passed as keyword arguments: 'name'
```

## We've Come Full Circle

By now, we've learned a lot about how Python specifies function parameters. When we started out, we learned that arguments could be passed by position or by keyword by default. With Python 3 and even more so since Python 3.8, we've now allowed authors to precisely lock down whether functions are called with keyword-only arguments, positional-only arguments, or some combination. Positional-only parameters, if any, come first, and keyword-only parameters come last. And what would be the fate of the parameters between the two? Those parameters can be passed either way, which was the same default, simple case we explored at the very beginning.

Naturally, our goal when authoring functions should be to make our intent as clear as possible, and make it as simple as possible both for callers to use the function correctly and for us as authors to make changes if need be in the future without breaking existing callers. The rules for Python function parameters give us everything we need to accomplish this end.

## Resources

This article is also available as a Jupyter notebook you can [download](https://github.com/JohnLockwood/100-days-of-python/blob/main/day-03/python-function-argument-examples.ipynb) or [run online](https://mybinder.org/v2/gh/JohnLockwood/100-days-of-python/main?labpath=day-03%2Fpython-function-argument-examples.ipynb).

## You May Also Enjoy

- [How to Profile Python Code](https://codesolid.com/how-do-i-profile-python-code/)

- [Python Format Strings: Beginner to Expert](https://codesolid.com/python-format-strings/)
