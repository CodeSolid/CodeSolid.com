---
title: "NumPy Examples --  Practice Questions Make You an Expert"
date: "2022-02-16"
categories: 
  - "python-practice"
tags: 
  - "featured"
coverImage: "numpy.png"
---

Have you learned some NumPy, but now your learning has stalled because you don't have any practice questions or exercises to review what you've learned?

This practice set of forty-five NumPy examples features NumPy questions in varying degrees of difficulty. Some are very common examples of NumPy arrays, others get into some more advanced features. The exercises to challenge you are all in this article, but you'll also find full solutions so you can compare your answers.

This example set features several questions that I worked on recently to review and improve my knowledge of NumPy -- the excellent, high-performance n-dimensional array library that is a core pillar of the Python data science stack. These questions and exercises range from those that I could get right or code off the top of my head to challenging questions that I had no idea about when I worked on them (or made mistakes on the first time I tried). So don't feel bad if some of these are hard, or you can't finish all of them. That said, they will be simpler if you have some background in NumPy.

If you need some materials for making a start on NumPy and Python data science, see our article, [How to Practice Python: Data Science and Pandas](https://codesolid.com/how-to-practice-python-data-science-and-pandas/).

## Finding the Solutions

For those I didn't know the answer to, I used a combination of Google and [The NumPy API Reference](https://numpy.org/doc/stable/reference/index.html) to try to work out the solution, so yes, you should research these if you want to practice! The exercises selected here cover many of the features of NumPy, but it's not meant to be exhaustive. For example, we don't cover the linear algebra features in `numpy.linalg`.

In the exercises that follow, any unqualified references to an "array" mean a NumPy array, not a native Python array. References to "np" refer to the NumPy package in the usual way it is aliased: "`import numpy as np`". Good luck, and let me know how it goes!

Update: We've added a solution dropdown to each question so you don't need to switch back and forth between the exercises and the solution set. That said, it's still a good idea to try to recall the answer or look in the NumPy API reference, and use the solution links as a last resort!

## Creating Simple One-Dimensional NumPy Arrays

NumPy has several functions that will return an n-Dimensional array. These exercises ask you to recall these functions to create arrays with only one dimension.

1. Using a NumPy function, how would you create a one-dimensional NumPy array of the numbers from 10 to 100, counting by 10?

Show Solution

```python
np.arange(10, 110, 10)

# Creates
# array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
```

2. How could you create the same NumPy array using a Python range and a list?

Show Solution

```python
np.array([i for i in range(10, 110, 10)])

# Creates
# array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])
```

3. What happens if you pass no arguments to the np.array()?  
    

Show Solution

It raises a TypeError exception, complaining that the required argument, 'object" is missing. NumPy arrays can be constructed from an iterable, as we've shown. If passed a scalar such as an integer, they'll create a "zero-dimensional array" -- that is, an array with only one element.

4. How might you create a NumPy array of the capital letters, A-Z?

Show Solution

```python
from string import ascii_uppercase
np.array(list(ascii_uppercase))

# Creates:
# array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#       'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
#      dtype='<U1')

# An alternate but more verbose solution is:
np.array([chr(i) for i in range(ord('A'), ord('Z') + 1)])
```

The next few questions deal with how to initialize NumPy arrays.

5. How would you create a ten-element NumPy array object of all zeros?

Show Solution

```python
print(np.zeros(10))
# Displays [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

6. How would you find the data type given in #4.

8. What is the data type for #4?

Show Solution (Numbers 6 and 7):

```python
# You can find the data type of a NumPy array using the dtype attribute.  
# In the case of np.zeros and similar functions, the data type is dtype('float64')
# For example

df = np.zeros(10)
df.dtype

# Displays dtype('float64')  in Jupyter, for example.
```

8. What function would return the same number of elements, but of all ones?

Show Solution

```python
print(np.ones(10))
# Displays [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

9. How could you create a ten-element array of random integers between 1 and 5 (inclusive)?

Show Solution

```python
np.random.randint(1, 6, 10)

# Sample output:
# array([1, 1, 3, 3, 4, 4, 1, 5, 3, 4])
```

10. How can you create a normal distribution of 10 numbers, centered on 5?

Show Solution

```python
# How can you create a normal distribution of 10 numbers, centered on 5? 
# Note, the 1 in center represents mu, size of STD DEV

np.random.normal(5, 1, 10)

# Example output:
# array([2.53449952, 5.65468816, 5.82071586, 3.86682187, 4.21763168,
#       5.80572274, 6.97562422, 4.58591293, 5.44201627, 4.80652277])
```

11. What code would create an array of 10 random numbers between zero and one?

Show Solution

```python
np.random.rand(10)

# Example output:
# array([0.83698711, 0.24264316, 0.30675551, 0.63795295, 0.87011717,
#       0.27054306, 0.65159876, 0.49426323, 0.68323172, 0.69278983])
```

## Creating and Using Multidimensional Arrays

In this section, we move past one-dimensional arrays. As a reminder, many of the same functions that we used to create one-dimensional arrays select either a single scalar value for the number of elements to create or a tuple representing the shape of the array in higher dimensions.

12. Consider the code: `np.ones((3,5))`. Does this A) create an array of three arrays containing five elements each or B) create an array of five arrays containing three elements each?

Show Solution

It creates an array of three arrays with five values each. For two-dimensional arrays in NumPy and Pandas, I always remember the mnemonic: "Radio Controlled" or "Royal Crown" (cola). Rows come first, then columns. Here's how it appears in Jupyter Lab:

```python
array([[0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0.]])
```

13. Consider an array named "`myarray`" that is displayed as in the block below. What value does the code `myarray[1,2]` return? A) 10 B) 7.

```python
# myarray:

array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

Show Solution

It displays a 7. Again, the "row" value is indexed first, then the "column" value. (Or the outer array and the inner array, if you prefer to think of it that way. Since the indexes are zero-based, myarray\[1,2\] displays a value from the second row, third column, or 7.

14. Given `myarray` as shown above, what is the value of `myarray.ndim`?

Show Solution

`myarray.ndim` has a value of 2. The `ndim` property tracks the number of dimensions for an array.

15. An array of three arrays of four elements each like this has twelve elements, of course. How could you create a new array consisting of two arrays of six elements each?

Show Solution

Call the `reshape` method on the array with the arguments `3, 4`. For example:

```python
original_array = np.arange(1, 13)
new_array = original_array.reshape(3, 4)
print(repr(new_array))
```

```bash
# Output:

array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
```

16. Given `new_array` from the last exercise, and the code `x = new_array`, you run the code:

```
x = new_array
x[0,0] = 42
print (x[0,0])
print(new_array[0,0])
```

Following this code, what is displayed?

Show Solution

```bash
42
42
```

As you might expect from working with Python lists and other mutable objects, assigning a NumPy array to a new variable simply creates a reference to the original array, not a copy of it. If you need the original array to be unchanged, use:

```python
x = new_array.copy()
x[0,0] = 42
print (x[0,0])
print(new_array[0,0])

# Displays:
# 42
# 1
```

17. How could you create a two-dimensional, 3 x 4 array (three arrays of four elements each) with random numbers from 1 to 10?

Show Solution

```python
values = np.random.randint(1, 11, (3,4))
print(values)
```

```bash
# Output varies:

[[ 4  6  6  9]
 [ 7  4 10  5]
 [ 1  6  4 10]]
```

18. How could you create an array of the same size and shape as #17, filled with 64-bit integer zeros?

Show Solution

```python
zeros = np.zeros(dtype=np.int64, shape=(3,4))
print(zeros)
```

```bash
# Output:

[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
```

19. Given this code:

```python
z_list = [z for z in range(0,5)]
y_list = [z_list for y in range(0,4)]
x_list = [y_list for x in range(0,3)]

x_array = np.array(x_list)
```

What would the value of `x_array.shape` be?

Show Solution

The key to this solution is understanding that the first line, z\_list, is a list comprehension creating a one-dimensional list. In line 2, y\_list creates a two-dimensional list with four nested lists of five-element lists. By line 3, we now have three two-dimensional lists, for a three-dimensional list. Passing that to the NumPy array constructor gives us a three-dimensional NumPy array with the shape. So printing x\_array.shape would show a tuple with the size in each dimension, or:

`(3, 4, 5)`

20. Given `x_array` from #19, what is the value for `x_array.ndim`?

Show Solution

Well, the last answer pretty much tilted our hand here if you know that `ndim` gives the number of dimensions. `x_array.ndim` is 3.

21. Given an array, named `"arr`", that looks like:

```python
[[0, 1, 2],
       [3, 4, 5]]
```

How could you display an array that looks like:

```python
[[0, 3],
       [1, 4],
       [2, 5]]
```

Show Solution

This code will display the array with the dimensions swapped.

```
print(arr.transpose())
```

Note that transpose() returns a view (shallow copy) of the array. If you need to modify it without impacting the original array, use `arr.transpose().copy()`.

## Indexing and Slicing Two-Dimensional Arrays

NumPy arrays support indexing and slicing across using scalars and tuples. For questions 22-28, use the following array, assigned to the variable, four\_by\_five. Assume that the rows are the "outer" arrays of five elements each and that the nth element within all the rows is a column:

```python
# four_by_five:

array([[ 1,  2,  3,  4,  5],
       [ 6,  7,  8,  9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]])
```

22. Write a statement that prints the first row. (It will be a five-element array).

Show Solution

```python
print(four_by_five[0])

# Output:
# [1 2 3 4 5]
```

23. Write an expression to print the last row. (It will be a five-element array).

Show Solution

```python
print(four_by_five[-1])

# Output:
# array([16, 17, 18, 19, 20])
```

24. What does `print(four_by_five[2,3])` display?

Show Solution

```python
print(four_by_five[2,3])

# Output:
14
```

25. What does `print(four_by_five[3,2])` display?

Show Solution

```python
print(four_by_five[2,3])

# Output:
14
```

26. How could you display the first column? It will be a (four-element array ending with 16.)

Show Solution

```python
print(four_by_five[:,0])

# Output:
[ 1  6 11 16]
```

The second argument to the slice expression is a zero, giving us the first column. The first argument is another slice expression representing the elements we want out of the column, so the colon here returns all the elements.

27. What does print(four\_by\_five\[:, 3:\]) display?

Show Solution

```python
print(four_by_five[:, 3:])
```

Output:

```bash
[[ 4  5]
 [ 9 10]
 [14 15]
 [19 20]]
```

Here we have a slice in both positions. In the first argument, we're saying "return all rows". In the second element, we're selecting only the columns at index 3 and later, that is, the last two columns.

27. Write an expression to return the last two columns of the middle two rows.

Show Solution

```python
print(four_by_five[1:3, 3:])
```

Output:

```bash
[[ 9 10]
 [14 15]]
```

## Vectorized Operations

Vectorized operations are implemented in NumPy so that many mathematical and logical functions operate across the whole array. These vectorized operations act on every array element without writing a Python loop. The most common ways to do this are to combine the array with itself, with an array of the same shape, or with a scalar value.

To keep it simple, let's use a small one-dimensional array to begin. For exercises #28-36, use the one-dimensional array shown below:

```python
one_dim = np.arange(1,6)
one_dim

# Output
array([ 1,  2,  3,  4,  5])
```

29. What would be displayed by `print(one_dim * 2)`

Show Solution

Output:

Again, many NumPy array operations are vectorized, including simple math operations. Therefore, multiplying a NumPy array by a scalar value behaves very differently than doing the same thing to a Python list.

For a NumPy array, each element is multiplied by two, so one\_dim given that one\_dim is set to `[1, 2, 3, 4, 5]`, then:

```python
print(one_dim * 2)

# Output:
# [ 2  4  6  8 10]
```

29. What would be returned by this expression: `one_dim + np.arange(5, 0, -1)` ?

Show Solution

Output:

Here we're creating a new array with a descending range: \[5, 4, 3, 2, 1\] and adding it to \[1, 2, 3, 4, 5\], so we get an array with the values \[6, 6, 6, 6, 6\].

30. How many zeros are in the array returned by `one_dim - one_dim` ?

Show Solution

Five. Subtracting an array from itself returns an array of the same length with all values set to zero. (Assuming all elements are numbers > 1).

31. What is the result of `one_dim > 2` ?

Show Solution

Using a comparison operator on a NumPy array vectorizes the comparison, so what's returned is an array of booleans that satisfy the comparison. Since for this expression the last three values satisfy the comparison, the array returned is:

```bash
array([False, False,  True,  True,  True])
```

32. For NumPy arrays, logical operations are done with the operators "`&`" and "`|`", rather than the usual Python "and" and "or". Given that, what would be the result of this expression?  
    `(one_dim > 4) | (one_dim == 1)`

Show Solution

Once again, we're looking for the results that satisfy the comparison, so the numbers that are either greater than four or equal to one. This matches the first and last element of the array, so our vectorized answer is:

```bash
array([ True, False, False, False,  True])
```

33. What is the result of this expression:  
    `-one_dim`

Show Solution

Here again, the negation operator is vectorized over the whole NumPy array, giving us:

```bash
array([-1, -2, -3, -4, -5])
```

34. `np.absolute` take the absolute value of each element. Given that, what would the result be of the following expression:  
      
    `np.absolute(-(one_dim[3:])`

Show Solution

Here we're not concerned with whether the value of the target array is positive or negative, `np.absolute` gets us an absolute magnitude. But we also need to evaluate the slice expression here, which returns the values from index 3 to the end of the array. So the correct value for this exercise is:

```bash
array([4, 5])
```

35. This exercise shows the use of one of NumPy's sequence functions, which operate on the whole array rather than per element. What is returned by `one_dim.sum()` ?

Show Solution

See, not all of these questions are brainbusters -- good for you if you guessed that `numpy.array.sum` simply adds up all the values in the array, returning 15. The sum function in Python does the same thing for lists, by the way:

```bash
numbers = [x for x in range(1,6)]
print(sum(numbers))
# Output 15
```

For a list or array of this size, the difference hardly matters, but being implemented in C, NumPy's performance gains really make a difference on large arrays or matrices.

36. Break out those pictures of the unit circle for this one, for some trigonometry so simple an ex-history major can do it -- well at least I can on a good day.  
      
    As background, we can round numbers to a decimal precision using `np.around(arr, num_decimals)`, and get the sine of an angle (in radians) using `np.sin`. So with that, given the following array of angles in radians:  
      
    `arr = np.array([0., .5, 1.0, 1.5, 2.0]) * np.pi`  
      
    What does the following display:  
      
    `print(np.int32(np.sin(arr)))`  
      
    Note: the fact that we're able to cast to an integer is a bit of a hint, but otherwise, we can end up with some pretty surprising rounding errors!

Show Solution

OK, this one was a bit more challenging, but if you happened to remember (or look up), that on the unit circle the sin function represents the vertical (y-axis) component of the angle, most of it falls into place. At pi \* 0, we're at the point (1,0), at pi \*.5 (one-half pi), we're at the point (0, 1), and so forth. So our output ends up looking like this:

\[ 0  1  0 -1  0\]

37. For the defined above in #36, what are the values for:  
      
    `np.around(np.cos(arr), 0)`

Show Solution

If #36 was concerned with the y-axis component of the points going once around the unit circle every 90 degrees, this one asked you for the x-axis component (the cosine). The solution is:

\[ 1  0 -1  0  1\]

## Working with Files

38. You're asked to save the following two arrays as is to a file, "data.npz". The arrays should be named as they are here in the file. How could you do it?

```python
people = np.array(["John", "Jennifer", "Helen", "Miryam"])
languages = np.array([2, 2, 1, 1])
```

Show Solution

```python
np.savez("data.npz", people=people, languages=languages)
```

39. Assuming you saved the file, "data.npz", in #38, how could you reload the arrays into two new variables: `people2` and `languages2`?

Show Solution

```python
arrays = np.load("data.npz")
people2 = arrays["people"]
languages2 = arrays["languages"]
print(people2)
print(languages2)

# Output
# ['John' 'Jenniffer' 'Helen' 'Miryam']
# [2 2 1 1]
```

40. Given  
      
    `arr = np.arange(1,13).reshape(3,4)`  
      
    How could you save it to a CSV file, "myrray.csv".  
      
    

Show Solution

```python
arr = np.arange(1,13).reshape(3,4)
np.savetxt("myarray.csv", arr, delimiter=",")
```

41. Given the CSV file saved in #40, how could you load it back into a variable, `arr2`?

Show Solution

```python
arr2 = np.loadtxt("myarray.csv", delimiter=",")
```

## NumPy String Functions

Next, let's relax a little with some simple character-oriented (string) functions, from the `np.char` package. Some of these are simply vectorized (element-wise) versions of the Python standard library functions.

Proving that every Python blog gets around to the Lumberjack Song eventually, here's the NumPy array we'll use for the problems in this section:

```python
lumberjack = np.array("I'm a lumberjack and I'm OK I sleep all night and I work all day".split(" "))
lumberjack

# Output
array(["I'm", 'a', 'lumberjack', 'and', "I'm", 'OK', 'I', 'sleep', 'all',
       'night', 'and', 'I', 'work', 'all', 'day'], dtype='<U10')
```

43. What would you expect the value of `print(np.char.capitalize(lumberjack)[2]`) to display?

Show Solution

Hopefully, by now you found this exercise to be easy-peasy, lemon squeezy:

```bash
Lumberjack
```

44. How could you surround each string with an initial and final asterisk character (\*)?

Show Solution

OK, that one was a bit more challenging. `np.char.add` can be used to concatenate two arrays. We call it in two steps to add the asterisk to the beginning and the end of each string. Here's the code and the output.

```python
step1 = np.char.add(["*"], lumberjack)
step2 = np.char.add(step1, ["*"])
print(step2)
```

```bash
["*I'm*" '*a*' '*lumberjack*' '*and*' "*I'm*" '*OK*' '*I*' '*sleep*'
 '*all*' '*night*' '*and*' '*I*' '*work*' '*all*' '*day*']
```

45. The function, `np.where`, can be used to create an array of indexes that can be used to index into the original array to subset an array based on a condition. If passed only a condition, it returns a set that array in the first value of a tuple, and we need to ignore the second (empty) condition. We can then use the indexes returned to get an array of the elements themselves.  
      
    Given that background, what might you expect the following to display?

```python
search_results, = np.where(np.char.str_len(lumberjack) >=5)
print(search_results)
print(lumberjack[search_results])
```

Show Solution

```bash
[2 7 9]
['lumberjack' 'sleep' 'night']
```
