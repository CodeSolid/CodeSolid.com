---
title: "Python String Examples:  Tutorial and Practice Exercises"
date: "2022-08-22"
categories: 
  - "python-for-beginners-posts"
tags: 
  - "featured"
coverImage: "image-34.png"
---

Table of Contents

- [Introduction](#htoc-introduction)
- [What Are Python Strings?](#htoc-what-are-python-strings)
- [How to Create Strings in Python?](#htoc-how-to-create-strings-in-python)
- [How to Access Characters in Python Strings?](#htoc-how-to-access-characters-in-python-strings)
- [String Slicing](#htoc-string-slicing)
- [How to Modify or Change a String in Python?](#htoc-how-to-modify-or-change-a-string-in-python)
- [String Operators in Python](#htoc-string-operators-in-python)
- [String formatting in Python](#htoc-string-formatting-in-python)
    - [f-strings](#htoc-f-strings)
- [Built-in Python String Functions](#htoc-built-in-python-string-functions)
- [Built-in Python String Methods](#htoc-built-in-python-string-methods)
- [If-Statements with Strings in Python](#htoc-if-statements-with-strings-in-python)
- [Iterating Through Strings in Python](#htoc-iterating-through-strings-in-python)
- [Python String Exercises for Beginners](#htoc-python-string-exercises-for-beginners)
- [Conclusion](#htoc-conclusion)
    - [You May Also Enjoy](#htoc-you-may-also-enjoy)

## Introduction

This tutorial will focus on the Python string data type. 

Python provides a rich set of built-in operators, functions, and methods for working with strings. We will learn how to access some elements of strings and call various methods to manipulate, format, and modify strings using Python.

## What Are Python Strings?

A string in Python is an object containing sequences of character data.

## How to Create Strings in Python?

We must enclose characters in single quotes, double quotes, or even triple quotes to create strings. Triple quotes in Python are used to represent multi-line strings and docstrings.

```python
# defining strings in Python
# using single quotes
my_string = 'String'

# using function type() to get the data type of my_string, 
# and printing the string
print(type(my_string)) 
print(my_string)

# using double quotes
my_string = "String"
print(type(my_string))
print(my_string)


# using triple quotes
my_string = '''String'''
print(type(my_string))
print(my_string)
# strings with triple quotes can be multi-line string
my_string = """Multilinestrings
are
cool"""

print(type(my_string))
print(my_string)
```

If we run this code, we see that the output and the data type are the same, no matter what quotes we used: 

```bash
<class 'str'>
String
<class 'str'>
String
<class 'str'>
String
<class 'str'>
Multilinestrings
are
cool
```

## How to Access Characters in Python Strings?

In Python, we can access individual elements of a string using the indexing method, and the index always starts at 0. However, we can also use negative indexing to access characters from the end of the string. 

For example, -1 refers to the last character, -2 refers to the pre-last character, and so on. 

![](images/image-34-1024x553.png)

```python
# accessing string characters in Python
my_str = 'hello'
print('my_str =', my_str)

# accessing first character

print('my_str[0] =', my_str[0])     # using index 0
print('my_str[-5] =', my_str[-5])   # using negative index -5

# accessing last character

print('my_str[-1] =', my_str[-1])   # using negative index -1
print('my_str[4] =', my_str[4])     # using index 4
```

Output:

```
my_str = hello
my_str[0] = h
my_str[-5] = h
my_str[-1] = o
my_str[4] = o
```

Attempting to access a character outside the index range will raise an IndexError, and trying to enter a non-integer number as an index or any data type other than an integer will result in a TypeError.

```python
my_str = 'hello'
# trying to get character using index out of range
print('string[19] =', my_str[19])

# trying to get character using float index
print('string[1.9] =', my_str[1.9])
```

Output:

<table><tbody><tr><td><img src="https://lh6.googleusercontent.com/5tyLAu1Pv6mM3YcB0QA9Xh9V_F97-pIHrwxAJnenlzklCqKZpNZ2s9I6KoFVQ0nEfDZxk82a5f6FrwpvE1rtRMBX3uFiV_4riuTcoOa1sXsJ_omMO3L9NVLaWrrVo2ee1nPvpaI-Nj38mbQL7ui0Tzg" width="479" height="98"><img src="https://lh5.googleusercontent.com/5Lx0xhyaOx5ldZiIKqHCNN7QhjPjJYR1Xw9Zk9SKfAHQUkkA6NTm5dWrRGiVoHCGCy1AoSBww-0biA9KeH0aJ0DAvbtnSnUxLZLY9i7NlUkNV6NjYJgAAuxKFuleDBwDDB7Air9YtrbsHXpcAUtBDFY" width="436" height="100.93496578505795"></td></tr></tbody></table>

## String Slicing

We can access a range of characters in a string using the slicing method. Slicing in a string is done with the slicing operator (colon). 

```python
# creating a string
my_str = "hello"
print("Initial String: ")
print(my_str)

 
# printing 2nd to 4th character
print("\nSlicing characters from 2-4: ")
print(my_str[2:4])

# printing characters between 5th and 2nd last character
print("\nSlicing characters between 5th and 2nd last character: ")
print(my_str[-5:-2])
```

Output:

```bash
Initial String: 
hello

Slicing characters from 2-4: 
ll

Slicing characters between 5th and 2nd last character: 
hel
```

## How to Modify or Change a String in Python?

In Python, we cannot update or delete string elements like in lists since strings are immutable, and trying to do so will cause an error. However, we can delete the entire string using del or create a new string with the same name to replace it completely.

Let's try to change the character in the string:

```python
my_str = "hello"
my_str[1] = "i"
```

As we can see in the output it causes a TypeError:

<table><tbody><tr><td><img src="https://lh5.googleusercontent.com/KLi9PNE40bu72o9kdxKAS9O7hhdkOrQFOrlnDyjabAU0F3Hn-O1lu-4Fkq4JLZ0cLIsYpSppe0bkZ7QV486Isk9B76yXITvdYeEmuo0uu5B6xMBZitlLg6FF18HWdiH9vU0bmrNFIRz-YgTLjMr1ZX8" width="446" height="84"></td></tr></tbody></table>

Now let us try to replace the whole string with another:

```python
my_str = "hello"
print("My string before:", my_str)

my_str = "hi"
print("\nMy string after:", my_str)
```

Output:

```bash
My string before: hello

My string after: hi
```

Deleting certain elements using indexes is not supported as well:

```python
my_str = "hello"
del my_str[1]
```

Output:

<table><tbody><tr><td><img src="https://lh3.googleusercontent.com/5VxI7SlTRi5-LH9nE9bvZbeh3LJpfGbxx3s2oOf2r8zpL9ZSzdOKkJx_LQ1O-CN9_nibUfja52KKYq6DwbnL6CFatb6CV-9bbs7DVJUt0TbspLIVT7ibs9vrniMEtqe0A8fUutpQDC3QIUyGFk4c2kA" width="391" height="72.19444444444444"></td></tr></tbody></table>

However, we can delete the string itself:

```python
my_str = "hello"
del my_str
print(my_str)
```

You can see in the output that we got NameError which means that our variable my\_str doesn't exist:

<table><tbody><tr><td><img src="https://lh3.googleusercontent.com/otUCcUfu2zXqklKWdvfx0VTORpgeD2fc3PVJFf-3wlf8pfBnZTgG8jlutjmZFEw_sFrWAWL7AKLr-C6qjzDPtx3pZfqIH3x6WUh1NalYXzCVonVnx7ndLeZZiOIqDSl0SJKINl6G8sJ30MZ_cEZbgC4" width="311" height="97"></td></tr></tbody></table>

## String Operators in Python

String operators in Python are different types of operators that can be applied to strings. Below you will find a list of operators for strings:

<table><tbody><tr><td><strong>Operation</strong></td><td><strong>Operator</strong></td></tr><tr><td>Assigning</td><td>=</td></tr><tr><td>Concatenation</td><td>+</td></tr><tr><td>String repetition</td><td>*</td></tr><tr><td>String slicing</td><td>[]</td></tr><tr><td>String comparison</td><td>==&nbsp;!=</td></tr><tr><td>Membership checking</td><td>innot in</td></tr><tr><td>Escaping sequence</td><td>\</td></tr><tr><td>String formatting</td><td>%{}</td></tr></tbody></table>

Let's look at how to perform some operations that we did not consider from the list:

```python
# Concatenation
str1 = "hello "
str2 = "world"
string = str1 + str2
print("This is concatenation: ", string)

# String repetition
str1 = "hello "
print("\nThis is string repetition: ", str1 * 5)

# String comparison
str1 = "hello"
str2 = "hello,world"
str3 = "hello,world"
str4 = "world"

print("\nThis is string comparison:")
print("'hello' and 'world' are the same? ",str1==str4)
print("'hello,world' and 'hello,world' are the same? ", str2 == str3)
print("'hello' and 'world' are different? ",str1!=str4)
print("'hello,world' and 'hello,world' are different? ", str2 != str3)

# Membership checking
str1 = "helloworld"
print("\nThis is memebership checking:")
print("Is 'w' in 'helloworld'? ", "w" in str1)
print("Is 'W' in 'helloworld'? ", "W" in str1)
print("Is 't' in 'helloworld'? ","t" in str1)
print("'t' is not in 'helloworld'? ", "t" not in str1)
print("Is 'hello' in 'helloworld'? ","hello" in str1)
print("Is 'Hello' in 'helloworld'? ","Hello" in str1)
print("'hello' is not in 'helloworld'? ","hello" not in str1)

# Escaping sequence
string = "\nHello,\"world\""
print("\nA string with escape sequence:", string)
```

Output:

```bash
This is concatenation:  hello world

This is string repetition:  hello hello hello hello hello 

This is string comparison:
'hello' and 'world' are the same?  False
'hello,world' and 'hello,world' are the same?  True
'hello' and 'world' are different?  True
'hello,world' and 'hello,world' are different?  False

This is memebership checking:
Is 'w' in 'helloworld'?  True
Is 'W' in 'helloworld'?  False
Is 't' in 'helloworld'?  False
't' is not in 'helloworld'?  True
Is 'hello' in 'helloworld'?  True
Is 'Hello' in 'helloworld'?  False
'hello' is not in 'helloworld'?  False

A string with escape sequence: 
Hello,"world"
```

## String formatting in Python

Python gives us the ability to convert objects to printable strings automatically. There are two built-in ways to do this: formatted string literals or "f-strings" and `str.format()` function.

### f-strings

A formatted string literal is prefixed with 'f'. Any text outside curly braces' {}' is output directly as a string. 

```python
name = "Alex"
age = 19
marks = 27.56

print(f'I\'m {name}, I am {age} and my subject mark is {marks}')
```

Output:

```bash
I'm Alex, I am 19 and my subject mark is 27.56
```

To insert another type of variable along with the string, the "%" operator can also be used. 

"%" is a prefix to another character, indicating the data type of value we want to insert along with the Python string. 

Below is a list of string formatting specifiers:

<table><tbody><tr><td><strong>Operator</strong></td><td><strong>Description</strong></td></tr><tr><td>%d</td><td>Signed decimal integer</td></tr><tr><td>%u</td><td>Unsigned decimal integer</td></tr><tr><td>%c</td><td>Character</td></tr><tr><td>%s</td><td>String</td></tr><tr><td>%f</td><td>Floating-point real number</td></tr></tbody></table>

Let's try to use all these specifiers to format a string:

```python
name = "Alex"
age = 19
marks = 27.56
my_str = 'I\'m %s,my age is %d and my subject mark is %f' % (name, age, marks)
print(my_str)
```

Output:

```bash
I'm Alex,my age is 19 and my subject mark is 27.560000
```

To learn more about Python String formatting, see our article, [Python Format Strings: Beginner to Expert](https://codesolid.com/python-format-strings/).

## Built-in Python String Functions

Python provides many built-in functions for working with strings. Here are a few of these built-in functions that we'll look at in a moment:

<table><tbody><tr><td><strong>Function</strong></td><td><strong>Description&nbsp;</strong></td></tr><tr><td>len()</td><td>Determines the length of the string</td></tr><tr><td>str()</td><td>Converts the specified value into a string.</td></tr><tr><td>chr()</td><td>Converts an integer to its Unicode character and returns it.</td></tr><tr><td>ord()</td><td>Takes string argument of a single Unicode character and returns its integer Unicode code point value.</td></tr><tr><td>type()</td><td>This function returns the type of an object.</td></tr></tbody></table>

Let us now practice these built-in functions:

```python
# len() function returns a length of the string
my_string = "Incomprehensibilities"
print("The length of the word is", len(my_string))
# str() converts integer to string
itisnot_str = 99

# type() returns the type of the variable
print("\nThe type before conversion -", type(itisnot_str))
itisnot_str = str(itisnot_str)
print("The type after conversion - ", type(itisnot_str))

# chr() converts integers unicode to string character
char = 99
print("\n'char' is", char,", and it's type before -", type(char))
char = chr(char)
print("'char' is", char,", and it's type after -",type(char))


# ord() converts a string to integer
char = "c"
print("\n'char' is", char,", and it's type before -", type(char))
char = ord(char)
print("'char' is", char,", and it's type after -",type(char))
```

Output:

```bash
The length of the word is 21

The type before conversion - <class 'int'>
The type after conversion - <class 'str'>

'char' is 99 , and it's type before - <class 'int'>
'char' is c , and it's type after - <class 'str'>

'char' is c , and it's type before - <class 'str'>
'char' is 99 , and it's type after - <class 'int'>
```

## Built-in Python String Methods

Python offers many built-in methods to perform various operations on a string. This table lists several of the most common methods you may need when working with strings in Python.

<table><tbody><tr><td><strong>Method</strong></td><td><strong>Description&nbsp;</strong></td></tr><tr><td>capitalize()</td><td>Converts first character to capital letter</td></tr><tr><td>lower()</td><td>Returns lowercased string</td></tr><tr><td>upper()</td><td>Returns uppercased string</td></tr><tr><td>encode()</td><td>Returns encoded string of given string</td></tr><tr><td>replace()</td><td>Replaces substring inside</td></tr><tr><td>split()</td><td>Splits string from left</td></tr><tr><td>join()</td><td>Returns a concatenated string</td></tr><tr><td>title()</td><td>Returns a title cased string</td></tr><tr><td>index()</td><td>Returns index of a substring</td></tr></tbody></table>

Let's take a closer look at some of the methods on this list:

```python
# using upper() method
my_str = "hello world"
print("Before:",my_str)
my_str = my_str.upper()
print("After:",my_str,'\n')

# using join() ] method
text = ['Good', 'morning,', 'my', 'world', '!']
print(text)
print(' '.join(text),'\n')

# using title() method
text = 'HELLO, i wanna hAve friends!'
print(text)
print(text.title())
print()

# using replace() method
text = 'good, good morning'
print(text)
print(text.replace('good', 'bad'))
```

Output:

```bash
Before: hello world
After: HELLO WORLD 

['Good', 'morning,', 'my', 'world', '!']
Good morning, my world ! 

HELLO, i wanna hAve friends!
Hello, I Wanna Have Friends!

good, good morning
bad, bad morning
```

## If-Statements with Strings in Python

Let's look at the use of strings in if-statements. 

```python
# This program compares two strings.
# using innput() to get input from the user
password = input('Enter the password: ')
# checking whether entered word is the same with the word 'hello'
if password == 'hello':
    print("Password accepted")
else:
    print("Sorry, that is the wrong password")
```

Output:

```bash
Enter the password:  hello
Password accepted

Enter the password:  world
Sorry, that is the wrong password
```

Note that you can use the `getpass` module to get a password without echoing the input.

## Iterating Through Strings in Python

In Python, you can perform many different types of operations on a string. Let's explore the Python method for iterating through characters in a string.

```python
# Python program to iterate over characters of a string
# using for loop to print dash between each character 
str_name = " HELLO WORLD"
for element in str_name:
    print(element, end = '-')
print("\n")

# iterating using for loop to print each character
str_name = "HELLO WORLD"
for element in range(0, len(str_name)):
    print(str_name[element])
```

Output:

```bash
 -H-E-L-L-O- -W-O-R-L-D-

H
E
L
L
O
 
W
O
R
L
D
```

<table><tbody><tr><td><img src="https://lh3.googleusercontent.com/ccOBFRMLWjkqiLvkGyVHJ7KCbITxheGfAjT6keuGHny_IGXH1siPMCCzF36CVUoYXOwKGC1Hx0dcNFgjLHiSKMJgCSm-D-zOmWnC6ui8PmQobmKy_IKa0qasJ9L5FeL3MWhg6nZvRvPruPbKI7VPIGI" width="177" height="196"></td></tr></tbody></table>

That was the end of our tutorial. Now go through the exercises to support what you have learned.

## Python String Exercises for Beginners

1\. Display this phrase as a title: "hELLo WoRlD!"

```python
txt = "hELLo WoRlD!"
print(txt.title())
```

2\. Change the string "wooow" into uppercase.

```python
x = 'wooow'
x = x.upper()
print(x)
```

3\. Split this string: "Hello World, Good Morning!"

```python
my_str = "Hello World, Good Morning!"
print(my_str.split())
```

4\. Create a program that displays each substring of the following string split at the dashes: "Hello-world-!-Good-morning-!"

```python
my_str = "Hello-world-!-Good-morning-!"
print("Original string:", my_str)
split_str = my_str.split("-")
print("\nDisplaying each substring:\n")
for item in split_str:
    print(item)
```

5\. Return the string without any whitespace at the beginning or the end: "Hello World"

```python
txt = " Hello World "
x = txt.strip()
print(x)
```

6\. Use indexes and slicing to output the first one character, the last one character, everything except the first one character, everything except the last one character, and everything between the first and the fifth characters of the following string: "Hello World"

```python
x = "Hello World"
print("String:", x)

# first one character
first_char = x[:1]
print("First character:", first_char)

# last one character
last_char = x[-1:]
print("Last Character:", last_char)

# Everything except the first one character
except_first = x[1:]
print("Except first char:", except_first)

# everything except the last one character
except_last = x[:-1]
print("Except first char:", except_last)

# everything between first and 5th characters
between = x[0:4]
print("Between 1st and 5th character:", between)
```

7\. Concatenate string and integer objects: 321 and "hello"

```python
n = 321
s = "hello"
string = str(n) + s
print(string)
```

8\. Add one string  to another using the + operator and the join() method: "Hello" and "World"

```python
# using + operator
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3)

# using join()
join_str = "".join((str1, str2))
print(join_str)
```

9\. Сompare these strings: "Hello", "Hello" and "World"

```python
str1 = "Hello"
str2 = "Hello"
str3 = "World"
print("Are str1 and str2 are the same? ", str1 == str2)
print("Are str1 and str3 are the same? ", str1 == str3)
print("Are str2 and str3 are the same? ", str2 == str3)
```

10\. Use replace() method to change the word "World "in "Hello World" to "People".

```python
txt = "Hello World!"
print("Text before: ", txt)
print("Text after:  ", txt.replace("World", "People"))
```

11\. Print "I am \_ years old" using format(). Instead of dashes, insert the value of the variable age = 17.

```python
age = 17
txt = "I am {} years old."
print(txt.format(age))
```

12\. Print the string "'hello'" ten times on separate lines.

```python
my_str = "'hello'\n"
print(my_str*10)
```

13\. Use the `find()` method to find out the index of the character "n" in the Python string "queen"

```python
queen_str = "queen"
print(queen_str.find("n"))
```

14\. Use the escaping sequence operator to print "I answered, "That's my dog!" using single quotes, double quotes, and triple quotes. 

```python
# using single quotes
print('I answered, "That\'s my dog!"')

# using double quotes
print("I answered, \"That\'s my dog!")

# using triple quotes
print('''I answered, "That\'s my dog!"''')
```

15\. Use a for loop to iterate and find the number of letter "L" s in the phrase "HELLO, WORLD". 

```python
count = 0
for letter in "HELLO WORLD":
    if(letter == 'L'):
        count += 1
print("There are ",count,"letters 'L's in the phrase 'HELLO WORLD'")
```

14. Use the escaping sequence operator to print "I answered, "That's my dog!" using single quotes, double quotes, and triple quotes. 

15. Use for loop to iterate and find the number of "l" in the phrase "Hello World". 

## Conclusion

In this tutorial, we've covered in detail what strings are in Python and the different mechanisms for working with them. Including string operators, built-in functions and methods, indexing, and slicing.

Make sure to go through and solve all of these exercises. This will strengthen your theoretical knowledge in practice.

### You May Also Enjoy

- [Python Indexing and Slicing: Complete Tutorial with Hands-On Exercises](https://codesolid.com/python-indexing-slicing-exercises/)
- [How to Use the Pandas Groupby Method](https://codesolid.com/pandas-groupby/)
