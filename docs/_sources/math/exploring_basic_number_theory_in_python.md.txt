---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Exploring Basic Number Theory in Python


As a beginning undergraduate in math, I really appreciate good math writing. That's why when the excellent author of [Introduction to Graph Theory](https://www.amazon.com/Introduction-Graph-Theory-Dover-Mathematics/dp/0486678709), Richard Trudeau, hailed [What Is Mathematics](https://www.amazon.com/What-Mathematics-Elementary-Approach-Methods-ebook/dp/B000SEKHFG) as "one of the best all-around mathematics textbooks since Euclid," I recognized that as my marching orders, so I picked up a copy and began reading.

I found this book worthwhile enough to begin working on the exercises instead of just reading through and "skimming."  The supplement to chapter 1 covered Number Theory, and as soon as I began grappling with these, I wanted to try out some things in Python.  This article is just an attempt to share some of those explorations.  (I'll be doing some "beginner explorations" in this article.  If you're more advanced, you might consider exploring SymPy's [ntheory package](https://docs.sympy.org/latest/modules/ntheory.html).

The discussion in the What is Mathematics section on Number Theory began with the idea of congruence.  Programmers are familiar with the modulus operator, %, which gives the remainder left over after an integer division of the operands.  For example:

```{code-cell} ipython3
10 % 3 == 1
```

In number theory, we say that two numbers, $a$ and $b$ are congruent with respect to a given modulus, $d$, if they give the same remainder. We write this as:

$$ a \equiv b \space (mod \space d) $$

For example, given a modulus of 3, we can see that both 7 and 10 divided by three both leave a remainder of 1, so we can say:

$$ 10 \equiv 7 \space (mod \space 3) $$

If this isn't obvious enough by inspection, we can test it trivially in Python:

```{code-cell} ipython3
def is_congruent(a, b, modulus):
    """Test whether two numbers, a and b, are congruent for the given modulus"""
    return a % modulus == b % modulus

print(is_congruent(7, 10, 3))  # OK, 1 == 1
print(is_congruent(7, 10, 4))  # NO!  7 mod 4 is 3, while 10 mod 4 is 2!
```

Many interesting properties apply to the congruence relation between numbers, which are similar to properties that apply to equivalence.

_What Is Mathematics_ goes through these properties, so I won't reproduce them here, but they generate many interesting results.  For example, congruent numbers can be added and multiplied; for any given modulus, we can construct tables to understand the results. We have some day-to-day experience with doing this in mod 12, where we know that if it's 10:00 AM now, five hours from now, it won't be 15:00 (unless you're in the military).  Instead, it will be 3 PM because $15 \bmod 12 = 3$.

To give an example that the authors didn't discuss, you may have learned in school that if the digits of a number add up to nine, the number is evenly divisible by nine.  Thus, 27 is divisible by nine because $2 + 7 = 9$. Because we're dealing with base 10 (where the digit choices are 0-9), the remainder after division by 9 is the same as you get from the sum of a number's digits:

For example, $139 \bmod 9 = 4$, and $1 + 3 + 9 = 13$.  We can see that 13 divided by nine gives a remainder of four, which we can also obtain by a second digit sum, i.e., $1 + 3 = 4$

+++

## Solving a problem by hand and checking it in SymPy

One of the exercises in *What is Mathematics* was this:  "To what number between 0 and 4 inclusive is the sum of $1 + 2^2 + 2^3 + ... 2^{18}$ congruent (mod 5)?"

In my first attempt to solve this, I tried to find a pattern in the first few terms to see if it was any help:

Here's the table I made for the modulus of those terms:

|Term|modulus 5|
|----|---------|
|1|1|
|2|2|
|4|4|
|8|3|
|16|1|
|32|2|
|64|4|
|128|3|

Looking at the right-hand column, we see that the modulus terms repeat in groups of 4, as follows:  (1, 2, 4, 3).

Since the four repeating terms add up to 10, and $10 \equiv 0 \space (\bmod 5)$, and since $2^{18}$ is the term we're concerned with, and since the series is based on zero rather than one, we'll have three terms left over at the end.  I therefore reasoned that the second modulus of the sequence we showed above should give us the answer:  $\boxed{2}$.  This will turn out to be wrong, but bear with me.

To check the answer in Python, I thought it was a great time to figure out how summations worked in SymPy. In general, SymPy is my go-to tool for checking results in Calculus. Now, for this problem, we'll see in a minute that that approach is a bit overengineered since Python will also get us there directly, but let's try SymPy first.

The series in the exercise can also be written as:

$\sum\limits_{i=0}^{18} 2^i$

Checking the documentation for the summation function in SymPy, we learn we can translate that into Python as `summation(2**i, (i, 0, 18))`, i.e., `summation(function, (variable, start, stop))`.

```{code-cell} ipython3
import sympy as sp
i = sp.symbols('i', integer=True)
result = sp.summation(2**i, (i, 0, 18))
print(result)
```

Since I've been working with congruences today, it's obvious to me that 524287 mod 5 should be 2 (because 7 mod 5 is 2), but let's show it in Python in case its not obvious to you:

```{code-cell} ipython3
print(result % 5)
```

(As I mentioned, I wanted to try out the summation feature of Sympy, but we didn't need SymPy otherwise. We can achieve the same result with the Python runtime library quite easily, as shown below).

```{code-cell} ipython3
result = sum([2**x for x in range(0, 19)])
print(result)
```

In addition to dealing with infinite series, SymPy's summation function also has the advantage of using the full closed range we're dealing with rather than the half-open range, $[0, 19)$.

Whether we use SymPy or a simple list comprehension, the answer we arrived at by grouping terms seems to check out, but let's verify that it's not a fluke. If it's not, the next term in the sequence should match up with the next term in our group of four.  That is, if we're not just lucky, we should find $2^{19} \equiv 4 \bmod 5$

In other words, the following should return the number four:

```{code-cell} ipython3
sp.summation(2**i, (i, 0, 19)) % 5
```

Well, OK, that's clearly not a four.  So, up to this point, I've learned I was right about $2^{18}$ but not for $2^{19}$, so by dumb luck, I had arrived at the right answer for $2^{18}$ with the wrong reasoning.

Fortunately, because I was summing the terms now to check my answer, it quickly occurred to me that the trouble with my algorithm might be that I was looking for a pattern in the individual terms rather than the series.  I decided to write a bit of code to see if I could detect a pattern in the sum of the terms instead.

```{code-cell} ipython3
for x in range(0, 10):
    print(sp.summation(2**i, (i, 0, x)) %5)
```

That's better.  Here the fourth term in the repeating sequence is 0, not 4.  This agrees with the result we got for $2^{19}$.  Let's do one final (inductive) check to make sure the algorithm seems to hold true for other terms as the series grows.  To do this we can run the summation, then see if the summation modulo 5 (what we call below the actual value) matches what we expect to see based on a repeated pattern (expected):

```{code-cell} ipython3
pattern = [1,3,2,0]

terms_to_check = 100
passed = True

print("Testing up to 2^{0}".format(terms_to_check))
for x in range(0, terms_to_check):
    # Our expected value for the summation of the series:
    actual = sp.summation(2**i, (i, 0, x)) % 5

    # Try matching the actual modulus value against our pattern using our "algorithm":
    index = x % len(pattern)
    expected = pattern[index]

    # Check
    if actual != expected:
        passed = False

print("Test passed?", passed)
```

This is just one of the explorations my reading of *What Is Mathematics* has suggested so far.  It's such a rich motherlode of math gems that I could easily spend a year playing with the ideas I'm learning from this one book.  Since I don't have time to do that right at the moment with my university math courses, I'll leave this one little article as yet another example of how Python helps me save myself from those many math errors I make either in calculation steps or in fundamental concepts.

```{code-cell} ipython3

```
