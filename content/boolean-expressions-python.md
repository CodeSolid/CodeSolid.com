---
title: "Boolean Expressions in Python: Beginner to Expert"
date: "2022-04-14"
categories: 
  - "python-for-beginners-posts"
coverImage: "yes-no-scaled.jpg"
---

We often talk about two different kinds of control flow in programming courses: branching and looping. A program branches when it goes down one path or another based on a condition. Both of these types of control flow are essential features of the vast majority of programming languages.

We discuss some common ways to loop in detail in our article [Python Lists for Beginners](https://codesolid.com/python-lists/). Here we want to concern ourselves with basic branching, a simple but fundamental concept that you'll quickly master with just a little practice. Setting aside some advanced techniques for the moment, at the heart of most branching statements you'll find a Boolean expression.

A Boolean expression in Python is a combination of values or values and functions that can be interpreted by the Python compiler to return a value that is either true or false. It often consists of at least two terms separated by a comparison operator, such as `"price > 0`". However, it can also be any expression or function call that returns a boolean result, such as `"'error' in msg`".

## A Simple Boolean Example in Python

Let's take a simple example of determining whether a number is odd or even. Perhaps we want to print a formatted string including "odd" if a number is odd and "even" if it's even. We know that a number that's evenly divisible by two is even -- that is to say, the remainder of the division will be zero. We use the modulo operator, "%," to calculate the remainder of a division:

```python
print(4 % 2)
print(5 % 2)
print(11 % 3)
```

Output:

```bash
0
1
2
```

We see that the remainder of 4 modulo 2 is 0, which tells us it divides evenly or is an even number. 5 % 2 does not divide evenly, so this does not return a zero. We show that you can use other numbers with the modulo operator on line three.

So now we know how to tell if a number is odd or even. However before writing the code for it, we need to take a fun side trip to the hardware store to pick up some other tools for the job. I promise we'll come back and build the code, but it'll be easier if we pack our toolkit first.

## Boolean Constants and Expressions in Python

The word Boolean is capitalized out of deference to Charles Boole, a 19th-century mathematician and philosopher who wanted to apply mathematical principles to logic. He worked out precise rules for expressions that are either entirely true or completely false. In Python, there are two Boolean constants that are capitalized: True and False. It's possible and acceptable to set a variable to one of these values, but what's even more common than Boolean variables are Boolean expressions, which are any expression that returns a True or False value. For example:

```python
# Is three greater than two?
print(3 > 2)

# Is the number of characters in the string "Hello" equal to one?
print(len("Hello") == 1)

# Is 5 equal to 3 + 2?
print(5 == 3 + 2)

# Is four greater than or equal to nine?
print(2 + 2 >= 9)

# Is seven not equal to twelve?
print(7 != 12)
```

Output:

```bash
True
False
True
False
True
```

Note that the double equals of a Boolean expression (`==`) are different from the single equals sign that we used to assign a value to a variable:

```python
# Assign a string variable to message.
message = "Hello, world!"

# Test for equality.  This returns True.
message == "Hello, world!"
```

## Python Comparison Operators

Frequently, Boolean expressions are expressions that use comparison operators. Another way to describe Boolean expressions in Python (or other languages) is to say that they are expressions that make a comparison. We've seen a lot of this already in our example, but here are the Python comparison operators and what they mean.

<table><tbody><tr><td><strong>Operator</strong></td><td><strong>How to Read It</strong></td></tr><tr><td>x == y</td><td>x equals y</td></tr><tr><td>x != y</td><td>x does not equal y, x is not equal to y</td></tr><tr><td>x &gt;= y</td><td>x is greater than or equal to y</td></tr><tr><td>x &lt;= y</td><td>x is less than or equal to y</td></tr></tbody></table>

## Negation Using Not

Just like in English, we can negate any boolean expression by using the keyword `not` in front of it. The keyword `not` is like a polarity reverser -- it makes a true expression false and a false expression true.

```python
print(9 == 5 + 4) # True
print(not 9 == 5 + 4) # False
print(not True) # False
print(not False) # True
```

## If and Else In Python

Now that we have some basic Boolean tools to work with, we're ready to return to our "odd" vs. "even" example and start doing some branching logic. We use the `if` keyword followed by a Boolean expression and a colon; then we indent the following one or more lines that will run only `if` the expression evaluates to true. (Most Python editors will seamlessly convert the tab key to four spaces for us, so I always indent using the tab key).

We can then optionally use `else` and a colon followed by one or more indented lines, and that code will be executed if the Boolean expression evaluates to false.

```python
my_number = 24
if my_number % 2 == 0: 
    print(my_number, "is even.")
else:
    print(my_number, "is odd.")
```

## Handling More Than Two Cases in Python: Elif

We can run code conditionally with just an `if` clause. The `else` clause is optional -- we may not do anything if the Boolean checked by else is `False`. Another optional clause that can be useful in cases where there are more than two possibilities is an `elif` clause, which combines "`else`" and "`if`". As always, it's easiest to show with an example.

I was going to write an example where we sort people into heights based on short, average, and tall, but out of sensitivity to those who might have body issues, I decided to work with potatoes instead. A quick search uncovered a reasonable example where `elif` might be used:

> Potatoes sold at grocery stores are typically: size A potatoes (2.5 inches in diameter) size B potatoes (1.5 to 2.25 inches in diameter) size C potatoes (less than 1.5 inches in diameter); we've seen C-sized potatoes described as the smallest ones available.
> 
> https://www.chefs-garden.com/blog/november-2017/insights-into-potato-sizes-and-the-beauty-of-small

Here's how we could build and test a basic potato sorter.

```
potato_size_inches = 1.6

if potato_size_inches >= 2.5:
    size = "A"
elif potato_size_inches >= 1.5 and potato_size_inches <= 2.25:
    size = "B"
elif potato_size_inches < 1.5:
   size = "C"
else: 
    size = "UNKNOWN"

print(size)
```

Output:

```
B
```

I'm no potato expert, so I can't tell you what's supposed to become of potatoes between 2.25 inches and 2.5 inches. However, our code handles that case for now by assigning the label "UNKNOWN".

## Equality Checks and Checking for None

In the last section, we used `==` and `!=` to say that two numbers are equal or not equal, respectively. Unlike many of the other operators we've seen, these operators can be used to compare numbers and various other Python types.

For example, using "`==`", we can check that two lists contain the same elements or that two strings are identical. In the string case, by the way, the comparison is case-sensitive. To do a case insensitive comparison, we can convert both strings to the same case and then make the comparison:

```python
s1 = "Hello"
s2 = "HELLO"
print(s1 == s2)
print(s1.lower() == s2.lower())
```

Output:

```bash
False
True
```

As consistent as Python is in general, there is one case in which "`==`" and "`!=`" are not recommended, and that's the case of checking for `None`. Python's `None` keyword is used when we want to declare a variable but not set it to a value just yet. `None` is a special type that represents the absence of a value. To test for "None", the recommended procedure is to use "`is"` and "`is not`" instead of "`==`" and "`!=`".

```python
some_variable = None
some_number = 0
some_string = ""

print(some_variable is None) # True
print(some_number is None) # False
print(some_number is not None) # True
print(some_string is None) # False

some_string = "Hello"
print(some_string is None) # False
```

Output:

```bash
True
False
True
False
False
```

The reason for this suggestion is that there is only one `None` object in Python, so we're testing that a variable is set to this one `None` object. Another reason to do it is simply to avoid editor warnings.

## What Are Compound Boolean Expressions in Python?

So far in our discussion, we've been mainly dealing with simple Boolean expressions. However, both in code and in real life, it's often the case that we want to make decisions based on more than one factor. We take an umbrella with us if it's raining or cloudy. That is to say, we'll take this action if either thing is true -- they don't have to both be true. Other times we need both things to be true to make a decision. We'll go out with friends after work if we have time and money. Finally, we often want to do something if something is **not** true.

Because Python was designed with simplicity in mind, the English words in bold in the last paragraph are also Python keywords we can use to create compound Boolean expressions. That said, we've already discussed the behavior of "`not`" in an earlier section, so let's focus on the behavior of "`and`" and "`or`".

The way `"and`" and "`or"` work is that "`and`" evaluates to true if and only if both expressions that it joins are true. On the other hand, "`or`" returns true if at least one of the expressions that it joins is true.  
  
For example, here's a program where one of the expressions (`time_available_minutes > 120`) is true. Because we're using "`and`" and not "`or`", the compound expression evaluates to false, so the else clause is executed.

```python
money_available_dollars = 3
time_avaialble_minutes = 180

if money_available_dollars > 10 and time_available_minutes > 120:
    print("Go out with friends")
else:
    print("Stay home")
```

Output:

```bash
Stay home
```

Since one of the expressions is true, changing the "`and`" to "`or`" in the example above changes the output to "Go out with friends." On the other hand, if both expressions are false, then the "`else`" clause will run either way.

Both "`and`" and "`or`" are said to be "short-circuit expressions". What this means is that for "`and`", if the first expression (on the left side of `"and`") is false, the right-hand side is never evaluated. The Python compiler "knows" that it can't get a `True` result for "`and`" if the first expression is `False`, so it skips it. Therefore, if each of these sides is a function that returns a Boolean result, if the first returns False, the second one will never be executed! For the "`or`" keyword, the right-hand side is not evaluated if the left-hand side evaluates to "True". In this case, we already know that the result is "True", so the right-hand side is ignored.

Some students find it helpful to construct a truth table when learning about Boolean values. Results marked with a \* are those results that are the result of short-circuit expressions.

## A Truth Table for Python Boolean Expressions

<table><tbody><tr><td>Expression 1</td><td>Connector</td><td>Expression 2</td><td>Result</td></tr><tr><td>True</td><td>and</td><td>True</td><td>True</td></tr><tr><td>False</td><td>and</td><td>True</td><td>False *</td></tr><tr><td>True</td><td>and</td><td>False</td><td>False</td></tr><tr><td>False</td><td>and</td><td>False</td><td>False *</td></tr><tr><td>True</td><td>or</td><td>True</td><td>True *</td></tr><tr><td>False</td><td>or</td><td>True</td><td>True</td></tr><tr><td>True</td><td>or</td><td>False</td><td>True *</td></tr><tr><td>False</td><td>or</td><td>False</td><td>False</td></tr></tbody></table>

## What Are the Precedence Rules For Python Boolean Expressions?

When reading or writing Boolean expressions, it's important to understand the order in which the expression will be evaluated. The Python documentation lists the [precedence rules](https://docs.python.org/3/reference/expressions.html?highlight=precedence#operator-precedence) for the entire language, but here our focus is on Boolean expressions and the related issue of comparison operators.

As the name suggests, Python precedence rules determine which operators are evaluated first. Because of precedence rules, we're allowed allow us to combine expressions in a way that makes sense. Expressions are chained using operators with higher precedence, using component parts that have operators with lower precedence.

We've been relying on one important rule in our discussion of compound boolean expressions. The comparison operators, `==`, `!=`, `>=`, `is`, `is not`, etc. all have higher precedence than `and`, `or` or `not`. Here is the precedence order, from highest to lowest:

- Comparison operators
- not
- and
- or
- if/else
- ...
- Assignment

Because comparison operators are evaluated first, for example, we're able to evaluate expressions like this:

```python
result = 3 > 5 or 9 > 2
```

Because comparison operators have the highest precedence, Python first evaluates `3 > 5` to `False` and `9 > 2` to `True`.

So at this stage, the evaluation looks like this internally:

```python
result = False or True
```

At this stage, "`or`" has higher precedence than assignment, so it gets evaluated, leaving us with:

```
result = True
```

In the case of "not", remember that it has higher precedence than "`and`" or "`or`", so in this expression:

```
not False or False
```

`not` gets applied to `False` first not to `False` or `False`. (In this case, the result is the same, but that won't always be true).

Another key precedence rule to remember is that "`and`" comes before "`or"`. In the following operation, changing the precedence changes the result:

```python
False and False or True
```

This works out to `True` because "`and`" is evaluated first, like this: `(False and False) or True`  
If we evaluate it the other way, "`False and (True or False)`", the result would be False. In fact, we can use parentheses like this in Python if that's what we mean to do.

```python
print(False and False or True)
print(False and (True or False))
```

Output:

```bash
True
False
```

I have found that the best way to understand the precedence rules in a language is not by memorizing lists of them, but by hands-on practice. Remember that you can always change the order of precedence to be whatever you really mean to do using parentheses

## Python If/Else and Booleans: Examples and Practice Questions

Note that the following practice questions are meant to challenge you based on the information in the article. Do your best to try these exercises without running them in Python.

Of course, as with everything else in programming, there's no substitute for doing lots of hands-on practice, so you might want to try out similar code in Python once you've finished with these example questions.

Online Exercises

[Download Exercises](https://github.com/CodeSolid/CodeSolid.github.io/blob/main/booksource/exercises/BooleanExpressionsExercises.ipynb)

Links to the solutions are after the article. Good luck!

**1.** The following Python code contains one or more errors. How would you correct them?

```python
water_level = 5

if water_level > 3
    print("Open flood gates")
else
    print("Normal operations")
```

Which of the following is not a boolean expression, and why?

1. 5 < 2
2. 2 < 3
3. 3.5 <= 7
4. 3 = 7
5. my\_variable is not None

3. What does the following print?

```python
noise_level = 2
heat_output_percent = 98

if noise_level > 4 or heat_output_percent < 95:
    print("Call technician")
else:
    print("Normal operation")
```

4. What does the following print?

```python
to_be = True

print(to_be and not to_be)
print(to_be or not to_be)
```

5. What does the following print?

```python
water_level = 3
time_of_day = "PM"
heat_ouput_percent = 75

print(water_level > 5 and time_of_day == "PM" or heat_output_percent < 90)
```

6. The following code works OK, but what if anything is wrong with it?

```python
if (3 > 10) or (4.5 > 9):
    print("Gotcha!")
```

7. How might the following code be improved?

```python
rebounds = None

if rebounds != None:
    print("Got some rebounds!")
else:
    print("No rebounds")
```

8. In the following code, which expressions are evaluated?

```python
light_level = 10
decibel_level = 30
result = decibel_level > 50 or light_level == 10
```

A) decibel\_level > 50  
B) light\_level == 10  
C) Both A and B  
D) Neither A nor B

9. Which of the following statements is false? There may be more than one.

A) An else clause must be preceded by an if clause.
B) An if clause must be followed by an else clause.
C) Usually, a Boolean expression contains one or more comparison operations.
D) Boolean expressions can appear outside of an if statement.
E) Boolean expressions must include a Boolean literal (i.e. one of the the keywords "True" or "False")

10. What is the error in the following code? How would you fix it?

```
water_level = 5

if water_level and water_level < 3:
    print("Normal operations")
else if water_level >= 3 and water_level <= 4.5:
    print("Call City Manager")
else:
    print("Open flood gates and call City Manager")
```

[Solutions to Exercises](https://colab.research.google.com/github/CodeSolid/CodeSolid.github.io/blob/main/booksource/solutions/BooleanExpressionsExercises.ipynb)

## You May Also Like

[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)

[Python Format Strings: Beginner to Expert](https://codesolid.com/python-format-strings/)
