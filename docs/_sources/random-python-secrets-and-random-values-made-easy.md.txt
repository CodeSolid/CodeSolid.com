---
title: "Random Python:  Secrets and Random Values Made Easy"
date: "2022-06-08"
categories: 
  - "python"
coverImage: "random.jpg"
---
# Random Python:  Secrets and Random Values Made Easy
## Introduction

The ability to generate random values is an important programming skill. Even if you don't need them every day, random values still show up in a surprising number of places. Of course, for many people, the first thing that comes to mind when they think about random values are game-related use cases such as shuffling cards, dice rolls, and slot machines.

Random values have many other uses, however. These include:

- Generating secure passwords or password-reset URLs.
- Creating sample data for use in test cases or code demonstrations.
- Sanitizing Personally Identifiable Information (PII) data to prepare the data for analysis.

As with so many other essential programming tasks, the Python programming language has well-designed, consistent support for generating random values as part of the Python standard library. Some of the relevant modules include the random module, the secrets module, and the uuid module. The secrets module provides cryptographically strong random numbers, while the random module provides less secure numbers that you can use for games, test data, simulation, and the like. The following section goes into the differences between the two types of random values.

## Random vs. Pseudo-Random Values

The main difference between "true" random numbers and pseudo-random numbers pseudo-random number generators use an algorithm to generate a sequence of numbers that appear to be random but are deterministic. In fact, they're so deterministic that given the same seed value (or starting value), they will generate the same series of numbers reliably! On the other hand, random number generators rely on physical processes to create numbers that are genuinely random.

While pseudo-random number generators are good for many purposes, they are not suitable for applications where true randomness is required, such as cryptography. This is because it is possible for someone who knows the algorithm to predict the next number in the sequence. For this reason, true random number generators are essential for security-critical applications.

## Random and Secrets: More Alike Than They Seem!

Already we've discussed in the last section, the random module is fine if we're coding a game or simulating data. However, we want the secrets module if we're dealing with authorization tokens or other secure data.

### The Random Module

There are other differences between the two modules as well. The random module is the older of the two and has been around since Python version 1. It has a large functional interface that is essentially a wrapper around a shared instance of a class, `random.Random`. However, you could always construct a Random class of your own and use that. The `random.Random` class could be instantiated with a known seed to give a reproducible sequence of random numbers. If missing, a seed value based on the system timer would be used.

This example shows the impact of selecting a seed on the `random.Random` class:

```python
"""Creating random integers demo"""
from random import Random, randint

seed = 42
seeded_1 = Random(seed)
seeded_2 = Random(seed)
randomly_seeded = Random()

# Get a random number between 1 and 1000, inclusive
print(seeded_1.randint(1, 1000))
print(seeded_2.randint(1, 1000))
print(randomly_seeded.randint(1, 1000))

# Use the functional interface
print(randint(1,1000))
```

```
655
655
161
956
```

Two instances of the Random class, instantiated with the same seed, generated the first two lines of input. These lines print 655 every time you run the program. (Try it!).

The last two lines were created using a randomly seeded instance and the functional interface (also randomly seeded). These lines vary with every run, and any runs where the numbers line up in the case of these two lines are purely coincidental.

### The Secrets Module

At first glance, the secrets module, first described in [PEP 506](https://peps.python.org/pep-0506/) and first appeared in Python 3.6, looks pretty different from the Python random module. Many of the functional interface wrappers are gone, so, for example, you can't import `randint` directly. Moreover, the `secrets.SystemRandom` class will ignore any seed values you may pass to it.

However, if we scratch beneath these surface differences, the two classes are quite similar, and indeed, looking at the source code:

- The `secrets.SystemRandom` class is actually an alias for the `random.SystemRandom` class.
- The `random.SystemRandom` class is a subclass of `random.Random`. Because of this, generally speaking, functions available in one are also available in the other. (Two exceptions are `getstate` and `setstate`, which are not implemented in `SystemRandom`).  
      
    The most significant difference internally is that the core "randomization" behavior in SystemRandom is implemented in terms of `os.urandom`. The `urandom` function, in turn, is passed an integer and returns that many random bytes using a platform-dependent, cryptographically strong random value generator.

We now know we can use either class, largely interchangeable, but `secrets.SystemRandom` will be more genuinely random and therefore of use in more secure contexts.

With this in mind, let's take a look at some use cases next.

## Generating Random Numbers

### Randint and Randrange

We've already seen how to generate random numbers in a specific range using `randint`. The `randrange` function is very similar, except that it excludes the upper bound, whereas the upper bound of `randint` is inclusive. If you run this code often enough, a five will turn up for the first output line, but not for the second.

```python
from secrets import SystemRandom
rand = SystemRandom()

# Integers betewen 1 and 5, inclusive
print(rand.randint(1,5))   

# Integers between 1 and 5, but not including 5
print(rand.randrange(1,5))
```

### Generating Random Distributions

There are several methods shared by Random and SystemRandom, that allow you to generate random values according to various distributions. These include uniform distributions (to get floating-point values between two endpoints, similar to what `randint` provides), Gaussian (normal) distributions, and others.

For example, we can create a list of 20 imaginary IQ values, randomly distributed along the same normal curve as a real population. By definition, IQ has a mean value of 100 and a standard deviation of 15. (By the way, for purposes of this example, we want to model this sort of distribution, even as we ignore the legitimate criticisms that have been raised about both the idea and how we test for it.)

Here is the code o create a "population" of 20 IQs at random:

```python
"""IQ distribution"""
from secrets import SystemRandom
rand = SystemRandom()
population = [round(rand.gauss(100, 15)) for _ in range(0,20)]
print(population)
```

The output will vary, of course. Here's one representative run:

```bash
[102, 90, 88, 82, 102, 93, 127, 121, 94, 107, 103, 80, 106, 106, 84, 107, 108, 88, 123, 121]
```

## Making Random Choices in Python

Choosing from a list or other sequence is often a two-step process in other languages. First, you get a random number in the range from zero to the upper bound of the list (length minus one). Then you apply that index to the list to select an element. In Python, two methods, `choice` and `choices`, give you the ability to do both of these steps at once. This makes it extremely easy to select a random sample of the desired size from any kind of sequence

For example, given the code above, let's say we wanted to take our population of IQs and select one or more values from it. Here's how we could do it quickly:

```python
# Select one IQ at random
print(rand.choice(population))

# Select four IQs at random
print(rand.choices(population, k=4))
```

Output (example):

102
\[107, 102, 88, 103\]

## How to Generate Random Strings With Python

Because it's so easy to select random choices from a sequence in Python using the methods `Random.choice` or `Random.choices`Creating random strings in Python is also straightforward. In addition, the secrets module defines some specialized functions that can also be used, depending on your needs.

Let's first look at a general approach that you can use to generate many kinds of strings. The string module includes several strings that are essentially hard-coded sequences of characters, e.g. `ascii_lowercase` (a-z), `ascii_uppercase` (A-Z), `ascii_letters`, `punctuation`, and `digits`. `Random.choices` or `SystemRandom.choices` can be called on any of these to create an array of the desired length, then the str class's join method can be used to convert the array to a new string.  
  
We combine those steps in the following example:

```python
from string import ascii_letters, digits, punctuation, ascii_lowercase, ascii_uppercase
from secrets import SystemRandom
rand = SystemRandom()

four_digits = "".join(rand.choices(digits, k=4))
ten_mixed_case = "".join(rand.choices(ascii_letters, k=10))
assorted = ascii_letters + punctuation
twenty_assorted = "".join(rand.choices(assorted, k=20))

print(four_digits)
print(ten_mixed_case)
print(twenty_assorted)
```

Example output:

```bash
8782
PLZYOxFLoQ
!mNsKsF;([I#F(c<JcG}
```

## Secure Random Strings Using the Secrets Module

In addition to easily creating random strings as shown above, the secrets module provides several functions that can be used to generate random sequences of bytes in various formats. At the lowest level, we can generate raw "bytes" arrays of various lengths using the `token_bytes` function

```python
from secrets import token_bytes
b = token_bytes(10)
print(type(b))
print(b)
```

Sample output:

```bash
<class 'bytes'>
b'!\x05P\xc6a\x87\xf9~(\xa9'
```

Raw bytes might be useful as input to cryptographic algorithms or the like, but remember that they won't contain valid UTF-8 codepoints, so this function shouldn't be used for generating strings. To get strings, one can use either the techniques from the last section or one of the next two functions.

Rather than get the bytes in raw format, we can return a string, consisting again of random bytes, but in hexadecimal format. This gives us two characters of hexadecimal output per byte:

```python
from secrets import token_hex
token = token_hex(10)
print(f"Returned a {type(token)} of length: {len(token)}:")
print(token)
```

Sample Output:

```bash
Returned a <class 'str'> of length: 20:
529af33afcc8acab096a
```

A third function in the same family -- in some respects perhaps the most useful, is `token_urlsafe`. This function allows us to get a string of random bytes into a slightly modified base64 encoded string. Here each byte results in an average of 1.3 characters, and the result can be safely used as a URL -- for example, to represent a shortened URL or to be used as a password reset token. An additional benefit is a string that comes from a much larger set of potentially random characters than the 16 digits of `token_hex`.

```python
from secrets import token_urlsafe
token = token_urlsafe(15)
print(token)
```

Sample output:

gfN2nGjO7izMPyXs5tvU

## Using UUIDs: Generating Values that are Random And Unique in Python

Although our focus in this article has been on random values, we'd like to spend some time now discussing values that are both random and unique for all practical purposes. One extremely widespread approach to this problem is the idea of a Universally Unique Identifier, or "UUID". A UUID is a 128-bit number that is not 100% guaranteed to be unique but is so statistically likely to be unique that the chances of a collision are vanishingly small.

In addition to being large numbers, UUIDs share a common representation format. A 128-bit number can be represented as 32 hexadecimal digits, while a UUID adds four hyphens to make a 36-character string arranged in a pattern of 8-4-4-4-12. For example:

```
'967909e3-7231-4040-aae4-8b6b2fb96a0b'
```

The Python module, uuid, has several different functions which correspond to the many recognized algorithms, for creating such identifiers, but the recommendation is to use one of the two most common types, uuid1 and uuid4.

uuid1 values are created by combining a network node id (which typically means a mac address of your network card), with a few bits of information about the UUID version and variant, and many bits representing a high-resolution timestamp.

uuid4 values, in contrast, generally contain six bits devoted to storing information about the version and variant, and 122 bits of purely random data. So even though in principle there could be collisions of two uuid4 values, in practice, according to [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_(random)), "the probability to find a duplicate within 103 trillion version-4 UUIDs is one in a billion."

You can create uuid1 and uuid4 values easily with the Python uuid module. As we'll see, the string representation looks the same, even though it is more meaningful to describe the bits in a uuid1 field.

```python
from uuid import uuid1, uuid4

print(uuid1())
print(uuid4())
```

Sample output:

bfc89f3e-e6ab-11ec-abfc-4a9b744d17b8
025586c2-50ed-41a6-ae31-bf96b9d79df2

As with most things in this article, when we say "Sample output", we really mean it. Of course, in the case of uuid4 at least, if you run this code 103 trillion times, you have a one in one billion chance of getting the same result as I did.

You'll forgive me if I don't wait, right?

Before leaving our discussion of UUIDs, we mention them here because they are a widely accepted standard, but as we've seen, there's quite a lot of overlap between the implementation of uuid4 and many of the utility functions in the system module. For example, I have often seen the `uuid4` function used to generate keys in a database, especially in NoSQL contexts where something like auto-increment fields may not be supported. In principle, one could also use `secrets.token_hex` for the same task, but uuid4 may make the intent of the code somewhat more clear.

## Closing Thoughts

I hope you've enjoyed our tour through the Python random modules. Remember that we've dealt here with what's available in the core Python standard library. In the data science world, we should also make a quick nod to NumPy's module, `numpy.random`, which provides the ability to generate samples according to many different distributions. There's some overlap in terms of functionality with the distribution methods in the core library we discussed above, but in the NumPy case, you can more efficiently generate large arrays of sample data.

Oh, and one final thing -- if you're curious about the featured image for this post, here's the code I used to create it (in Jupyter Lab):

```python
import random
import matplotlib.pyplot as plt

x = [random.randint(1, 100) for n in range(100)]
y = [random.randint(1, 100) for n in range(100)]
plt.figure(figsize=(8,6), dpi=80)
plt.scatter(x, y)
plt.show()
```

## You May Also Enjoy

- [Python Format Strings: Beginner to Expert](https://codesolid.com/python-format-strings/)
