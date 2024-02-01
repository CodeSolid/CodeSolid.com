---
title: "Python Function Best Practices"
date: "2022-12-27"
categories: 
  - "python-functions"
coverImage: "first-prize.jpg"
---
# Python Function Best Practices

Learning to write functions in Python -- or any language -- is like learning to play chess. We can master the basics of play and how to move the pieces around the board in a few minutes, but learning how to play well against more advanced opponents can take a lifetime to master.

Between the beginner level and the level of the grandmaster, one of the things we try to do is to study the strategies and best practices of those who came before and have played the game better than us. In this spirit, we present a short list of Python function best practices. Learning and implementing these function best practices will help you write functions that are clean, simple, and easy to understand and maintain.

### Write Functions that Have a Single Responsibility

In general, functions should do a single thing, and it should be clear what that one thing is. One very simple approach to this is to avoid using "and" in a function name. For example, `validate_and_save_user` can be recast as two separate functions, `validate_user` and `save_user`. This second version makes it easy to test the user validation independently of saving a user.

Yes, this may mean that some functions will become smaller, sometimes to the point of being only a few lines or a single line long. This is not necessarily a problem if the function adds value by making it clear what the intent of the code is. See the next point for more on this.

### Use Functions to Clarify Intent

It's sometimes a judgment call as to whether a function will clarify the code's intent or simply add unnecessary lines of code, but I would suggest that when in doubt, a function may be helpful. Consider the following code:

```python
# ...
if user_is_subscriber and user_subscription_level == 2:
     # do something
```

Granted, the lack of clarity is really around the variables here. What are the subscription levels, and what is the magic number 2 doing? So far this code is completely mysterious. Consider instead:

```python
def is_platinum_user(is_subscriber: bool, subscription_level: int):
    platinum_level = 2
    return is_subscriber and subscription_level == platinum_level

# ...
if is_platinum_user(user_is_subscriber, user_subscription_level):
    # do something,
```

Without impacting the surrounding code, we've done a safe refactoring that now makes it clear that subscription level #2 is the boundary between the platinum level and the rest of the folks. Moreover, it's clear by looking at the caller code what it's trying to do now, and as a side benefit, our code now has a single source of truth for who the cool kids are.

One suggestion that was a favorite of the Ruby community is worth mentioning here. Sometimes a good indicator that you need a function to clarify your intent is if the code is unclear enough that you're tempted to write a comment to clarify it. Though I don't agree with the general condemnation of comments, that "all comments are code smells", I do think that comments may often point the way to a place where a function may make things more clear.

### Choose Function and Parameter Names Carefully

Function names should adequately describe the function's purpose, and should generally consist of at least a noun and verb combination. Take a look at the following function names:

- `load`

- `load_user`

- `load_user_from_database`

It's very hard to tell what the first one is doing, the second is improved considerably, and by the time we reach the third we know exactly what's going on just by looking at the name. Granted, if the third one is in the `database` module already, `load_user` might be sufficient to describe it for a developer familiar with the codebase. When in doubt, it's better when naming functions to err on the side of clarity. This is a case where the Zen of Python's advice that "Explicit is better than implicit." really makes a lot of sense.

The same thing goes for parameter names. Unless you're dealing with two-dimensional points or locations for buried pirate treasure, banish "x" and "y" from your code. Consider the difference between:

- `load(x)`

- `load_user(email)`

You know what the second one is doing, don't you? What about the first? Is it loading a user by an email address or loading gold that a pirate buried?

Don't make users guess. Remember, the person reading your code six months from now may be you!

### Document Function Parameters With Type Hints

Consider a Python function that takes a user\_id as an argument. In a relational database with autoincrement fields, that user\_id might be an integer. Otherwise, it might be a string representing a uuid. If we have a function: `lookup_user(user_id)`, we don't have any guidance whatsoever on what we're dealing with. If, however, we see a function definition with a type hint: `lookup_user(user_id: int) -> User`, we know now that we need to pass an integer as an identifier, and we even have a class we might click on to navigate to more information about the return value.

To be sure, we can always look around the code and figure it out, but the goal of all our function best practices should be to make your functions as obvious as possible, and type hints help to do that. In addition, if the consumer of your function use some sort of IDE or linting tool that supports type hints, they can get a warning if they use the function incorrectly.

### Use Docstrings to Further Document Functions

Historically, Python had docstrings long before it had type hints. Python docstrings generally begin with a brief statement describing what the function does. For certain short and easy-to-understand functions, this may be all that's needed. Docstrings can also contain more detailed usage notes and details, as well as information about parameter names, types, meanings, and default values. For more information about Python doc strings, [PEP 257](https://peps.python.org/pep-0257/) discusses several important docstring conventions.

### Prefer Functions that Accept Basic Python Types

When writing a function, it's often tempting to pass an object to it and then read whatever attributes we need to read off the object. This can certainly make things more convenient when there are many such attributes, but it raises several issues.

In the first place, if the object is not immutable, we need to read through the whole function to understand if the object was changed once we handed it off. Reading the attributes before the call makes this a non-issue.

Secondly, since objects also contain methods, we have the same problems with respect to having to examine whether our function is causing side effects.

Third, having a non-object interface makes the function generally much easier to test.

Finally, if the function in question is tightly coupled to the object, there's a case to be made that perhaps it makes more sense for at least part of it to be broken out as a method on the object itself.

I realize that this best practice may be a bit controversial, and some developers who are object purists will argue that objects should pass messages to one another, that's the whole point of object-oriented programming. Having seen how messy things can get when stateful objects are passed around, I disagree with this. I prefer the enhanced testability and simplicity of interfaces that accept simple types.

### Prefer Functions with No Side Effects

The easiest functions to reason about are those that map a given set of parameters to an unambiguous, deterministic return value. These are analogous to mathematical functions, and they are what the functional programming folks refer to as pure functions. Pure functions do not relate to any external state and their behavior is easy to test and reason about.

Readers familiar with functional programming will probably have noticed by now that I've been heavily influenced by them, even though Python is certainly not a "pure" functional language. It's worth noting, however, that many of the most ideologically pure languages in this respect are also the least widely adopted, so there's a great deal to be said for languages like Python that offer greater flexibility.

Along the same lines of being flexible, one very important exception I would make to the general rule of avoiding side effects is in the area of logging. For any application meant to run in a production environment, logging is critical to ensure you can troubleshoot issues. Strictly speaking, logging is a side-effect, but my position is that the advantages of having logs available clearly outweigh whatever benefits one would get by being a functional programming purist.

### Prefer Returning a Copy to Mutating a Parameter

Unless a section of code is extremely sensitive, it's generally a good idea to avoid functions that mutate variables that are passed in. If you need to add values to a list based on some condition, for example, you could return a copy of the list with the new element added.

Another approach if the condition is non-trivial is to isolate it to a function and modify the list in the caller instead. This avoids the performance penalty of cloning the list, but at the same time avoids having a function that operates on its parameters rather than returning a value.

The point here is not to add extra clock cycles but to think about following the general principle of having a clear path from inputs to outputs, keeping side effects to a minimum.

### If You Do Mutate a Parameter, Make It Obvious

There are times when returning a copy of an existing list or sequence may not be feasible or desirable, and it may be that we have enough places we want to do this task that we need to break it down into component functions.

Once again, being pragmatic trumps being an ideological zealot. In such cases, we can fall back upon the general rule of not making a user guess what a function is doing, but instead documenting it as best we can in both the name of the function and the docstring.

### Use Asserts to Document the Function Contract

I am indebted to Steve Macguire's book, Writing Solid Code, both for the inspiration that led to the name of this website and to for the current best practice. Macguire recommends using asserts to check a function's "invariants", which is a fancy word for something we hold to be true. So when "we hold these truths to be self-evident, that all \[persons\] are created equal", that's an invariant.

Like C, the language that was the topic of Macguire's book and that had an assert macro, Python has an "assert" function that can be used to check if preconditions are met. One of the best places to put such checks is at the start of a function, to check that the arguments passed to the function makes sense.

When we discussed returning early from a function, we had an example that checked to see if a list were passed as None or empty, and returned early from the function.

```python
def count_sales_over_one_hundred(sales):
    """An early return example"""    
    if not sales:
        return 0

    # Do count otherwise...
```

Though this code works just fine, it could be improved somewhat, since generally, passing None where we're expecting a valid list or another type should be handled as a programmer error. Since an empty list is safe to iterate over if we're counting things (i.e., we won't iterate at all, and the count will be zero, as expected), we can treat None separately here as a programmer error by using an assert:

```python
def count_sales_over_one_hundred(sales):
    """Assert example"""
    assert sales is not None
    # Do count otherwise...
```

Note that in production, asserts may be optimized out of your code for example, by running it as shown here:

`python -O progam_name.py`

Because of this, it's important when using asserts not to check errors that may be real runtime exceptions this way (files that fail to open, for example). Also, _never_ use assert "inline" to check the return value of a function. The following code does something important when run with assertions on (the default). Using the `-O` or -OO switch, `something_important` is never called!

```python
def something_important():
    print("Doing something important here...")
    return True

# Don't do this!  Something_important may not be called.
assert something_important()
```

I learned not to do this the hard way somewhat early on in my career.

### Closing Thoughts: Be Mindful of State

Perhaps as long as we've programmed computers, and certainly for as long as they've had sufficient memory to hold a decent amount of data, managing state has been an issue. By now almost all programmers have heard the timeworn advice to avoid global data, but much of the history of programming best practices since then can be seen as just moving that data around, without solving the fundamental problem. Beginning around 1972 in the case of Smalltalk, and 1979 for C++, object-oriented languages promised to free us from global state by encapsulating code and data together as one unit.

However, anyone who shares my experience of having to debug troublesome state management in a large-scale class may be inclined to agree that object orientation didn't quite solve the problem, it just localized it. To be sure, having things narrowed down from "all of the software" to "this messy class" was an improvement, but managing any level of complexity in state is still problematic.

I'm inclined to agree with the functional programming folks that the solution to this issue lies in small, stateless functions passing immutable data around, such that such state as we need is even further segmented and localized. Yet the languages that force one to do this are -- let's admit -- far less popular than the ideologically "messy" languages we know and love like Python. However, with some thoughtful attention and lots of practice, we can write programs that are as easy to maintain as they are to understand.

## You May Also Enjoy

[Python Format Strings: From Beginner to Expert](https://codesolid.com/python-format-strings/)  
  
[Python Dataclass: Easily Automate Class Best Practices](https://codesolid.com/python-dataclasses/)

[Python Indexing and Slicing](https://codesolid.com/python-indexing-slicing-exercises/)

[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)
