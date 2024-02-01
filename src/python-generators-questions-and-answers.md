---
title: "Python Generator Functions: The Complete Guide"
date: "2022-03-04"
categories: 
  - "python"
coverImage: "python-logo.png"
---
# Python Generator Functions: The Complete Guide
Many Python developers consider generators an advanced topic because they are less well known than sequence types such as lists, arrays, and strings.

Also, because the syntax for generator functions can appear strange at first, many developers don't take the time to learn about them at all. That's a shame, really, because, in some instances, generators are not just a curiosity but an essential developer tool. In addition, generators are very simple to write. Indeed, for generator expressions, if you know how to write a list comprehension, you're practically an expert already.

In this article, we answer several questions that you may have about generators. We'll talk about what generators are and what problems they solve. We will also dive into the various ways there are to create them. Because there are so many questions folks have about using generators, we wrote the article in a question and answer format, so feel free to skip ahead to your top concerns. (However, reading it straight through also makes it a good introduction to Python generators).

## What are Python Generators?

When people think of a generator in Python, they often think of a function that behaves like a sequence type -- something you can iterate through. Unlike common sequence types like lists, however, generators only return each value as you ask for it, where a list stores everything you've put in it in memory.

More precisely, a generator is a Python object. It is an expression, function, or class that -- strictly speaking -- can return an iterator. An iterator, in turn, is with which you can write a loop. Common ways to consume an iterator are a for-loop and a list comprehension.

We use iterators all the time in Python, even though we may not know we are doing so. Sequence types like lists, strings, tuples, and range objects have a magic method, "\_\_iter\_\_," which returns an iterator. Generator objects also have this magic method. However, as with most magic methods, you rarely need to implement them directly.

In a later section, we'll get into the precise details of what iterators are and how they work. But just as you don't need to write the magic methods, you rarely need to work directly with an iterator. Instead, you write a for loop or a list comprehension, and Python will handle the iterator for you.

## What are Python Generators Used For?

Python generators are used in cases where you need to be able to consume some data in a loop, but the size of the data set is potentially large enough to crash your program if you load it into memory. Generators allow the set of things to be iterated to be unbounded.

Data sets like a year's worth of access log entries from a high traffic website or the luminosity of stars visible through a light telescope are good candidates for a generator.

## Are Generators Faster Than Lists in Python?

In general, generators are not faster than normal functions because they perform their operations on each iteration. Generators can sometimes _appear_ to be faster than lists, but this performance depends partly on factors like a CPU cache.

The reason for this qualified answer is that in our tests, we found at first that generators were faster even when the generator had to perform some task for each iteration. In that case, we expected the list could be faster because the result would already be calculated and stored.

As we ran the tests several times, what became clear was that we were running into cases where the result of the first run was being cached in the generator case. Once we accounted for this, we compared first-run performance, and at that point, it became clear that the lists were faster.

Here, for example, is a straightforward case of returning a number based on a range object (note that the %time function is available in NumPy and Jupyter notebooks):

```python
num_list = [x for x in range(0,10000000)]
num_generator = (x for x in range(0,10000000))

print("List time:")
%time _ = [x for x in num_list]

print("\nGenerator time:")
%time _ = [x for x in num_generator]
```

Output:

```bash
List time:
CPU times: user 90.7 ms, sys: 27.3 ms, total: 118 ms
Wall time: 119 ms

Generator time:
CPU times: user 330 ms, sys: 84.4 ms, total: 414 ms
Wall time: 437 ms
```

Running the test using %timeit gives a very different result. Still, we frequently ran into messages suggesting that the result was being cached (because the first run performance was an order of magnitude for subsequent runs).

As we increased the complexity of the task from just returning a number to something like creating a string of random letters, the difference in the time for first-run performance became even more striking.

```python
import random
import string
def rand_string(count=1000):
    letters = string.ascii_lowercase
    return ''.join(random.choice(string.ascii_lowercase) for i in range(count))

str_list = [rand_string() for _ in range(0,1000)]
str_generator = (rand_string() for _ in range(0,1000))

print("List time:")
%time y = [x for x in str_list]

print("\nGenerator time:")
%time y = [x for x in str_generator]
```

Output:

```
List time:
CPU times: user 39 µs, sys: 2 µs, total: 41 µs
Wall time: 40.8 µs

Generator time:
CPU times: user 301 ms, sys: 3.56 ms, total: 305 ms
Wall time: 305 ms
```

## How Do I Write a Python Generator?

Python generators come in a few different forms. In the following sections, we discuss generator functions, generator expressions, and classes as generators. We'll also discuss a problem that trips up many Python developers who are beginning to work with generators.

## What Is a Generator Function?

A generator function is relatively simple to write because it looks just like a normal python function with a `yield` statement instead of a return value. Yield is a Python keyword that lets a program call a function repeatedly while maintaining the function's internal state.

Let's take a simple illustration to show how this works. We'll implement a function that works somewhat like a Python range object. To keep the example simple, however, we'll only allow positive step values:

```python
# Define a generator function:

def counter(start=0, end=10, step=1):
    """A simplified range-like function for positive numbers only"""
    assert step > 0 and end >= start
    i = start
    while i < end:
        yield i
        i = i + step  

# Use the generator function

print("For loop demo")
for i in counter(1,4):
    print(i)

print("List comprehension demo")
print([x for x in counter(1,4)])
```

Output:

```bash
For loop demo
1
2
3
List comprehension demo
[1, 2, 3]
```

As we've seen, creating a generator function is not difficult in itself. Simply yield a value from the function and call it from inside a for loop or comprehension, and Python will do the right thing.

If you're satisfied that you understand generators enough to write them, you might practice the technique by modifying the function above, so it does the right thing in the presence of negative step values.

However, one issue we've glossed over is _how_ Python "knows" when to stop calling the generator that we've created. If you're curious about that, the next section is for you!

## How do Python Generators Work?

Writing a generator is one thing -- they're relatively simple. But how do Python generators work under the hood?

Generators work by exposing a method, `__iter__()`, that Python can call from the context of a loop or comprehension expression. Calling next on the value returned from `__iter__()` will either return the next value that the function yields or raise a `StopIteration` exception.

We can show how this works using the counter generator we created in the last section.

```python
# Get a generaor and return its iterator
my_generator = counter(1,4)
iterator = my_generator.__iter__()

# Call next on the iterator until we get a StopIteration exception
while(True):
    try:
        value = next(iterator)  # Same as iterator.__next__()
        print(value)
    except StopIteration:
        print("No more elements")
        break
```

Output:

```bash
1
2
3
No more elements
```

## What Is a Generator Expression?

A generator expression is a more concise way to write a generator than a function with a yield statement. The syntax of a generator expression is the same as that for a list comprehension, except that instead of square brackets, we enclose a generator expression in parentheses.

Like generator functions, generator expressions are only iterated when they are consumed. We can demonstrate this by comparing the results of a generator expression and a list comprehension:

```python
demo_list = [i for i in range(1, 6, 1)]
print("Demo list: ", demo_list)

demo_generator = (i for i in range(1, 6, 1))
print("Demo generator: ", demo_generator)

# Now we consume the generator
for x in demo_generator:
    print(x)
```

Output:

```bash
Demo list:  [1, 2, 3, 4, 5]
Demo generator:  <generator object <genexpr> at 0x107ef2500>
1
2
3
4
5
```

As with all generators, before we consume it, the generator is just an object, the results aren't stored anywhere. We use a for loop to iterate through it.

As with list comprehensions, generator expressions also support not just iterating but also filtering results. For example:

```python
words = "Is there any place in this town where we could find a shrubbery".split(" ")
gen = (word for word in words if len(word) > 4)
print(type(gen))
for word in gen:
    print(word)
```

Output:

```bash
<class 'generator'>
there
place
where
could
shrubbery
```

## Can a Python Class Be a Generator?

So far, we've looked at generators as Python functions using the yield method. We've also discussed generator expressions, which you get if you take a list comprehension and replace the square brackets with parentheses.

We turn next to the issue of Python classes.

Python classes can be generators. One advantage of doing so is that exposing a generator as a Python class often makes the generator simpler to reason about and may also make the generator re-usable without exhausting the underlying iterator.

Let's improve our implementation of a range-like generator in Python to see this in action. To be sure, this is still just a toy example since Python already supports a range object, but it will give us some practice in setting up a generator class.

```
class Ranger:
    def __init__(self, start=1, end=6, step=1):
        self.start = start
        self.end = end
        self.step = step or 1 # Prevent zero
        self.direction = 1 if step > 0 else 0
    
    def __iter__(self):
        if self.direction:
            return self.pos_counter()
        else:
            return self.neg_counter()
    
    def pos_counter(self):
        """A simplified range-like function for positive numbers only"""
        assert self.step > 0 and self.end >= self.start
        i = self.start
        while i < self.end:
            yield i
            i = i + self.step
    
    def neg_counter(self):
        """A simplified range-like function for negative numbers only"""
        assert self.step < 0 and self.end <= self.start
        i = self.start
        while i > self.end:
            yield i
            i = i + self.step  # self.step is negative, so subtracting

        
r = Ranger()
l1 = [x for x in r]
print(l1)

r2 = Ranger(-5, -10, -1)
l2 = [x for x in r2]
print(l2)
```

Output:

\[1, 2, 3, 4, 5\]
\[-5, -6, -7, -8, -9\]

Moving our original range clone to a class implementation allowed us to naturally encapsulate and decompose the two different use cases we had (iterating forward and backward). We rely on the `__iter__` -- the magic method that Python calls at the start of each loop -- to choose between the two based on the step value.

Although we didn't show it in this example, implementing the \_\_iter\_\_ function also allowed us to solve a subtle bug in our original generator-as-function. To learn why this is so, please see the next section.

## Why Does My Generator Only Work Once?

One problem you may bump into with generators you write is that -- unlike a list or a range object, for example -- you can only iterate them once. After that, if you try to iterate through them, nothing happens.

A generator will only work once if the iterator behind it has been exhausted. The solution is to return the generator from a class that implements the \_\_iter\_\_ function. Python loops and comprehensions will call the \_\_iter\_\_ function each time they run an iteration.

Let's look at the problem first, and then we'll show the solution:

```python
print("We can iterate a range twice:")
demo_range = range(1, 6, 1)
print([x for x in demo_range])
print([x for x in demo_range])

print("\nSame with a list:")
demo_list = [x for x in demo_range]
print([x for x in demo_list])
print([x for x in demo_list])

print("\nNOT SO with a generator!")
# Note the parentheses here to construct a generator
demo_generator = (x for x in demo_range)
print([x for x in demo_generator])
print([x for x in demo_generator])
```

Output:

```bash
We can iterate a range twice:
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

Same with a list:
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]

NOT SO with a generator!
[1, 2, 3, 4, 5]
[]
```

Being non-re-entrant is not a problem only for generator expressions, as shown here -- it's also a bug in our toy implementation of the range object as a generator function (see the section above on generator functions).

We need to wrap the generator in a class that implements the \_\_iter\_\_ protocol to fix this problem. Here's a class that shows how we might do this in the simplest way, by returning a generator expression from the \_\_iter\_\_ function():

```
class FiveNumbers:
    def __iter__(self):
        gen_exp = (i for i in range(1,6))
        return gen_exp

# Can we call it twice now?   
numbers = FiveNumbers()
print([x for x in numbers]) 
print([x for x in numbers]) 
```

Spoiler alert: it works this time!

Output:

```
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

For a more detailed example where we show a Python class wrapping a generator, see the section, [Can a Python Class Be a Generator?](https://codesolid.com/python-generators-questions-and-answers/#htoc-can-a-python-class-be-a-generator)

## What's the Equivalent of Iterable in Python?

Although there is no direct equivalent of a Java iterable in Python, the closest match in Python would be any class that implements the magic method, `__iter__()`. `__iter__()` is the method that is most closely analogous to `Iterable.iterator()` in Java.

In Python, however, there is no need for a functional equivalent of Java's `Iterable.forEach`. Magic methods in Python are more closely integrated with the core language, so the idiomatic use of a class that implements `__iter__()` would simply be to write a for loop expression with an instance of the class.

## What Are the Advantages of Generators in Python?

Generators provide two main advantages over lists, arrays, or other data structures. First, generators use less memory, so they are the right choice for large data sets. Secondly, a generator only uses memory when iterated (lazy evaluation), whereas a list uses memory whether iterated or not.

Generators are a good choice whenever the quantity of data to be iterated is large enough that memory becomes a constraint. I think the tradeoffs of generators are like those you consider when processing a file. If you know a file will be small (a configuration file, for example), go ahead and load it into memory. If, on the other hand, you expect the size of the file to be arbitrary, you're better off reading the file line by line, byte by byte, or using a fixed-length buffer.

You can demonstrate that generators are evaluated when iterated if you try to print one without iterating it. You won't see the values you'll expect; you'll see something that looks like you're examining a Python object (as indeed, you are).

```python
my_generator = (i for i in range(1,11))
print(my_generator)               
```

Output:

```bash
<generator object <genexpr> at 0x1078cf4c0>
```

## What Is an Asynchronous Generator?

An asynchronous generator is a generator defined with the async keyword. In general, one would implement an asynchronous generator to efficiently handle asynchronous input and output.

We can simulate an asynchronous process by returning a value after a random time rather than create an example of a socket or database call or the like. We'll process these values as they arrive asynchronously using an async for-loop.

```python
import random
import time

async def get_random():
    """Return random numbers, and sleep for value returned in seconds"""
    for _ in range(0,5):
        value = random.randint(1,4)
        yield value
        time.sleep(value)
        
async for i in get_random():
    print(f"get_random is sleeping for {i} seconds")

print("Finished")     
```

Output (actual values will vary):

```bash
get_random is sleeping for 2 seconds
get_random is sleeping for 2 seconds
get_random is sleeping for 3 seconds
get_random is sleeping for 4 seconds
get_random is sleeping for 3 seconds
Finished
```

## You May Also Like

- [Random Python: Secrets and Random Values Made Easy](https://codesolid.com/random-python-secrets-and-random-values-made-easy/)
- [Python Format Strings: Beginner to Expert](https://codesolid.com/random-python-secrets-and-random-values-made-easy/)
