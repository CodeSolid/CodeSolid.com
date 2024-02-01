---
title: "Useful Collection Classes in Python You May Not Know"
date: "2022-03-19"
categories: 
  - "python"
coverImage: "collection_side.jpg"
---
# Useful Collection Classes in Python You May Not Know
Most Python developers know about dictionaries, lists, and tuples -- three workhorse collections that are so useful that they repeatedly appear in Python code. Compared to other languages, these essential collections have such excellent support in the language that they feel almost like native types. For example, they all have special constructors and operators unique to their classes.

```python
# A list
my_list = [1,2,3]

# Slicing the list (reversing it in this case)
my_list[::-1]

# A dictionary
a_dict = {"key1": "value1", "key2": 42}

# Set a new item on the dictionary, not with "add" or "append"
# or "setValue", but with an # operator
a_dict["chicken"] = "Foghorn"

# A tuple
cat_in_the_hat_characters = ("Thing 1", "Thing 2")

# Sequence (tuple) unpacking
thing_1, thing_2 = cat_in_the_hat_characters

print(thing_2)
```

Perhaps because the built-in classes are so helpful and tightly integrated into the language, for a long time, I didn't learn about the Python collection classes systematically as I did when I was learning other languages. It was too easy to learn the basics and stop there. For most purposes, that's perfectly fine. Still, as I learned more about Python, I realized that some other collections are worth knowing and adding to your developer toolkit.


## Where Are Python Collections Defined

However, in searching for useful collections, it's important not to make the mistake I made at first of only looking in the collections library. You will find handy Python collections in several different places. For example, both the `dict` type and the three main sequence types (`list, tuple,` and `str`) are all defined as built-in types in Python.

We'll assume you're familiar with the primary sequence types, but you might start with [Python Lists for Beginners](https://codesolid.com/python-lists/) if you're not. Two other types originally began their lives in a separate module but are now part of the built-in types: set and frozenset. We'll discuss these later in this article because it brings up an interesting point about mutable and immutable types in Python. (And also because sets are cool!)

Another important group of collection classes is defined in the queue module, which is part of the standard library (but not a built-in). As we'll see below, this module specializes in allowing communication of results between threads.

Finally, the Python collection package contains several useful classes for specific cases. They can serve as simple data classes for storing large arrays of objects more efficiently than Python classes. They can overcome some limitations and solve problems with "regular" dictionaries. They can even allow for cases where you want to configure an application or library with a set of overridable defaults to give your users the ability to configure from the command line or the environment.

Let's look at some classes from the collection package next.

## Saving Memory with Namedtuple

Imagine a huge array of objects in memory. For example, I once worked on an underground geological mapping project dealing with three-dimensional points consisting of (x,y,z) triplets. Or better yet, think of a massive list of objects representing people. Each object might have several fields: `first_name, last_name, middle_initial, address_line_1, address_line_2, city, state, zip ...` Well, you get the picture.

You could store this in a custom class for a small list of people objects, which would be fine. However, one of the features of Python classes is that the names of the fields -- first\_name, last\_name, etc. -- are stored as dictionary keys for each object instance. If you think about it, the fact that you can add keys dynamically to an object necessitates this: we can set age on person1 and leave it off on person2 after constructing these objects. Typically, that's what we want, but as an array of such objects becomes large enough, storing these keys every time becomes a problem.

One could represent it as a tuple or other sequence type for a simple enough object. (In fact, because we were optimizing for JSON parsing time instead of memory on the project I worked on, that's exactly what we did -- we stored a list of lists, where each inner list was a point: `[ [1,2,3], [1,5,7] ...` etc.`]`.

In the case of points, losing the labels was not a big deal: we knew that they are represented x,y,z by convention. But as a list or tuple becomes large, losing the labels is a real problem. Quick: does `person[5]` mean the value for address\_line\_2, or does it mean city?

What we need in Python is something that serves the role of an immutable data transfer object. (Scala developers may recognize a favorite class of theirs from the description, the Scala "case class"). Enter the Python namedtuple class, which provides just such a feature.

To keep the example simple, let's model a point using a namedtuple. The namedtuple class is a factory for other classes that we then use to create the object. Here's how you can use it to generate point objects:

```python
from collections import namedtuple
Point = namedtuple("Point", field_names=['x', 'y', 'z'])

# Create a point using positional arguments
p1 = Point(10, 10, 20)

# Create a point using named arguments
p2 = Point(x=1.3, z=3.1, y=2.9)

# Use the spread operator on an existing dicitonary
a_point_dict = {'x': 30, 'y': 40, 'z': 54}
p3 = Point(**a_point_dict)

print(p1)
print(p2)
print(p3)
```

Output:

```
Point(x=10, y=10, z=20)
Point(x=1.3, y=2.9, z=3.1)
Point(x=30, y=40, z=54)
```

Python does not store the key names (class attribute names) for each object instance, unlike a class or a dictionary instance. That way, your program uses less memory, which becomes essential for larger lists. However, the flip side of that coin is that the object is immutable.

In most contexts, immutable objects are easier to reason about since they lead to a more "functional" programming style. It does mean, of course, that one must provide all arguments to the object in the constructor. Providing all arguments to the constructor is an effective way to make sure the object is fully initialized when it's constructed. Still, it is somewhat less convenient than adding properties as we go along.

## Using Defaultdict to Gracefully Handle Missing Values

There are some cases where we always want a dictionary to have a starting value for any arbitrary key we assign to it. If the values in the dictionary are lists, for example, a reasonable default value would be an empty list. We can handle cases like this with a standard Python dictionary, but we need to write extra code to check for the key.

To see what I mean, consider a word counting program where our task is to return a dictionary with the count of each word encountered in a string of text. Here we show such a function using a standard dictionary.

```python
def count_words(text):
    """returns a dictionary with the counts for each word in the text"""
    tokens = text.split(' ')
    tokens

    counts = {}
    for token in tokens:
        if token in counts.keys():
            counts[token] = counts[token] + 1
        else:
            counts[token] = 1
    return counts

count_words("I am a sentence with a cat, the whiskers of a cat, and a dog with no whiskers")
```

The above code listing works fine, but it is more verbose than it needs to be. To fix it, we can use the defaultdict class. This class takes a default\_factory, which allows lookups on a missing key to return a default value Here's the same counter program re-cast to use a `defaultdict`.

```python
from collections import defaultdict

def count_words(text):
    """returns a dictionary with the counts for each word in the text"""
    tokens = text.split(' ')
    tokens

    counts = defaultdict(int)
    for token in tokens:
        counts[token] = counts[token] + 1
    return counts

count_words("I am a sentence with a cat, the whiskers of a cat, and a dog with no whiskers")
```

The default for the int class is a zero, as you can show with the code `print(int())` Because that's our default factory, all we need to do in the loop is increment it each time we see a word The returned dictionary will always return a valid count for any word that occurs once, more than once, or never in the string.

## The Python Queue Package Makes It Easy to Pass Values Between Threads

The Python queue package contains one of the more interesting groups of "collection classes" in Python. Their main use-case is for inter-thread communication. They implement the correct locking semantics to balance the load and coordinate activities between threads. You can use these within a single thread too, but the documentation notes that they are not re-entrant. In other words, they cannot be called again before the first call has finished within a single thread.

The queue package contains three main classes:

- The Queue class, which implements what we usually think of as a queue structure -- that is to say, the order is "FIFO" -- First In / First Out.
- The LifoQueue reverses this order, so it's Last In / First Out. This is the order that we usually associate with a stack.
- Finally, in the PriorityQueue, items are retrieved in sorted order. The Python documentation has a fascinating [PriorityQueue example](https://docs.python.org/3/library/queue.html#queue.PriorityQueue) that uses a dataclass decorator to easily set up a class to set a priority on any class that would otherwise not be sortable.

The constructor for each class takes an extra parameter, `maxsize`, which is zero by default (unlimited). Setting this value to a positive number limits the number of items that can be in the queue at one time. Beyond this value, additional puts will block until items code in another thread removes them from the queue.

The example below provides a simple illustration of starting a producer thread and a consumer thread. In order to join on both in the main thread and not have the program hang, we set a common value for the number of items produced and consumed. Another way to do this would be to join the thread and use a timeout to specify a specific time to wait).

The producer thread puts five numbers into the queue and sleeps a random amount of time each time. The consumer thread gets five numbers out of the queue.

```python
import threading
import queue
import time
from random import randint

shared = queue.Queue()

ITEMS = 5

def producer_function():
    items = 0
    while items < ITEMS:
        items = items + 1
        print(f"Producer put: {items}")
        shared.put(items)
        time.sleep(randint(0,2))

def consumer_function():
    remaining = ITEMS
    while remaining > 0:        
        if not shared.empty():
            i = shared.get()
            remaining = remaining - 1 
            print(f"Consumer got: {i}")
            time.sleep(randint(0,2))
        
producer = threading.Thread(target=producer_function, daemon=True)
consumer = threading.Thread(target=consumer_function, daemon=True)
producer.start()
consumer.start()
producer.join()
consumer.join()
        
```

The output will vary due to the random sleep time. Here's a representative run:

```bash
Producer put: 1
Consumer got: 1
Producer put: 2
Consumer got: 2
Producer put: 3
Producer put: 4
Consumer got: 3
Consumer got: 4
Producer put: 5
Consumer got: 5
```

There are several related classes in Python similar to the Queue classes. The multiprocessing package contains a few related Queue classes used for inter-process communication rather than inter-thread communication. Beyond this, like the classes in the queue package, the deque class in the collections package supports fast appends and pops from the "left or right side" of the queue, meaning it too can serve as a deque or stack. This class is said to be thread-safe, but it's unclear whether it automatically supports locking, as do the classes in the queue package.

## Overridable Python Configuration With ChainMap

One of the hallmarks of production-ready software is that you can often configure it in multiple ways. I once worked on a product that took this to a bizarre extreme. It was configurable from the command line, a configuration file, the environment, and various combinations of the environment or the command line pointing to the configuration file. Even in cases that are less pathologically complex than this, it's frequently desirable to be able to configure an application's behavior, let's say, in the following ways:

- Read a configuration file first.
- Next, any environment variables. Overriding any settings specified in the configuration file with the environment variables, if applicable
- Finally, read the command line variables. The command line variables take precedence over both the configuration file settings and the environment variable.

For example, AWS's command-line tool (which is written in Python) implements exactly the [configuration sequence](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html) listed above.

One way to implement this in Python is to use the ChainMap class. The ChainMap implements a set of mappings so that they can be treated as a single unit. You can also accomplish this with a regular dictionary and multiple update calls, but ChainMap is documented as being somewhat faster. It also maintains each of the original maps, so one can see where the values are coming from.

We won't show the code to read the configuration file, the environment, and the command line for brevity. Let's take a more straightforward case to show how such overriding will work. The argument to ChainMap is a list or series of maps, with the maps that will be searched first appearing first in the list.

```python
from collections import ChainMap

# Some example configuration
config_settings = {"lifecycle":  "Production", "data_center": "Atlanta", "log_level": "info"}
environment = {"app_name": "Late Parrots", "log_level": "debug"}
command_line = {"app_name": "HyperGlobalMegaNet", "data_center": "Charlotte"}

# Setting up the Map
config_map = ChainMap(command_line, environment, config_settings)

# Print the values
print(f"{'KEY' : >12} : VALUE")
for key in config_map.keys():
    print(f"{key : >12} : {config_map[key]}")
```

```
         KEY : VALUE
   lifecycle : Production
 data_center : Charlotte
   log_level : debug
    app_name : HyperGlobalMegaNet
```

In this example, the `lifecycle` value came from the original configuration file settings (`config_settings`). The configuration file setting for `data_center` was overridden by the command line, which also overrode the `app_name` specified in the environment. The `log_level` from the environment was returned, overriding the `log_level` specified in the configuration file.

Though the lookup happens seamlessly, displaying either `config_map` or the variable that contains the list of the mappings, `config_map.map`, shows that the original mappings are still intact.

## Python Sets and Set Operations

A popular self-help book once had the title "All I Really Need to Know I Learned In Kindergarten." The concepts are a bit more advanced when it comes to sets, but not much. Many of us learned about sets in fifth or sixth grade when we first encountered using those fun overlapping circles called Venn diagrams to reason about them.

As in mathematics, Python sets are groups of unique elements of any type: numbers, Python blogs, dog breeds, scary news items, things that rolled under the couch -- you name it.

To make this a bit more concrete, let's look at some Python sets and some operations we can do on them.

```python
low = set((1,2,3,4,5))
low_subset = set((1,2,3))
high = set((4,5,6,7,8))
```

Given these three sets, we can show some results we'd get for various set operations. In some instances, we have a couple of different ways to get the result.

### Most Useful Operations on Python Sets

<table><tbody><tr><td>To do this:</td><td>Use this code</td><td>Equivalent (if any)</td><td>Result</td></tr><tr><td>Test membership in a set.</td><td><code>2 in low<br>2 in high</code><br><code>2 not in high</code></td><td></td><td><code>True<br>False</code><br><code>True</code></td></tr><tr><td>Find out if two sets have no common elements.</td><td><code>low.isdisjoint(high)</code></td><td>There are other ways to do this, but they are not as good.</td><td><code>False</code></td></tr><tr><td>Find common members of sets.</td><td><code>low.intersection(high)</code></td><td><code>low &amp; high</code></td><td><code>{4,5}</code></td></tr><tr><td>Find out if a set is a subset/superset of another set.</td><td><code>low_subset &lt;= low<br>low &gt;= low_subset</code></td><td><code>low_subset.issubset(low)<br>low.issuperset(low_subset)</code></td><td><code>True<br>True</code></td></tr><tr><td>Combine all the members into a new set (union)</td><td><code>low.union(high)</code></td><td><code>low | high</code></td><td><code>{1, 2, 3, 4, 5, 6, 7, 8}</code></td></tr><tr><td>Find members of a set that aren't in members of one or more other set(s)</td><td><code>high.difference(low, low_subset)<br></code><br><code>high.difference(low)</code></td><td><code>high - low - low_subset<br><br>high - low<br></code></td><td><code>{6, 7, 8}</code><br><br><code>{6, 7, 8}</code></td></tr><tr><td>Find members that are in one or other but not both (opposite of intersection)</td><td><code>low.symmetric_difference(high)</code></td><td><code>low ^ high</code></td><td><code>{1, 2, 3, 6, 7, 8}</code></td></tr><tr><td>Find out if a set is empty/non-empty</td><td><code>len(low) == 0<br>len(low) != 0</code></td><td></td><td><code>False<br>True</code></td></tr></tbody></table>

For more information and use cases, see the [Python 3 set documentation](https://docs.python.org/3.10/library/stdtypes.html#set).

## Mutable and Immutable Collections and Sequences in Python

Before wrapping up our discussion of Python collections, we should take a moment to discuss mutable and immutable collections and types in Python. This difference is worth understanding if we want to understand the difference between `set` (which we've talked about quite a bit) and `frozenset`. As you've probably guessed by now, a frozenset is not something you need to defrost to put in the microwave -- it's an immutable set. It's also hashable.

According to the official definition of [hashable](https://docs.python.org/3.10/glossary.html#term-hashable) types:

> An object is _hashable_ if it has a hash value which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` method). Hashable objects which compare equal must have the same hash value.
> 
> https://docs.python.org/3.10/glossary.html#term-hashable

As you can see, part of the definition of hashable is that the object is immutable, that is, "it has a hash value which never changes during its lifetime." The other crucial part is the \_\_eq\_\_() method, which, together with the \_\_hash\_\_() method means that hashable types can be efficiently compared.

These properties are essential in the context of our discussion of Python collections for at least two reasons:

- Dictionary keys must be hashable types. Given that dictionaries are implemented as a hashtable, this makes sense. A hashtable is effectively a mapping of elements with a fast hash function to a set of "slots" that contain the values.
- The elements stored in a Python sets or frozensets must also be hashable, because fast tests for membership is an important characteristic of sets. So you can think of a set as a kind of dictionary that only has keys. Indeed, in other languages (I'm looking at you, [Golang](https://go.dev/blog/maps)), there is no set type. The idiom there if you need a set is to use a map (Hashtable) of keys to boolean False.

Because the frozenset type is hashable, if you need to model a set of sets, the set can either be a frozenset or not, but the elements _must_ be frozen sets.

Citation: Although the content here is original, a work that influenced and informed several parts of this article was Brett Slatkin's outstanding [Effective Python - 90 Specific Ways to Write Better Python](https://www.amazon.com/Effective-Python-Specific-Software-Development/dp/0134853989/ref=sr_1_1?crid=2CXWAWXHX0ZOW&keywords=Effective+Python&qid=1647689385&sprefix=effective+python%252Caps%252C64&sr=8-1&_encoding=UTF8&tag=codesolid-20&linkCode=ur2&linkId=1c3df20577c978bdae5ee5653644bb1c&camp=1789&creative=9325).

## You May Also Like

[Random Python: Secrets and Random Values Made Easy](https://codesolid.com/random-python-secrets-and-random-values-made-easy/)

[Python Dataclass: Easily Automate Class Best Practices](https://codesolid.com/python-dataclasses/)
