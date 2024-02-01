---
title: "How To Compare Python Dictionaries"
date: "2022-01-31"
categories: 
  - "python"
coverImage: "comparison_smaller.jpeg"
---

The easiest way to compare Python dictionaries is simply to use the same equality operator you use on other Python types, "==". This works great for most cases, but it relies on the behavior of "==" for the values involved. If you need a more strict test, this can be done in a few lines of code.

## Python Is Consistent

Two of the benefits of Python are its ease of use and consistency. It's different from Java, for example, where string comparisons compare object references, and you have to use the "equals" method to do the string comparison you want to do. In Python, in contrast, you can largely rely on `==` to do the right thing most of the time.

Consider the following code:

```python
string = "Hello"
same_string = "Hello"
number = 3
same_number = 3
boolean = True
same_boolean = True

print(string == same_string)
print(number == same_number)
print(boolean == same_boolean)
```

Output:

```bash
True
True
True
```

Of course, this also works for negative cases, as you'd expect: `"pig" == "canary"` returns `False`.

## Compare Dictionaries Like Other Types

Python is not just consistent for simple types, it also implements reasonable equality checks for more complex types as well. Let's see this for dictionaries:

```
dictionary = {"favorite_website": "https://codesolid.com", "attempts": 1}
same_dictionary = dictionary.copy()

# Comparing simply a matter of using ==, same with other Python types
print(dictionary == same_dictionary)
```

Output:

```bash
True
```

Since what's being checked is perhaps a bit less obvious than it is for simple types, let's try changing different elements.

```python
dictionary = {"favorite_website": "https://codesolid.com", "attempts": 1}

# Add a key
key_added = dictionary.copy()
key_added["new"] = "New Value"
print(dictionary == key_added)

# Remove a key
key_removed = dictionary.copy()
del(key_removed["attempts"])
print(dictionary == key_removed)

# Change a value
value_changed = dictionary.copy()
value_changed["attempts"] = 2
print(dictionary == value_changed)

# Change type of a value from int to float
type_changed = dictionary.copy()
assert(type_changed["attempts"] == 1)
type_changed["attempts"] = 1.0
print(dictionary == type_changed)
```

Output:

```bash
False
False
False
True
```

The first three cases are pretty much what we'd expect. The last one needs some explaining.

## Use Caution With Equality-Compatible Types

What's happening in the last case is that we're comparing a `1` (an integer) with `1.0` (a floating point value). Behind the scenes, the integer value converts to a float, the two floats are compared, and the comparison returns true. This has nothing to do with dictionaries _per se_ -- it's just a property of the values being compared. In the same way:

```python
print(1 == 1.0)
```

Output

```bash
True
```

## What If We Need a Stronger Check for Equality?

If we need to check that the dictionaries are equal **and** that the types of all the values are equal, that's relatively straightforward in Python. Here's one version of a method that will work:

```python
import typing
def type_aware_equals(d1: typing.Dict, d2: typing.Dict) -> bool:
    """Compares dictionaries with strong check on equality of values"""
    
    # Return early if standard equality fails
    if d1 != d2:
        return False

    # Compare types
    values = zip(d1.values(), d2.values())
    for value in values:
        if type(value[0]) != type(value[1]):
            return False
    
    return True
```

To test this, we can run our original cases again, using the function instead of `==` this time. We'll also do one more check for dictionaries we know to be equal to make sure that case works.

```
print(type_aware_equals(dictionary, key_added))
print(type_aware_equals(dictionary, key_removed))
print(type_aware_equals(dictionary, value_changed))
print(type_aware_equals(dictionary, type_changed))

# Make sure equal dictionaries are reported correctly
same_dictionary = dictionary.copy()
print(type_aware_equals(dictionary, same_dictionary))
```

Output:

```bash
False
False
False
False
True
```

## Using "==" for Other Python Collections

As we saw, Python's treatment of equality for dictionaries is consistent with its treatment of equality for simple types like numbers and strings.

This consistency also extends to other built-in composed types and collections, as well as collections defined in Python standard library modules. For example, here we demonstrate that it works for lists, sets, tuples, and arrays:

```python
from array import array

favorite_foods = ["Chilli", "Fish and Chips", "Potatoes"]
list_copied = favorite_foods.copy()
print(favorite_foods == list_copied)

foods_as_set = set(favorite_foods)
second_set = foods_as_set.copy()
print(foods_as_set == second_set)

tuple1 = ("Parrot", "is", "late")
tuple2 = ("Parrot", "is", "late")
print(tuple1 == tuple2)

# An array of integers, and a copy
array1 = array('i', [1,2,3])
array_copy = array('i', [1,2,3])
print(array1 == array_copy)
```

The output is as we expect:

```bash
True
True
True
True
```

## What About User-Defined Types?

This topic is a bit more advanced than what we've been discussing, but I wanted to include it for readers who may be asking themselves, "How is such consistency achieved? Can I implement it too?"  
The answer is, "Yes, you can."

Although you may not need it for simple cases,it's also possible to define methods on user-defined classes that will allow consumers of your class to use the standard comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`, etc.). This is not done directly via operator overloading, as it is in C++. Instead, Python allows this via special methods like `__eq__`, `__ge__`, `__lt__`, etc. These are called "magic methods" or sometimes "dunder" methods (dunder comes from the "double underscore" at the beginning and end of each method).

Such magic methods are ubiquitous in Python, and form an important part of what the book, Fluent Python, calls "the Python data model". In the case of what we're discussing now, the various comparison operators, Python's `functools` module contains a useful shortcut to save you from having to implement each one of these methods individually. It's possible to only have to define two such methods and have the rest implemented automatically, using the [@functools.total\_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering) decorator. The Python documentation for that decorator contains a useful example you can use as a starting point for your own classes.
