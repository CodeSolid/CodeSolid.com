---
title: "Python Classes Zero to Expert: A Tutorial with Exercises"
date: "2022-03-29"
categories: 
  - "python-for-beginners-posts"
  - "python-practice"
tags: 
  - "featured"
coverImage: "gears-scaled.jpg"
---

Although it may not appear that way at first because of how well Python objects are integrated into the language, Python is a highly object-oriented language.

We won't stop to prove that yet, but we will toward the end of the article. Instead, because this article focuses on the needs of beginning software developers, we need to build up some basic terminology first.

Following that, we'll create several basic examples of Python classes -- both how to write them and use them. Through these exercises, you'll learn about classes and objects, inheritance, and what we mean when we say a program is object-oriented.

We'll follow that up with a set of review questions and programming exercises you can run online or on your machine -- See our article on [getting started With Jupyter Notebook](https://codesolid.com/jupyter-notebook-a-complete-introduction/) if you need help running these online. These will reinforce your knowledge.


## Classes vs. Objects

Let's start with some basic terminology and definitions to get oriented. In Python, as in many other languages, you can think of Python classes as a template or cookie-cutter for creating objects. On the other hand, objects are "instances" of a class, just as you could consider Christmas Tree cookies to be "instances" of cookies cut out from a Christmas Tree cookie-cutter.

In Python, we can show the type of an object using the built-in function, type. For example:

```python
print(type(42))
print(type(98.6))
print(type("I am a string object"))
```

Output:

```bash
<class 'int'>
<class 'float'>
<class 'str'>
```

Using the Python type function shows us the class of the object we pass to it, so this tells us that even number and string literals are classes in Python.

Before we get into more theory, let's write our first class in Python. There will be a lot of new stuff here, but don't worry, we'll explain all that.

## A First Python Class

Let's look at a very simple Python class, and then we'll discuss the code in detail.

```python
# Declare a class
class Pet:    
    """a simple class declaration in Python"""    
    def __init__(self, name: str):
        """The __init__ method is a constructor"""
        self.name = name
            
    def move(self):
        """another method"""
        print(f"{self.name} is moving!")

# Create Two Instances
dog = Pet('Fritz')
cat = Pet('Smokey')

# Call a method on one instance
cat.move()

# Access a property on a class
print(dog.name)
```

Output:

```bash
Smokey is moving!
Fritz
```

Now let's examine what the code is doing. In lines 2 through 10, we declare a class. We begin on line two with the code "`class Pet`". Unlike many types defined by Python, such as list, dict, etc., for user-defined classes, the convention is to capitalize the name of the class. Inside the class, we indent the rest of the code.

The `__init__` method on line 4 is a special method called a constructor. Note the terminology: functions are called methods when they appear inside a class. The most common methods are instance methods. Instance methods start with a parameter that's conventionally called "`self`." This special parameter is not passed explicitly outside the class. Inside the class and its methods, however, it refers to the current instance of the class.

Inside the constructor, we set a property on the class, another name for a variable that's a member of a class. So `self.name = name` assigns a class property to the name passed in as a parameter. In addition to the constructor, we also declare another method, "`move"` on line 8. Here we can use `self.name` to access and display the property we set in the constructor.

To create objects, we use the name of the class as though it were a function. We can see this in action, where we create two pets on lines 13-14. Again, we don't pass self here explicitly, but we do pass the name argument (and any additional arguments, if there were any) as we would any other parameter.

On line 17, we see that we use the name of the instance, a period, and a method name to call a method. We can also use the name of the instance as we do in line 20 to access a property of the class and display it.

## Theory Break: What Is Object Orientation?

Now that we've defined a class and created and used two objects based on this definition, we're in a position to understand what it means to say a programming language is object-oriented. At one time, this was a favorite interview question for new developers, and I suspect you're still likely to encounter it.

Generally speaking, the conventional definition of an object-oriented language is a language that supports:

- **Encapsulation:** bundling code and the data it uses together in objects.
- **Inheritance**: being able to build subclasses or subtypes of classes. For example, in the Pet case, we might want a Dog and a Cat class that are related to Pet somehow. We'll see examples of that shortly.
- **Runtime polymorphism**: a fancy name for calling the correct method on the class based on the actual object type. We'll be able to demonstrate this once we've learned about inheritance.

## Inheritance in Python Classes

In our simple Pet class example, we saw how code and data were encapsulated in the class as methods and properties. Next, let's see how to use another central feature of object orientation: inheritance.

In Python, as in other languages, class inheritance serves many valuable functions.

First, it's a way to enforce the DRY principle ("Don't Repeat Yourself"). Pets have names, so we wouldn't want to copy and paste the code if we created a Dog class and a Rabbit class. We also want our pets to move. A deceased parrot makes for a great Monty Python sketch but not a great pet.

Secondly, inheritance lets us override certain class features if we need to. For example, for a Shape class, the draw method would do something different for Elipse, Line, and Rectangle, but the canvas they're drawn on would want to treat them all the same, perhaps iterating through a list and calling draw on each one.

Finally, inheritance lets us model how we think about classes of objects in the real world. We categorize things naturally, although it sometimes sounds strange to do it explicitly. We know that this orange is not representative of all oranges. It is an instance of a class whose parent class is fruit. The fruit class, in turn, is a child of the class, edible plants.

Let's dive into some concrete examples of inheritance using our Pet class.

```python
class Dog(Pet):
    def __init__(self, name: str, breed: str):
        Pet.__init__(self, name)
        self.breed = breed

class Rabbit(Pet):
    def move(self):
        print("Hop, hop, HOP!")    

spirit = Dog("Spirit", "Pit Bull")
spirit.move()
print(f"{spirit.name} is a {spirit.breed}.")

fluffy = Rabbit("Fluffy")
fluffy.move()
```

Output:

```bash
Spirit is moving!
Spirit is a Pit Bull.
Hop, hop, HOP!
```

Our first child class is `Dog`. We can also say that Dog is a subclass of Pet or that it extends Pet. We do this by enclosing the parent class in parentheses after the name of the class (line 1). On line 2, we create a new constructor for the `Dog` class because we also want to keep track of the breed. However, on line 3, we want to take advantage of the \_\_init\_\_ method in the parent to make sure the name is set up correctly, so we use the syntax <parent\_class\_name>.\_\_init\_\_(self, <other\_parameters>). Then we set the breed, which will only be a property of dogs, not of pets in general or rabbits. (Yes, I know: rabbits have breeds, too. But my poor little sample bunnies don't have that feature.)

Next, we move on to the Rabbit class on line 6. Again we put the parent class in parentheses. Here we inherit the constructor from Pet, but on line 7, we override the move method to make it unique for rabbits.

In the output section, we see the results. Spirit knows how to move because he's a pet. We didn't have to do anything extra. We did set up a new constructor, however, and as a result, Spirit has a breed, too. Because we also used the Pet class to set his name, we can now show his name and breed on one line.

In our discussion of object orientation, we said polymorphism allows us to call the correct object based on the object type. If we add the following code to our Dog and Rabbit example, we can see this in action:

```python
pets = [spirit, fluffy]
for pet in pets:
    pet.move()
```

Output:

```bash
Spirit is moving!
Hop, hop, HOP!
```

## When To Use Inheritance in Python, and When Not To

As powerful as inheritance is, newcomers to object-oriented programming sometimes tend to overuse it. Inheritance is not always the first tool you want to choose.

Inheritance is most useful in cases where you need to have a set of objects to expose one or more methods that allow them to do some basic operation "polymorphically," i.e., they are called the same way, but they do different things depending on the actual class of the object.

We've already given the example of a Shape class, which might implement the draw method differently for an Elipse, Rectangle, Line, Text, etc. If we think about what a drawing program might need to do with a set of shapes, we can develop many more examples that should be treated differently for each object type. For instance, it might implement `load` and `save` to store and retrieve the shape from a file, or other drawing and manipulation primitives such as `resize`, `rotate`, `flip`, etc. Or consider a generic Configuration tool, which might `read`, `write`, and `parse` ini files, XML, JSON, Yaml, or other file formats.

In all these cases, it's clear that the child objects can be treated polymorphically. Part of the reason these all work gets us into one of our core tests for when to use inheritance. In the case of a Shape, it makes perfect sense to say that a Circle or Elipse is a Shape, as is a Rectangle or even a line. Admittedly, "Text" may strike us as a borderline case, but in terms of being able to be resized, drawn on the screen, saved or loaded from a file, we realize that yes, in that respect, it's a Shape, too!

In contrast to relationships where one object _**is**_ another object, there are many cases where an object _**has**_ another object. In object-oriented design, you'll frequently encounter the advice that "is-a" relationships should be modeled with inheritance, but composition is the appropriate tool for "has-a" relationships.

Let's begin with an obvious case where confusing an is-a and a has-a relationship can lead to trouble. Consider a person and their email address(es). Here's some bad code for how that might be modeled:

```python
# BAD CODE. Don't do this

class Person:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.las_name = last_name

class Email:
    def __init__(self, first_name: str, last_name: str, email: str):
        self.email = email
        Person.__init__(self, first_name, last_name)
        
example = Email('Ben', 'Franklin', 'postmaster@usps.com')
```

If you saw this code outside of an example of what-not-to-do, you might suppose that the author was trying to associate a person with their email somehow. They indeed achieved that, but the implementation is loaded with problems.

1. An email address is not a person.
2. Trying to model it this way meant we now need a first\_name and last\_name to create an EmailAddress object.
3. It's frequently true that an email address uniquely identifies a person. (Certainly, many web apps behave as if that were true, even though husbands and wives will sometimes share an email address for their accounts). However, the person who has multiple email addresses is far more common. From that perspective, we can say that a person _**has**_ zero or more email addresses.

Given what we discussed above, here is a reasonable implementation for Person and "EmailAddress."

```python
from typing import List

class Email:
    def __init__(self, email, is_confirmed = False):
        self.email = email
        self.is_confirmed = is_confirmed
        
    def __repr__(self):
        return f'Email("{self.email}", is_confirmed={self.is_confirmed})'        
        
class Person:
    def __init__(self, first_name: str, last_name: str, emails: List = None):
        self.first_name = first_name
        self.last_name = last_name
        self.emails = emails
        if not self.emails:
            self.emails = []
            
    def __str__(self):
        emails = [str(email) for email in self.emails] 
        return f"{self.first_name} {self.last_name}: {emails}"
            
        
ben  = Person('Ben', 'Franklin')
me = Person('John', 'Lockwood', [Email('john@example.com')])
print(ben)
print(me)
```

Output:

```bash
Ben Franklin: []
John Lockwood: ['Email("john@example.com", is_confirmed=False)'
```

As you can see, this implementation models our real-world understanding of people and their emails. Ben Franklin didn't have one, but I do. Actually, I have several, but the model works for that, too.

The "`__str__`" and "`__repr__`" methods, incidentally, are Python magic methods. Implementing these is optional, but having one or both means you can customize how the object looks when it's converted to a string, for example, by the print method. (To see why, try running the code above but without the \_\_str\_\_ or \_\_repr\_\_ methods.). Generally speaking, \_\_str\_\_ is meant to be human-readable and less formal while `__repr__` should output a machine-readable string that could be used to reconstruct the object. The `__repr__` method is also called by Python when displaying the contents of a list, which is why we needed to implement that instead of `__str__` for the Email class.

The object-oriented design maxim we're employing here is a [well-known one](https://en.wikipedia.org/wiki/Composition_over_inheritance):

> Prefer composition to inheritance.
> 
> Original author unknown. In Design Patterns book and others.

I know it seems like a bit of a cheat: teaching inheritance, then telling you not to use it very much. However, in my experience, this maxim is a good one. I've seen many real-world examples where a developer used inheritance where composition would have made more sense.

One final beginner object-oriented programming pitfall I feel is worth mentioning is using inheritance on basic types such as strings or containers, which is rarely a good idea. For example, one might be tempted to implement email as a subclass of string, but as we saw with is\_confirmed, Email can equally well be a string with additional methods. This allows us, for example, to raise an exception in the init method if the email address doesn't match our expectation of what a valid email address should be.

If you feel like you need to subclass the str, list, or dict type, the python collections package has three wrapper classes you can use, but composition works just fine for most purposes.

## Python Abstract Base Classes

As in other languages, abstract base classes allow certain methods to be defined as signatures only, with no implementation. Such methods are called abstract. A subclass needs to be created to implement the abstract method to create an instance based on an abstract class.

This is easiest to see with an example. Let's go back to the animal class that we discussed earlier. Suppose we know that different animals eat and move differently. We want to make sure that every Animal can move and sleep, though we don't want to make any assumptions about how they do it in our base class. Here's how we can do this with an abstract class:

```python
from abc import ABC, abstractmethod

class Animal(ABC):
     
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass
```

At this stage, if you try to create an object based on Animal, you'll get an error:

```python
fluffy = Animal()
...
TypeError: Can't instantiate abstract class Animal with abstract methods move, sleep
```

The point of an abstract class is to have our cake and eat it, too. We want to force subclasses to implement certain methods, but we don't want to tell them how to do it. In order to create instances based on an abstract class, we must first subclass it and override the methods, for example:

```python
class Bird(Animal):
    def move(self):
        print("Flying...")
    
    def sleep(self):
        print("Snoozing in my nest...")
    
tweetie = Bird()
tweetie.move()
tweetie.sleep()
```

Output:

```bash
Flying...
Snoozing in my nest...
```

## Is Python an Object-Oriented Language?

If you speak to a system administrator or DevOps engineer, they may tell you that Python is a scripting language. That's because Python is a very effective tool for writing short, simple automation tasks. But the more you learn about Python, the more you discover that Python is a very object-oriented language.

Almost everything in Python is an object. So unlike Java, which makes a distinction between "primitive types" like numbers, and reference types (or objects), in Python, even numeric literals are objects.

Python operators are the exception to the "everything is an object rule," but even Python operators are implemented as syntactic sugar around methods on objects. Of course, this is very useful syntactic sugar -- it's a lot clearer to write four = 2 + 2 in Python than it does to write: four = (2).\_\_add\_\_(2), but the result is the same.

That \_\_add\_\_ function is another "magic method." These are sometimes called "dunder" methods (from the double-underbar at the beginning and end). We called it on the object created by the int literal, 2. We had to wrap the first `2` in parentheses so Python wouldn't think we were trying to deal with a floating-point number when we typed the period.

It's hard to get away from objects in Python. Even those simple functions we think we're creating in a script are wrapped in an object of the function type.

## Practice Exercises for Python Classes and Objects

The exercises for this article are below, but they're also available as a downloadable Jupyter Notebook, or you can develop them online.

[Download](https://github.com/CodeSolid/CodeSolid.github.io/blob/main/booksource/exercises/PythonClassesExercises.ipynb)

[Run Online](https://colab.research.google.com/github/CodeSolid/CodeSolid.github.io/blob/main/booksource/exercises/PythonClassesExercises.ipynb)

1. The code below has two bugs. Can you spot them? Try to do it without running the code.

```python
class Pet:
    def init(self, name):
        self.name = name

    def move():
        return f"{self.name} is moving..."
```

2. Rewrite the code from the last question so that the test below works and prints "Fritz is moving…"

```
# Paste and fix the code here:

# Leave this code
dog = Pet("Fritz")
print(dog.move())
```

3. Write a simple Tag class to encapsulate HTML tags, for example:

```markup
<p>I am a paragraph.</p>
```

4. For the tag class hierarchy, can you think of how this might be implemented as a function? Which way would you think is simpler and more maintainable?
5. Create an abstract base class, `Shape`, with a single abstract method, `draw`. Implement two child classes, `Elipse` and `Rectangle`, that override the draw method. For the implementation, you can substitute a stub (a simple string printout saying what the class is drawing).
6. You will need to create an \_\_init\_\_ method with some data for this task. For the Rectangle class that you defined above, print a rectangle using characters and the code to test it, for example:

```
# ... Implementation code above:

r = Rectangle(5,3)
r.draw()
*****
*****
*****
```

7. Modify the Rectangle class to make the character that gets printed configurable, but with a default of `X`. Write code to test it.
8. Create Square as a subclass of Rectangle, which does the right thing for a square. Change the default value of the character to `%`But continue to allow it to be overridden.
9. For each of the classes created above in exercises 5-8, implement a reasonable \_\_str\_\_ method and test.
10. For each of the classes created above in exercises 5-8, implement a reasonable \_\_repr\_\_ method and test.

## Additional Topics to Explore

If you're new to Python classes and have gotten through the article and the exercises, that's awesome! We've covered a lot of material in one admittedly rather long article.

If you're still thirsty for more, naturally there's a lot more to Python classes and objects than we've covered here. For example, we haven't covered two somewhat related types of methods, given by the decorators [@classmethod](https://docs.python.org/3/library/functions.html#classmethod) and [@staticmethod](https://docs.python.org/3/library/functions.html#staticmethod).

The literature on object-oriented design principles is vast, but a good introduction is the so-called "Gang of Four" [Design Patterns](https://www.amazon.com/Design-Patterns-Elements-Reusable-Object-Oriented/dp/0201633612/ref=sr_1_1?keywords=gang+of+four+design+patterns&qid=1648570029&sprefix=Gang+of+four%252Caps%252C66&sr=8-1&_encoding=UTF8&tag=codesolid-20&linkCode=ur2&linkId=af4c0cf365baa3f945e23b008a817b01&camp=1789&creative=9325) book. Though some of this work may still apply, in Python a better approach to object design is to first consider whether objects are needed at all, and if so, to ensure those objects that we write are well integrated with the Python data model. By far the best book I've found in this space is Luciano Ramalho's [Fluent Python](https://www.amazon.com/Fluent-Python-Concise-Effective-Programming/dp/1491946008/ref=sr_1_2?crid=6MB6CL75D5JB&keywords=Fluent+Python&qid=1648570375&sprefix=fluent+python%252Caps%252C76&sr=8-2&_encoding=UTF8&tag=codesolid-20&linkCode=ur2&linkId=9e0c7858e1da770a9c0013dac1febbc4&camp=1789&creative=9325).

## You May Also Enjoy

[Python Dataclass: Easily Automate Class Best Practices](https://codesolid.com/python-dataclasses/)

[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)

[Python Format Strings: Beginner to Expert](https://codesolid.com/python-format-strings/)
