---
title: "Python Function Exercises With Solutions"
date: "2023-01-10"
categories: 
  - "python-functions"
coverImage: "barbell_2_small.jpg"
---

One of the first things to master as a newcomer to Python is the skill of writing functions. Like everything else in programming, skills are developed through practicing. These beginner-focused exercises contain complete solutions to help you if you get stuck and to show you how we would approach the problem.

It's strongly recommended that you try these exercises out first before looking at the solutions. If you want to try these out in Jupyter notebook, we've include an [online notebook](https://jupyter.codesolid.com/lab/index.html?path=exercises/FunctionExercises.ipynb) that contains only the exercises -- you can work on these online without installing anything.

1. Using a loop (that is, without using a slice), write a function "reverse\_list" and takes a list as input and returns a copy of the list in which all the elements have been swapped (the first element with the last, the second with the next to last, etc.) Test that it works correctly for the following lists:

```python
odd_length = [23, 4, 9, 6, 8, 22, 18]
even_length = [6, 5, 2, 9, 44, 12]
empty_list = []
```

Solution:

```python
def reverse_list(input: list) -> list:
    """returns a reversed copy of list, leaving original list unchanged"""
    half_list = int(len(input) / 2)
    output = input.copy()
    for idx in range(0, half_list):
        output[idx] = input[len(input) - 1 - idx]
        output[len(input) - 1 - idx] = input[idx]
    return output

# Test as instructed
odd_length = [23, 4, 9, 6, 8, 22, 18]
even_length = [6, 5, 2, 9, 44, 12]
empty_list = []
assert reverse_list(odd_length) == [18, 22, 8, 6, 9, 4, 23]
assert reverse_list(even_length) == [12, 44, 9, 2, 5, 6]
assert reverse_list(empty_list) == empty_list

# Ensure orginal unchanged
assert odd_length == [23, 4, 9, 6, 8, 22, 18]
```

2\. Write a function that takes in a string and returns the string with all the vowels  
removed. Test it using the following code (you should see no output):

```python
assert remove_vowels("We all love Python!") == "W ll lv Pythn!"
```

Solution:

```python
def remove_vowels(string):
    """Returns a string with the vowels removed."""
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string

assert remove_vowels("We all love Python!") == "W ll lv Pythn!"
```

3\. Write a function that takes in a list of integers or floats and returns True if the list contains duplicates and False if the list does not contain duplicates. Use a type hint to "enforce" the correct type.

Solution:

```python
def has_duplicates(items: list[int|float]) -> bool:
    """Checks the list and returns true if there are duplicate values."""
    return len(set(items)) < len(items)

# Test
assert not has_duplicates([1,2,3,4])
assert has_duplicates([1.0, 2.0, 3.3, 3.3])
```

4\. Write a function to print all the powers of two, up to and including the twelfth power. The output should look like this:

```bash
2 to the power of 0 = 1
2 to the power of 1 = 2
# ...
```

Use a while loop to control the iteration and printing.

Solution

```python
def print_powers_of_two():
    """Print two raised to a number, for numbers in range 0 to 12, inclusive"""
    exponent = 0
    LAST = 12
    while exponent <= LAST:
        print(f"2 to the power of {exponent} is {2**exponent}")
        exponent += 1

print_powers_of_two()
```

5\. Write a new function to calculate the same values as we did in #4. This time, write a function named calculate\_values to return numbers raised to a power of two in a list, again beginning at 2 to the zero power and ending at 2 to the 12th power as before. Call the function and test the returned list this way:

```python
values = calculate_values()
print(values)
assert values[0] == 1
assert values[-1] == 4096
```

You should see the list values and no other output.

Solution

```python
def calculate_values():
    LAST = 12
    return [2**exponent for exponent in range(0, LAST+1)]

values = calculate_values()
print(values)
assert values[0] == 1
assert values[-1] == 4096
```

* * *

6\. Write a function with the following signature:

```python
def display_box(width: int, height: int, character="*")
```

This function will draw a simple ASCII-art rectangle (non-filled) of the given height and width, using `character` to print the lines. For example, `display_box(5, 4, 'x')` should output the following:

```python
xxxxx
x   x
x   x
xxxxx
```

* * *

The function should raise an exception if the dimensions are less than 2 wide by two high.

Solution

```python
def display_box(width: int, height: int, character="*"):
    if width < 2 or height < 2:
        raise Exception("Box dimensions must be at least 2 x 2")
    line = 0
    while line < height:
        # First or last line
        if line == 0 or line == height - 1:
            print(character * width)
        else:
            print(character + " " * (width - 2) + character)
        line += 1

# Try testing with different values, e.g.
display_box(5, 4, 'x')
```

7\. This exercise is famous, and a perhaps one of the most popular "can you handle basic programming" interview questions. Write a function, fizzbuzz, with a single integer argument named value. If the value is evenly divisible by three, return the string "fizz". It the value is evenly divisible by five, return the string "buzz". If the value is evenly divisible by both three and five, return fizzbuzz. Finally, if none of these apply, return an empty string.

Test it with the following code:

```python
values = [3,6,9,11,5,10,20,23,15,30,60]
for value in values:
    print(fizzbuzz(value))
```

Solution

```python
def fizzbuzz(value: int) -> str:
    result = ""
    if value % 3 == 0:
        result += "fizz"
    if value % 5 == 0:
        result += "buzz"
    return result
    
values = [3,6,9,11,10,20,40,23,15,30,60]
for value in values:
    print(fizzbuzz(value))
```

Test output:

```bash
fizz
fizz
fizz

buzz
buzz
buzz

fizzbuzz
fizzbuzz
fizzbuzz
```

8\. There are six New England states: Rhode Island, Connecticut, Massachusetts, Maine, Vermont, and New Hampshire. Their postal abbreviations are RI, CT, MA, ME, VT, and NH, respectively.

Write a function that takes a New England state code as a string and returns a string with the longer name as shown above. Return None if no mapping is found.

Solution

Whenever an exercise calls for mapping one value to another, think "dictionary"! Once you realize that, the function boils down to creating the dictionary and passing the key (in this case, the state code), to the get function. (Get is convenient since it will return None by default if the key is not found rather than throwing an exception).

```python
def get_state_full_name(state_code: str) -> str:
    """Maps a state code to a full name for New England States only"""
    states = {
        "RI": "Rhode Island", 
        "CT": "Connecticut",
        "MA": "Massachusetts",
        "ME": "Maine",
        "NH": "New Hampshire",
        "VT": "Vermont"}
    return states.get(state_code.upper())
```

9\. Speaking of interview questions, here's another fairly simple one we used to ask developers who interviewed for our small team. We were doing Java, but the question works equally well in Python, so I've translated it here.

Suppose you have a list of movie objects, which are defined as follows:

```python
class Movie:
    def __init__(self, title, director, year_released):
        self.title = title
        self.director = director
        self.year_released = year_released
```

Write a function that takes a list of movies and displays the title and director of each movie in the list.

Solution

Here's a reasonable solution one could code in an interview that includes an informal test to demonstrate the function.

```python
  class Movie:
    def __init__(self, title, director, year_released):
        self.title = title
        self.director = director
        self.year_released = year_released
        
def display_movies(movies: list[Movie]) -> None:
    """Displays movie title and director, one per line"""
    for movie in movies:
        print(f"'{movie.title}'. Directed by {movie.director}.")

movies = [Movie("Full Metal Jacket", "Stanley Kubrick", 1987), 
          Movie("Star Trek II: The Wrath of Khan", "Nicholas Meyer", 1982)]

display_movies(movies)
```

Output:

```bash
'Full Metal Jacket'. Directed by Stanley Kubrick.
'Star Trek II: The Wrath of Khan'. Directed by Nicholas Meyer.
```

10) A certain print order costs $3.00 per copy for orders of less than ten copies, $1.25 for for orders of 10-99 copies, and $0.90 per copy for orders of 100 copies or more. Write a function that returns a total price for the order.

Solution

Note that in the solution below, we use descriptive names to clarify the pricing and price cutoffs. This makes the function longer but clarifies our intent and makes it easier to change prices or cutoffs if the business requirements change.

```python
def calculate_price(copies: int):
    """Calculate price of a print order based on cutoffs"""
    small_order_rate = 3.00
    medium_order_rate = 1.25
    large_order_rate = .90
    
    minimum_medium_order = 10
    minimum_large_order = 100
        
    if copies < minimum_medium_order:
        return copies * small_order_rate
    elif copies < minimum_large_order:
        return copies * medium_order_rate
    else:
        return copies * large_order_rate
```

11) The velocity of an object falling near the earth is given as -9.81 meters per second squared. (It's negative because the object is falling downwards, so it's relative to where it started). Write a function that takes two arguments, a whole number of seconds since the object was released and a starting height in meters. Return a boolean value that's True if the object would still be accelerating, or False it it already hit the ground.

Solution

```python
def still_falling(seconds_ago: int, starting_height: float):
    """Returns true if an object dropped so many seconds ago would still be falling"""
    distance = -9.81 * seconds_ago**2
    return starting_height + distance > 0
```
