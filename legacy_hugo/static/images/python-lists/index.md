---
title: "Python Lists for Beginners: A Complete Lesson With Exercises"
date: "2022-02-21"
categories: 
  - "python-for-beginners-posts"
  - "python-practice"
coverImage: "coding-notebook-smaller-1.jpeg"
---

Python lists are one of its most flexible and widely used data types. This article is a beginner's guide to Python lists, but like everything in programming, remembering what you learned requires sufficient early practice. With this in mind, in addition to the lesson, we also feature several exercises at the end that you can use to review and reinforce what you've learned. These lessons come with links to live Jupyter notebooks you can run both for the exercises themselves and the solution set (in case you get stuck).

## Introduction

The basic idea of a list is straightforward because most people already know how to use a list in real life. We might have a list of things to do, for example:

- Finish work project

- Stop at the pharmacy

- Return parrot to the pet store

## Creating a list in Python

Here's how easy it is to create a Python list with those items:

```python
todo_list = ["Finish work project", "Stop at the pharmacy", "Return parrot to the pet store"]
print(todo_list)
```

```bash
['Finish work project', 'Stop at pharmacy', 'Return parrot to pet store']
```

Square brackets tell Python we're dealing with a list. It's also possible to use a list constructor -- `"list()"`. But it's more common to use square brackets, as we've done here. We can even create an empty list that way:

```python
empty = []
print(type(empty))
```

```
<class 'list'="">
```

In the case of our to-do list example, we wanted to populate the list in advance, so we included three strings. Inside the list, we separate each list item with a comma.

## Lists can contain items of any Python type

We can add any Python object to a list -- numbers, strings, dates, user-defined classes, dictionaries -- even other lists.

We can even mix and match types in a single list, but just as in real life, this isn't something you usually want to do unless the items are related somehow. It would make the meaning of the list unclear, and it would be hard to write valid code to process the list.

```python
# A list of numbers
prime_numbers = [2,3,5,7]

# The three stooges
stooges = ['Moe', 'Larry', 'Curly']

# A list of lists
all_my_lists = [prime_numbers, stooges]

# An unclear list of mixed types -- bad idea!
some_list = [42, 3.14, "Make some soup", "Yugoslavia"]
```

## Python Lists are Ordered

The elements in a Python list are ordered with numbers beginning with zero. This numbering scheme may seem odd for new programmers, but it's standard. Most programming languages start counting from zero rather than one, so this is also how C, Java, JavaScript, and many other languages do it.

The fact that lists maintain their items in order means we can retrieve or change an element in the list if we know where it appears.

Let's look at several things we can do with lists in the following code segment. We'll start with a small list of countries to see what we can do.

```python
countries = ['United States', 'Colombia', 'Japan', 'Kenya']

# Get the first country into a variable.  
# Use the list name, the [] operator, and the zero-based index in the list.
usa = countries[0]
print(usa)

# Find the zero based-index of Japan
location = countries.index('Japan')
print("Japan is at index: ", location)

# Find out how many countries are in the list
length = len(countries)
print("There are", length, "countries in the list.")

# Change the last item in the list.
# Since the list counting is zero based, the index of the last 
# item is the list's length - 1
countries[length - 1] = 'Republic of Kenya'

# Print the list
print(countries)
```

```
United States
Japan is at index:  2
There are 4 countries in the list.
['United States', 'Colombia', 'Japan', 'Republic of Kenya']
```

To review, we learned several basic operations that work on lists in the last section.

- `list_name[SOME_NUMBER]`. Given a list's name, add a number in square brackets after it either to return the item (for example, to set it to a variable), or to set the item (by using an assignment expression after it). The numbering of list items starts at zero.

- `len(list_name)`. The `len` function returns the number of elements in the list. The index of the last list item is at len(list\_name)

## Iterating a list with a for loop

Iterating a list with a for loop is a simple technique you'll use again and again in your Python code. Here's how to do it:

```python
countries = ['United States', 'Colombia', 'Japan', 'Kenya']

for country in countries:
   print(country)
```

Output:

```bash
United States
Colombia
Japan
Kenya
```

A for loop with a list is very simple. It consists of the word "for," a variable to hold each element as we iterate through the list, the word "in," the name of the list, and a colon. You indent the statements you want to run "inside the loop" underneath the main body of the loop. (The tab key is usually the best way to do this). We only have one statement in the loop above, but you can have more than one indented line beneath the for loop's first line. For example, here, we print out the country's name on one line and print out the number of characters in the country's name.

```python
for country in countries:
   print(country)
   print(len(country))
```

Output:

```bash
United States
13
Colombia
8
Japan
5
Kenya
5
```

## Modifying the List Elements

Lists are considered a mutable data structure. Not only can you change the value of a list element (as we saw above for 'Republic of Kenya'), but you can also modify the list members in other ways.

Three list methods for accomplishing this are:

- `list.append` - Adds an item to the end of the list.

- `list.remove` - Removes the first item with the specified value

- `list.insert` - Adds a new item at the specified index, moving the other elements over.

Let's see these methods in action on our countries list.

```python
countries = ['United States', 'Colombia', 'Japan', 'Kenya']

# Remove Japan, list will now have three items
countries.remove('Japan')

# Add two new countries at the end of the list
countries.append('China')
countries.append('Belgium')

# Add a new country at index 1
countries.insert(1, 'Canada')

print(countries)
```

Output:

```bash
['United States', 'Canada', 'Colombia', 'Kenya', 'China', 'Belgium']
```

## Creating a List Dynamically - First Method (Loops)

We can combine a for loop with the append method to dynamically create a list. Suppose we had a list of words and wanted to return a new list with the length of each one. One common approach to a problem like this is to create a new empty list before we loop through the list of words, then append a length for each word we process inside the loop.

Suppose we wanted to print the lengths of several words in a list, then return an array consisting of the lengths of each at the end.

```python
# We use the split method to create a list from a sentence
words = 'a short list of words of different lengths'.split(' ')

lengths = []
for word in words:
    length = len(word)
    print(length, ":", word)
    lengths.append(len(word))
   
print(lengths)
```

Output:

```bash
1 : a
5 : short
4 : list
2 : of
5 : words
2 : of
9 : different
7 : lengths
[1, 5, 4, 2, 5, 2, 9, 7]
```

In this case, it makes sense to build the list of lengths in the loop because printing the length of each word is another task we have to do simultaneously. However, if all we're doing is building the list, there's a much more concise and efficient way to do it in Python.

By the way, you may have noticed that we use the same function, "`len`"to return the length of either a string or a list. The `len` function also works on other Python types, such as tuples and dictionaries.

## Creating A List Dynamically (List Comprehensions)

For times when you don't have another task to perform when you're creating the list, Python has a much more concise and elegant syntax, called a "list comprehension." Here's our example above, now reworked to use a list comprehension:

```python
words = 'a short list of words of different lengths'.split(' ')
lengths = [len(word) for word in words]
print(lengths)
```

Output:

```bash
[1, 5, 4, 2, 5, 2, 9, 7]
```

As with loops, list comprehensions can also include conditions to use as filters. For example, let's say we want to filter a list of words, including only those with more than five characters. Here's how we can do it with a list comprehension:

```python
words = ['Long', 'words', 'include', 'grammarian', 'programmer', 'prestigious', 'and', 'beautiful']

# Filter
long_words = [ w for w in words if len(w) > 5]

print(long_words)
```

Output:

```bash
['include', 'grammarian', 'programmer', 'prestigious', 'beautiful']
```

## Slicing

We've already seen how to select a single list element with an index. Python also has a related mechanism for obtaining a subset of several list elements at once. Slices are ranges of elements that Python will select from the list. You may find this syntax a little challenging at first, but I guarantee that if you get some experience with it, you'll come to love what it can do!  
  
Some examples will help to demonstrate how slicing works.

```python
numbers = [0,1,2,3,4,5,6,7,8,9,10]

first_four = numbers[0:4]
print("first_four =", first_four)

last_three = numbers[8:]
print("last_three =", last_three)
```

Output:

```bash
first_four = [0, 1, 2, 3]
last_three = [8, 9, 10]
```

To create our array, "`first_four`"we sliced numbers using two numbers, zero and four. Python slices _include_ the starting index but _exclude_ the ending one, so this slice gave us the numbers from index zero to index three. Our second example shows that if we omit the last index, it defaults to the end of the list. Similarly, if we leave out the first index, it defaults to the beginning of the list. Because of this behavior, we could make a copy of the whole list with the slice: "`numbers[:]`".

So far, we've seen how the first index and the last work, but slices also have an optional third part that we haven't discussed yet. The third term of a slice represents a step value, which by default is +1. Setting it to a different value causes it to skip elements, and setting it to a negative value reverses the order of the returned elements.

Let's see some examples of this:

```python
last_three_again = numbers[:-3]
print("last_three_again =", last_three)

every_other_number = numbers[0::2]
print("every_other_number =", every_other_number)

reversed = numbers[::-1]
print("reversed = ", reversed)
```

Output:

```bash
last_three_again = [8, 9, 10]
every_other_number = [0, 2, 4, 6, 8, 10]
reversed =  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

In the first example, we slice "three elements beginning at the end," using a negative index for our end value. In the second example, stepping by two has the effect of selecting only even numbers from the list. In the final example, we use the same slice we used to copy all the elements but add a -1 as the third term. Doing this causes the slice to operate backward, effectively reversing the list.

## Python List Exercises for Beginners

If you're a beginner and you've made it this far, congratulations! You've learned a lot. However, most new programmers find they need a lot of practice to remember what they've learned. Taking the lesson above and reworking it is a great way to do this. When you're ready, here are more exercises that you can work through based on this lesson. It's best to try these out on your own, using the lesson above as a reference. However, there's also a link to the solutions after the exercises.

[Source Code](https://github.com/CodeSolid/CodeSolid.github.io/blob/main/booksource/exercises/ListExercises.ipynb)

[Code Exercises Online](https://colab.research.google.com/github/CodeSolid/CodeSolid.github.io/blob/main/booksource/exercises/ListExercises.ipynb)

1. Create a list of three of your favorite foods.

3. From your list of favorite foods, select the second item.

5. Using a slice, create a reversed copy of your list of favorite foods.

7. `"my name is john".upper()` returns the string "MY NAME IS JOHN". Given that fact, create an uppercase list of your favorite foods using a for loop.

9. Create a second uppercase list of your favorite foods, using a list comprehension.

For exercises 6-14, use the following list as your starting point.

```python
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
```

6. Use a function to get the length of the letters list. Display it.

8. Get the last item in the list, using a positive index.

10. Get the last item in the list, using a negative index.

12. Write a slice expression to return the letters D through F (inclusive)

14. Write a slice expression that returns the following list: \['A', 'D', 'G'\]

16. Based on what you learned in exercise 4, can you guess how to write a program to return a list of lowercase letters based on the `letters` list?

18. For #11, did you iterate the list using a list comprehension or a for loop? Why?

20. How could you return a copy of the list using a slice expression?

22. How could you return a list that looks like the list below:

```python
['G', 'F', 'E', 'D', 'C', 'B', 'A']
```

15. The range function returns a sequence -- that is to say, it can be used as you would use a list inside a for-loop or list comprehension. For example:

```python
num_list = [x for x in range(1,6)]
print(num_list)
```

Output:

```bash
[1, 2, 3, 4, 5]
```

Based on what you know about slice syntax, what would you expect the output of the following code to be?

```python
num_list = [x for x in range(0,26,5)]
print(num_list)
```

16. What do you predict will be printed by the code below?

```
num_list = [x for x in range(1,6)]
num_list[0:2] = [99, 100]
print(num_list)
```

17\. Here's a slight variation on the code from #16. What do you expect will be printed by the following code?

```python
num_list = [x for x in range(1,6)]
other_list = num_list[:]
other_list[0:2] = [99, 100]
print(num_list)
```

View Solutions

## You May Also Like

[Learning C++ and Python: The Perfect Duo for Success](https://codesolid.com/learning-c-and-python-the-perfect-duo-for-success/)

[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)

[Python Indexing and Slicing: Complete Tutorial With Hands-on Exercises](https://codesolid.com/python-indexing-slicing-exercises/)

[How to Find Duplicates in a List in Python](https://codesolid.com/finding-duplicates-in-a-list-in-python/)

[Python String Examples: Tutorial and Practice Exercises](https://codesolid.com/python-string-examples-tutorial-and-practice-exercises/)
