---
title: "The Python For Loop:  Complete Tutorial and Practice Exercises"
date: "2022-06-05"
categories: 
  - "python"
  - "python-for-beginners-posts"
coverImage: "woman-programming_small.jpg"
---
# The Python For Loop:  Complete Tutorial and Practice Exercises
## Introduction: What is a For Loop In Python

The for loop is a fundamental construct in Python. It allows you to iterate through a sequence of items, such as a list or a range. In this tutorial, we will discuss the for loop in detail and provide several examples along the way and a set of exercises at the end so that you can practice using it. We will also compare the for loop with while loops and demonstrate several techniques, including how to build a list using a for loop, best practices for naming and other techniques, iterating through Python dictionaries, and several more techniques.

## Python For Loop Syntax: Iterating Through a List

We can use the for loop to iterate through any sequence of items, but our first example will use a list. The syntax for a for loop is as follows:

```python
for item in sequence:
    statement
    ...
    statement
```

Whatever is indented one level underneath the for loop, as shown above, will be controlled by the loop. (There can be further indentation levels, such as an if statement within a for loop, for example).

The for loop will execute the statement or statements inside the block for each item in the sequence. The item variable will refer to the current item in the series for each iteration of the for loop.

Let's see how this works with a simple example. We'll create a list of numbers and then iterate through it using a for loop:

```python
numbers = [0, 1, 3, 4, 5]

for number in numbers:
    doubled = number * 2
    print(number, "times 2 =", doubled) 
```

Output:

```bash
0 times 2 = 0
1 times 2 = 2
3 times 2 = 6
4 times 2 = 8
5 times 2 = 10
```

### A For Loop Best Practice

Note that part of what makes the example above so simple and readable is that we have named are variables according to a loop naming best practice. The list (sequence) is named with a plural name that describes what each element is (in this case, "numbers"). For the variable we use to store the name of each item as we go through each iteration, we use the singular form of the name in the list.

So, it's "for number in numbers" in this case. If you had a list of people, you could use "for person in people." And so forth.

Newcomers to programming will sometimes use an "i" for this item variable. However, I think this is based on confusion with other languages. In other languages, a for loop contains an index into the list, not the item from the list itself.

## Python For Loop Example: Building a List Using the Range Function

In our second example, we'll see how we can use a for loop to build a list dynamically. This example will show a popular programming pattern in which we use a Python for loop to iterate through a sequence of values and transform it into something else.

We'll start with an empty list and then add items to it using a for loop. Our example will use the range function to generate a sequence of values from 1 to 10. The range function returns an iterable sequence of numbers that is often used to iterate a specific number of times in a for loop. We start at the first number passed to the range function (which defaults to zero), and we end just before the second number we pass to the range function. So range(1, 6) counts from 1 to 5, not 1 to 6.

```python
numbers = []

for number in range(1,6):
    numbers.append(number)

print(numbers)
```

Note we must always create the empty list outside the code block that the loop controls. Then we call append inside the block of code controlled by the loop to add each element.

## For Loops vs. Comprehensions

If you're new to Python and just learning about it, you may hear at some point that creating a list, as we've shown above, is somehow "not as good" as making a list using a list comprehension. Without discussing list comprehensions in detail, there is some truth to that. However, knowing the pattern shown above is still very helpful because sometimes, the loop needs to do more than just build the list.

We focus on simple examples in tutorials such as this one. Still, as your skill progresses, you will find yourself writing for loops that need to not just iterate through a sequence. They may also have to construct strings dynamically, print values, or save results to a database in addition to creating a new sequence and returning it.

If the only thing you're doing is creating a sequence, a list comprehension is more concise. However, as a beginner, using a loop is also perfectly valid. Moreover, avoiding a list comprehension is also what you'll need if your code is doing more than simply creating a sequence.

## Using a For Loop With a Python Dictionary

Recall that you can use the for loop on any sequence. So far, we've seen lists and ranges as sequences, but dictionaries are also iterable this way. In Python, a for loop iterates through the keys of a dictionary. The syntax for this is as follows:

```python
for key in dictionary:
    statements
```

The for loop will execute the statement or statements inside the block for each key in the dictionary. The "key" variable will refer to the current key in the dictionary for each iteration.

Let's see how this works with a simple example. We'll create a dictionary and then iterate through it using a for loop:

```python
fruits = {"a": "apple", "b": "banana", "c": "cherry", "d": "Doh! Out of fruits!"}
for fruit_key in fruits:
    print(fruit_key + " is for " + fruits[fruit_key])
```

Output:

```bash
a is for apple
b is for banana
c is for cherry
d is for Doh! Out of fruits!
```

As you can see, this prints out each key and its corresponding value from the dictionary. Note that we use the dictionary key to look up the value for that key (fruits\[fruit\_key\]\]).

This is because, by default, iterating through a dictionary using a Python for loop only gives us the keys, not the values.

If you want to iterate through both the keys and values of a dictionary, you can use the items() method. To get the same output as above, use:

```python
fruits = {"a": "apple", "b": "banana", "c": "cherry", "d": "Doh! Out of fruits!"}
for fruit_key, fruit_value in fruits.items():
    print(fruit_key + " is for " + fruit_value)
```

## For Loops vs. While Loops

Loops using "for" and "while" are two of Python's most basic control structures. They both allow you to iterate through a sequence of items, but they have different purposes and uses.

Generally speaking, the Python for loop is used to implement a definite loop, one that will execute a number of times that's known in advance. Iterating through a list, for example, it will loop once for each element, or "len(list)".

The while loop, on the other hand, is most often used for what's called an indefinite loop. This type of loop will execute until some condition is met.

The while loop's syntax can be summarized as:

```python
while boolean_condition:
    statement block
```

For example, suppose you wanted to multiply a number by 2 and keep iterating through it until the product of the numbers is greater than 100. Here's how you might do it:

```python
sum = 1
while sum < 100:
    print(sum)
    sum = sum * 2
```

Output:

```bash
1
2
4
8
16
32
64
```

Another pattern that's more common with while loops rather than for loops is to loop "forever" (`while True:`) and use a `break` statement following some check on a return value or the like inside the loop. The break keyword exits the loop unconditionally.

(As an aside: It's important that there be a condition that will break out of the loop, however, otherwise, the loop could be infinite. (CTRL-C will stop it for you). Also, this sort of loop is also combined with a sleep statement to do polling of a remote server or the like; the sleep helps prevent the loop from running too tightly and consuming the CPU unnecessarily.)

Generally speaking, then, the for loop is better suited for situations where you know how many times it will need to run, and the while loop is for when you don't. That said, there are often ways to rewrite for loops as indefinite loops and while loops as definite loops

## Using the Enumerate Function

  
The enumerate function is a useful built-in function in Python that allows you to iterate through a sequence of items and also keep track of the index for each item. The syntax for using the enumerate function in a for loop is as follows:

```python
for index, value in enumerate(sequence):
    statements
```

The sequence can be a list, tuple, string, or dictionary. The enumerate function will return an object that contains the index for each item in the sequence as well as the value of each item.

Let's see how this works. The following example displays both the index and the value for the list 'a', 'b', 'c'

```python
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print(f"The letter at index {index} is {letter}.") 
```

Output:

```bash
The letter at index 0 is a.
The letter at index 1 is b.
The letter at index 2 is c.
```

## For Loop Practice Exercises

To practice what you've learned, here are some things you can try:

1. For the first exercise, create a list of numbers from 1 to 20 using the range function, and print it.
2. With the list that you created in #1, use a for loop to go through the list, and print each number that is divisible by three. You'll need to use an "if" statement and the modulo operator for this (See [Python Operators](https://codesolid.com/python-operators/) if you need a refresher on the modulo operator).
3. Try re-writing the example in #2 as a while loop. Which loop was more clear and easier to reason about?
4. Did you know strings are sequences in Python? Declare a string and write a for loop to iterate through it. How is the string divided when you do this?
5. Given the following list of Python dictionaries, write a for loop to go through the list, printing only the value given by the name key. (For this and #6, if you're not familiar with working with dictionaries, you may need to consult [Python Dictionaries for Beginners](https://codesolid.com/python-dictionaries-with-exercises/)).

```python
people = [{"name": "Eric Idle", "born": 1943}, {"name": "Terry Jones", "born": 1942}, {"name": "John Cleese", "born": 1939}]
```

6. Using the enumerate function, write a for loop that loops through each dictionary in the `people` list from the last example (#5). For each item in the list, add a new key, "index", set to the index value returned from the enumerate function.
7. One could imagine a 5 unit by 5 unit square of points on an X, Y coordinate plane, spaced one unit apart, beginning at one. If you printed out the values, it would look like this

```bash
x: 1, y: 1
x: 2, y: 1
(... 21 more lines ...)
x: 5, y: 4
x: 5, y: 5
```

The code below is partially written and shows how this can be done using nested loops. It will create the program to print this output, but each line has the word MISSING where the rest of the code should be. Replace the word missing with the correct code to make the program run as described.

```python
for y in range( # MISSING
    for x in range( # MISSING
        print( # MISSING
```

8. A Python set is a data structure that contains no duplicate items:

```python
todo_set = set(["Buy the milk", "Buy the milk", "Study Python", "Bookmark CodeSolid"])
```

Write a for loop to iterate through todo\_set, printing each value. How many times did "Buy the milk" get printed?

9\. Write a program that iterates through this string: "The quick brown fox jumps over the lazy dog", creating a list of each letter that's a vowel. Print the list of vowels.

10\. Write your own exercise and solve it. Bonus: Post your exercise and solution it in the comments section!

## You May Also Enjoy

[Python Format Strings: From Beginner to Expert](https://codesolid.com/python-format-strings/)  
  
[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)

[Python Dataclass: Easily Automate Class Best Practices](https://codesolid.com/python-dataclasses/)

[Python Indexing and Slicing: Complete Tutorial and Hands-On Exercises](https://codesolid.com/python-indexing-slicing-exercises/)
