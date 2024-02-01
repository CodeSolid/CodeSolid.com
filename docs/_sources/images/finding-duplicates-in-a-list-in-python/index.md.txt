---
title: "How to Find Duplicates In a List in Python"
date: "2022-11-02"
categories: 
  - "python"
coverImage: "programmer_smalll.jpeg"
---

Dealing with messy data is a common task. Data analysts recognize that data cleaning is where they spend a lot of their time, but software engineers also have to contend with it from time to time.

One typical example of messy data is a list with duplicate entries, so finding the duplicates in a list is a common thing to do. The most common reason for this is that we need to find the copies to return a list that is "pared down," where each element is unique.

Like so many programming tasks, Python makes this easy to do. However, the best approach depends on several things. If we are doing this duplicate search to remove duplicates, we may or may not need to preserve the order, so we'll dive into both solutions here. If we don't care about the order, there's an even simpler solution that works across all versions of Python from 2.4 on.

Since these are the most common cases, we'll deal with those right up front. We will begin with straightforward instances in which the elements are strings or numbers that are easily compared. Next, we'll consider two related topics:

- What if the objects you're dealing with are not simple but are lists of custom objects? How can we deal with objects with some unique key, for example? How can we ensure that the code we wrote for strings or numbers also works here?

- What if instead of removing the object, we want to find the duplicate counts?

But again, let's start with the simplest cases first!

## Finding Duplicates in a List When Order Doesn't Matter

If the order of the elements in the Python list doesn't matter, the trick to eliminating duplicate values is simply to think about a data structure that's like a list, but guarantees that the items are unique without preserving the order. Go ahead and think about it. I'll give you a minute...

If you thought about a Python set type, you get the gold medal in my only guessing game in this article (promise). We can leverage the fact that sets guarantee uniqueness (in Python as in other languages as in mathematics). So all we have to do is convert the list to a set, then back into a list, and return the new list.

Let's write the function and a quick test for it.

```python
from typing import List

def get_unique_elements(input: List) -> List:
    """returns unique elements without preserving the order"""
    return list(set(input))

# Test it
too_much_cheese = ["cheese", "pizza", "chicken", "cheese", "grapes", "cheese"]
unique = get_unique_elements(too_much_cheese)
print(unique)
```

Output:

```bash
['cheese', 'chicken', 'pizza', 'grapes']
```

As you can see, all the elements are there, but the order was changed. "Cheese" now comes before "chicken".

## Removing Duplicates from a List With Order Preserved

To remove duplicates from a list in Python while preserving the order, we use the `fromkeys` function of dict or OrderedDict (depending on the Python version), then convert the result to a list.

Python dictionaries have preserved the order of inserted elements since Python 3.6, so reworking our example above to preserve the list's order while removing the duplicates can be done using a dictionary.

Here's the code for newer versions of Python:

```python
from typing import List

def get_unique_elements_ordered(input: List) -> List:
    """returns unique elements.  Preserves order.  Python 3.5 and earlier"""
    return list(dict.fromkeys(input))

unique_ordered = get_unique_elements_ordered(too_much_cheese)
print(unique_ordered)
```

Now the output preserves the same order as the list, but with the extra cheese removed:

\['cheese', 'pizza', 'chicken', 'grapes'\]

In Python 3.5 and earlier, we can do the same thing by making the minor changes shown in bold below:

from typing import List
**from collections import OrderedDict**

def get\_unique\_elements\_ordered(input: List) -> List:
    """returns unique elements.  Preserves order.  Python 3.5 and earlier"""
    r**eturn list(OrderedDict.fromkeys(input))**
unique\_ordered = get\_unique\_elements\_ordered(too\_much\_cheese)
print(unique\_ordered)

This gives the same output as above.

## Removing Duplicates in a List of Complex Objects

So far we've been looking at solutions that rely on either a Set or a dictionary or OrderedDict to ensure that the object is unique. We then convert that to a new list and return it.

This works fine for many simple built-in types like numbers and strings. However, when we start to deal with objects, things get a bit more interesting, and we need to do a little more work.

To see why let's begin by considering a really simple user-defined function. Suppose we want to save a list of people and their phone numbers. We'll consider people to be duplicates if both their first name and their phone number are the same.

Our class just has a phone field and a name field.

```python

class Person:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"Person({self.name, self.phone})"

# Our list of close friends
people = [
    Person("Melissa", "9193612495"),
    Person("Jon", "5083412318"),
    Person("Ida", "7043756942"),
    Person("Melissa", "9193612495")
]  
```

As you can see, we have two friends named Melissa who also have the same phone number. In our earlier examples, we returned our unique list using either a set or a dict as an intermediate structure.

Let's try that here to see if we get unique values. Do we go from four elements to three as we expect?

```python
a_dict = dict.fromkeys(people)
a_set = set(people)

print(len(people))
print(len(a_dict))
print(len(a_set))
```

Output:

```bash
4
4
4
```

Interestingly, Python's default behavior allows us to add the objects as keys to a dictionary or store them in a set, but we're not getting the behavior we want.

The problem here is that Python really doesn't know if two objects contain the same information or not. We might want a phone number as a key. Often in a store's point-of-sale system, that's how they look you up as a customer. On the other hand, we might want to compare the whole object.

By default, Python implements two "dunder" methods related to object equality. (Dunder methods are special methods that begin and end with double underscores, hence **D**ouble + **UNDER**score = "dunder"). Because Python doesn't know how user-defined objects can be compared, it

The reason our code does not work yet is that by default, Python implements both of these dunder methods in terms of the object's identity (a numeric value that Python uses internally to keep track of object instances). Because we created a duplicate Melissa as a new object, Python considered her to be a different object than the original Melissa, even though they have the same name and phone number.

We want to prevent such human cloning. We want only one Melissa. To implement this behavior, the two dunder methods we need are `__eq__` and `__hash__`. The first should return True if we consider the object passed into it to be equal to the current object. The second should return an integer value that Python can use to decide where to store it in the hashtable so it can quickly be retrieved. (Dicts and sets are both implemented as hashtables internally).

Here are the two methods we need to add to our Person class:

```python
    def __hash__(self):
        return hash(self.phone + self.name)
    
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
```

Now our test code works as expected. If we add our people to either a set or a dict, clone Melissa doesn't get to come to the party:

```
people = [
    Person("Melissa", "9193612495"),
    Person("Jon", "5083412318"),
    Person("Ida", "7043756942"),
    Person("Melissa", "9193612495")
]  

a_dict = dict.fromkeys(people)
a_set = set(people)

print(len(people))
print(len(a_dict))
print(len(a_set))
```

Output:

```bash
4
3
3
```

Of course, if we wanted to, we could implement the hash function differently, in this case comparing only the phone number, for example.

## Find Duplicates in a List to Count the Entries

Next to removing duplicates, perhaps the most common reason to find duplicates in a list is to count the number of entries. When analyzing text, for example, you might want to know how often a word occurs.

You might first think of using a dictionary to do this. This is a reasonable approach since the words could be stored as keys and the counts as values. However, in Python, there's a Counter class specialized for this purpose that makes the task even easier. All you have to do is pass the list to the constructor to create a dictionary-like object that processes the counts for you automatically.

Let's demo this briefly by printing the word count of an important question my father taught me to ask:

```python
# Count duplicates using the counter class

from collections import Counter

question = "How much wood would a woodchuck chuck if a woodchuck could chuck wood ?"
question = question.split()
count = Counter(question)    
print(count)
```

Output:

```bash
Counter({'wood': 2, 'a': 2, 'woodchuck': 2, 'chuck': 2, 'How': 1, 'much': 1, 'would': 1, 'if': 1, 'could': 1, '?': 1})
```

Since Counter has a dictionary interface, we can get the count for any value. Counter returns zero if the key is not in the dictionary (unlike a dict, which will raise a key error).

```python
print(count['woodchuck'])  # prints 2
print(count['squirrel'])         # prints 0
```

Without the Counter class (which is built-in to Python since version 3.1), we could still accomplish this, with the following more verbose code:

```python
# Count duplicates without the counter class (3.0 and earlier)

question = "How much wood would a woodchuck chuck if a woodchuck could chuck wood ?"
question = question.split()
count = {}
for word in question:
    added = count.get(word)
    if added is None:
        count[word] = 1
    else:
        count[word] = count[word] + 1
        
print(count)
```

By the way, we cheated a bit in our example above and added a space before the question mark. The issue of punctuation and case matching muddies the water a bit. Removing multiple punctuation characters is easy to do but doing it efficiently is a topic that's a bit bigger than we want to dive into for this article.

## You May Also Enjoy

- [Python Lists for Beginners](https://codesolid.com/python-lists/)

- [Python Indexing and Slicing: Complete Tutorial and Hands-On Exercises](https://codesolid.com/python-indexing-slicing-exercises/)

- [Python Lists vs. Arrays: How to Choose Between Them](https://codesolid.com/python-lists-vs-arrays/)

- [Python Dictionaries for Beginners: A Complete Lesson With Exercises](http://Python Dictionaries for Beginners: A Complete Lesson with Exercises)
