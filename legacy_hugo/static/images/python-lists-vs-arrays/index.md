---
title: "Python Lists vs. Arrays:  How to Choose Between Them"
date: "2022-02-02"
categories: 
  - "python"
coverImage: "list-ledger-800x600-1.jpeg"
---

When newcomers think of arrays, they may have an idea that this is implemented in Python as the built-in list type. However, as in other languages, Python lists and arrays are actually quite different. Even experienced Python developers often reach for the list type first when they need a sequence type, and for most cases, this is definitely the right choice. There are some special cases where arrays make more sense, but for everyday programming tasks, Python lists are more efficient.

As with most things in Python, the language's consistency means that you can often easily replace the one with the other, or at least, their APIs are very similar. Let's look at arrays and lists in turn. Finally, we'll also take a brief look at how NumPy fits into the picture in terms of performance at the end.

Table of Contents

- [Python Lists 101](#python-lists-101)
- [Python Arrays](#python-arrays)
- [Arrays May Use Less Memory Than Lists](#arrays-may-use-less-memory-than-lists)
- [For Large Amounts of Data, Use Generators Instead of Lists or Arrays](#for-large-amounts-of-data-use-generators-instead-of-lists-or-arrays)
- [Performance Timers: Array and List Loop Performance](#performance-timers-array-and-list-loop-performance)
- [Tip: Use Arrays For Low Level Buffer Access](#tip-use-arrays-for-low-level-buffer-access)
- [NumPy Arrays and Performance](#numpy-arrays-and-performance)

## Python Lists 101

```python
from datetime import datetime

# A list initialized with a literal
short_list = ["first", 2, datetime.now()]

# Define a list using a list comprehension
long_list = [x for x in range(1,101)]

# Lists grow dynamically.
long_list_2 = list()
for x in range(1,101):
    long_list_2.append(x)

print(long_list == long_list_2)
```

Output:

```bash
True
```

From the first example above (`short_list`), we see that lists in Python are able to hold elements of disparate types. The second example (`long_list`) shows a list comprehension to generate a list. The third example creates a list identical to the one in the second example. This time we use a simple loop, as one might do in another language. The other thing this demonstrates is that the list grows dynamically, and mutated in place. We call append to add each element in turn, and the list grows in size to accommodate this.

Despite the name and the ability to grow dynamically, Python lists are not implemented internally as a linked list. Rather, they are an array of references to objects. When you call "`append`", on a list, Python allocates more memory than it needs to append a single item to be more efficient. Because Python lists are implemented as an array, indexing any object in the list is efficient, no matter where in the array the object is located.

Let's turn next to Python arrays;

## Python Arrays

There are a few differences between lists and arrays that we should go over up front.

First, let's discuss some of the types that are available. The list type is always available as part of Python's built-ins. With arrays, there are several types we can talk about. Two built-in types are the `bytes` type, an immutable sequence of bytes, and the `bytearray` type, a mutable array. Other arrays can also be created where the item size is not just a single byte, but matches well known C types. These arrays are created using the array module, which must be imported.

Lists of course have a literal syntax: `[item1, item2, ..., itemN]`, as we saw in the example above. For array types, only the immutable `bytes` built-in type has a literal syntax, prepending "b" to a string. As with regular Python strings, `bytes` literals can also have an "r" to mean the "raw" case where we want to treat the escape character, `"\n"`, as a literal. For example:

```python
b1 = b"123\n4"
print(f"Bytes of length: {len(b1)}:  {b1}")

b2 = br"123\n4"
print(f"Raw bytes of length: {len(b2)}:  {b2}")
```

Output:

Bytes of length: 5:  b'123\\n4'
Raw bytes of length: 6:  b'123\\\\n4'

Objects of type `bytes` be indexed or sliced as with most sequences, but indexing and slicing can't be used to assign a value.

```python
b1 = b"Hello, Python fans!"
print(b1[7:13])
print(b1[7])

# This code would give raise an exception:
# TypeError: 'bytes' object does not support item assignment
# b1[7] = 'J'
```

Output:

```bash
b'Python'
80
```

The mutable array types do not have a literal syntax like the `[item1, item2, ..., itemN]` syntax that can be used to initialize a list. For these, an array constructor must be used.

Arrays must always contain objects of the same type. For those in the "array" module, the type must be specified when the object is initialized. For the built-in `bytearray` type, of course, the underlying type for each individual item is a byte. However, Python doesn't have a byte type, so it reports the type as an int and returns this type if indexed.

```python
bytes_object = b'Python'
print(type(bytes_object[0]))
```

Output:

```bash
<class 'int'>
```

Another built-in array type is the `bytearray`. The [constructor](https://docs.python.org/3/library/functions.html#func-bytearray) for this class takes different types of values, when passed an integer it allocates an array of that many bytes, initialized to zero. Unlike the `bytes` type, `bytearray` objects are mutable, as we show below:

```python
bytearray_object = bytearray(100)
print(bytearray_object[0:5])
bytearray_object[0:5] = b'Hello'
print(bytearray_object[0:5])
```

Output:

```bash
bytearray(b'\x00\x00\x00\x00\x00')
bytearray(b'Hello')
```

## Arrays May Use Less Memory Than Lists

For smaller types like bytes, arrays may more compactly store their values than lists do, since arrays can store the object itself, while in the list case there is both an object and a structure with a reference to it.

Some examples from the array module will make this clear.

```python
from array import array

# Build an array of unicode characters (strings) from a single larger string.
string_elements = array('u', "Hello, array lovers everywhere!")

print(len(string_elements))
print(string_elements[0])
print(string_elements[0:5])
print(type(string_elements[0]))
print(string_elements.itemsize)
```

Output:

```bash
31
H
array('u', 'Hello')
<class 'str'>
4
```

In the example above, the first parameter to the array constructor is a type code, in this case saying we're dealing with Unicode characters. The second parameter is a string, which according to the Python documentation is converted into an array of type `wchar_t` internally in C. This can be either 2 bytes wide or 4 bytes wide depending on the platform, according to the documentation. (I'd expect 4 to be a bit more common, since utf-8 characters can be up to 4 bytes wide, and I imagine this would make the underlying code simpler).

Either way, when we access an element of the list, Python converts the character to the Python string type, as we see in the last line. It does the same thing for slices in this case.

We get a very different result if we change the type to an array of unsigned char (basically a byte array).

```python
from array import array

# Build an array of bytes (unsigned chars)
string_elements = array('B', b"Hello, array lovers everywhere!")

print(len(string_elements))
print(string_elements[0])
print(string_elements[0:5])
print(type(string_elements[0]))
print(string_elements.itemsize)
```

Output:

```bash
31
72
array('B', [72, 101, 108, 108, 111])
<class 'int'>
1
```

Here, the "b" prefix before the string means to treat the string as an array of bytes, and it's represented internally as an unsigned char. Because the string is in English, the length Python returns is the same in both cases, because it's the length of the array, not the underlying byte representation. This works out because the first 128 ASCII characters in UTF-8 use the same 1-byte value that ASCII uses.

So this representation is quite compact. Depending on the type, of course, it's possible you'll need more space in memory. An array of double-precision floating point values, for example, uses 8 bytes per item.

```python
double_array = array("d", [42.42])
print(double_array.itemsize)
```

Output:

```
8
```

##   
For Large Amounts of Data, Use Generators Instead of Lists or Arrays

Although arrays may store their values more compactly than lists, memory can still be a constraint for very large arrays. In this case, a Python generator may be a more appropriate choice. Let's say we wanted a class to iterate through the lines of a file. For short files, we could even read the whole file into a list and process the list. If we wanted to do this with a longer file, we could of course read and process a line at a time directly in Python. However, this case also lets us demo a basic generator:

```python
class FileIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file_handle = open(filename, 'r')
        
    def readline(self):
        while line := self.file_handle.readline():
            yield line
        self.file_handle.close()
        
contents = FileIterator('giant_file.txt')
for line in contents.readline():
    print(line)
```

In addition to creating an iterable generator with the yield keyword, Python also supports concise generator expressions, which have a similar syntax to list comprehensions. Let's say for example that you wanted to sum up all the odd numbers between below 10. For such a small list of numbers, using a list comprehension would be fine and quite concise. Indeed, if you're new to list comprehensions, you may find this syntax _too_ concise, but bear with me:

```python
print(sum([x for x in range(10) if x %2 == 1]))
```

Output:

```bash
25
```

Again, too concise or not, that code works fine for a short list. But what if you wanted to try the same thing for all the numbers under some multiple of a print(sum((x for x in range(10) if x %2 == 1)))print(sum((x for x in range(10) if x %2 == 1)))billion or more. Well, in addition to taking a lot more time, such a list would start to use up too much memory. However, we can change the list comprehension to a generator expression so that it would work fine even if we change 10 to a much larger number. All that's involved is to change the brackets around the list to parentheses:

```
print(sum((x for x in range(10) if x %2 == 1)))
```

Again we get the output of 25, but here we can safely change range(10) to range(1000000000). I've actually done it. You won't run out of memory. (But be prepared to wait awhile anyway!)

## Performance Timers: Array and List Loop Performance

As we've seen, there are some space-saving benefits to arrays, but for really large sequences, generators provide a better option. However, setting aside the issue of space savings, it's possible that Python arrays may have better loop efficiency than lists. Until we test this, we really have no way of knowing.

To test this out, we used the `timeit` function to see if the iteration time differs significantly between arrays and lists. We expected the times to be about equal or perhaps a little faster in the non-object array case. The actual result then was quite surprising. In each case, we'll looped through a list or array of 10,000 numbers 10,000 times.

The list case first

```python
from timeit import timeit

result = timeit(setup="num_list = [x for x in range(0,10000)]", 
                          stmt="for i in num_list: x = i", number=10000)
print(result)
```

Output:

```bash
0.6914394581690431
```

Now the array case, using signed integers:

```python
from timeit import timeit

result = timeit(setup="from array import array; num_array = array('i', [x for x in range(0,10000)])", stmt="for i in num_array: x = i", number=10000)
print(result)
```

Output:

```bash
1.3694779579527676
```

Admittedly, this result still seems a bit strange to me. One possible place for the slowdown I considered was the conversion of the underlying object to a Python object reference, but even when I reworked the Python code to ignore the loop values, the slowness persisted, though both loops became slightly faster. For Python loops, the winner is clearly the list type.

## Tip: Use Arrays For Low Level Buffer Access

As we've seen, although arrays may offer some space savings over Python lists in certain cases, for truly large sequences, the preferred technique to iterate over them is either to read each item individually or to use a generator. Also, although some space may be saved by using an array, we showed that this will negatively impact loop performance for long sequences.

So what, then, is the point of ever using an array at all? Arrays, unlike lists, support accessing the memory that contains them directly. This can be used to interface with the C language, or to use Python libraries to do fast IO without dipping into C. One main mechanism used to support this is Python's [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects), which is a way of exposing the contents of a memory buffer to a low-level IO function such as [readinto](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto). This would allow pre-allocating and re-using the buffer to efficiently read data from a socket, for example.

In addition to one-time memory allocation, which can be an optimization where many reads are involved, the buffer protocol also supports zero-copy slicing. To demonstrate this, we can use a [memoryview](https://docs.python.org/3/library/stdtypes.html#memoryview) object, which allows obtaining a wrapper around this raw buffer. Let's compare how slicing works for this case with how it works for a list. In the example below, we see that creating a slice in the array returns a copy of the array:

```python
list_numbers = [0, 0, 0, 0, 0]
print(list_numbers)

# Try to mutate the list by changing a slice of the list
first_three = list_numbers[0:2]
first_three[0] = 100
first_three[1] = 99
print(list_numbers)
```

Output:

```bash
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
```

Note that for a list, creating a variable for the slice is treated differently than treating the slice as an L-value (i.e., the target of an assignment expression). In that case, the slice is mutable.

```
list_numbers = [0, 0, 0, 0, 0]
print(list_numbers)
list_numbers[0:1]  = [5,6]
print(list_numbers)
```

Output:

```
[0, 0, 0, 0, 0]
[5, 6, 0, 0, 0, 0]
```

If we use a memoryview object instead to show the same operations, we see that slicing simply returns a view into the original buffer, not a copy of it. In Effective Python, Brett Slatkin gives the example of returning streaming video data to a consumer, and being able to efficiently grab a slice of data to return to the user in response to skipping ahead in the video, for example.

The example below simply reworks our list example on a small scale to demonstrate that for memoryview, a returned slice is not a copy, but exposes the original list.

```python
memoryview_numbers = memoryview(bytearray(5))
print(memoryview_numbers.tolist())
first_three = memoryview_numbers[0:2]
first_three[0] = 100
first_three[1] = 99
print(memoryview_numbers.tolist())
```

Output:

```bash
[0, 0, 0, 0, 0]
[100, 99, 0, 0, 0]
```

## NumPy Arrays and Performance

Although our focus on this article has been on the array types that are part of the standard library, we should probably mention NumPy arrays, given that this library is almost as popular! In NumPy, the `array` type is an alias for the `ndarray` class, an n-dimensional array. These arrays feature a number of aggregation and matrix algebra functions that are written in C with a Python wrapper.

In addition to adding matrix support, for the operations they support, NumPy arrays are extremely fast compared to their standard library counterparts. However, the caveat is that this is true only when using the methods that NumPy provides. Mixing Python's standard library calls with NumPy's arrays can actually decrease performance.

Here are the timings we ran earlier, with two additional comparisons at the end, one using the standard library (the "wrong" way), and one using an equivalent NumPy function. I apologize for the low readability of these timeit expressions; feel free to skim ahead to the output.

```python
from timeit import timeit
import numpy as np

iterations = 500

def display(elapsed_time, message, rounding=3):
    print(f"{round(elapsed_time, rounding)} seconds -- {message}.")

result = timeit(setup="num_list = [n for n in range(0,256)] * 1000", 
                stmt="sum(num_list)", number=iterations)
display(result, "Python sum function on a list of numbers")

result = timeit(setup="l = [n for n in range(0,256)] * 1000; num_array = bytearray(l)", 
                stmt="sum(num_array)", number=iterations)
display(result, "Python sum function on a bytearray of numbers")

result = timeit(setup="import numpy as np; l = [n for n in range(0,256)] * 1000; np_array = np.array(l)", 
                stmt="sum(np_array)", number=iterations)
display(result, "Python sum function on a NumPy array", rounding=4)

result = timeit(setup="import numpy as np; l = [n for n in range(0,256)] * 1000; np_array = np.array(l)", 
                stmt="np_array.sum()", number=iterations)
display(result, "NumPy sum method on a NumPy array")
```

Output:

```bash
0.597 seconds -- Python sum function on a list of numbers.
0.729 seconds -- Python sum function on a bytearray of numbers.
6.585 seconds -- Python sum function on a NumPy array.
0.051 seconds -- NumPy sum method on a NumPy array.
```

So, in this case at least, NumPy is an order of magnitude slower when interfacing with the Python standard library, but an order of magnitude faster on its own!
