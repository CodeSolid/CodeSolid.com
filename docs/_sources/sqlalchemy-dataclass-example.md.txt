---
title: "SQLAlchemy DataClass Example"
date: "2023-02-21"
categories: 
  - "python"
coverImage: "PythonDatabase.png"
---
# SQLAlchemy DataClass Example
One of the features of SQLAlchemy 2.0 was improved support for Python dataclasses. This new feature allows you to convert a SQLAlchemy declarative table mapping into a Python dataclass with a single decorator.

If you're not an old hand at SQLAlchemy, don't worry. Neither was I when I encountered this feature. That's why this article walks you step by step, first explaining why this is something you might want to use and how to use it by means of a simple example. Some of the topics we'll cover are:

- A high-level review of dataclasses and SQLAlchemy.

- Using the SQLAlchemy Object-Relational-Mapping (ORM) declarative table mappings with a dataclass.

- Creating a few such Python/SQLAlchemy dataclasses.

- Connecting to a database and using the SQLAlchemy metadata feature to automatically create tables based on our Python classes. (To keep things simple, we'll use SQLLite3, so we won't have to set up an external database).

- Inserting some real data into the tables.

## Python Dataclasses Overview

As we discussed in [Python Dataclass: Easily Automate Class Best Practices](https://codesolid.com/python-dataclasses/), the Python dataclass annotation allows you to quickly create a class using Python type hints for the instance variables. The dataclass annotation will then automatically create several useful methods, including \_\_init\_\_, \_\_repr\_\_, and \_\_eq\_\_. That article provides much more detail about how to do this, but in general, using the dataclass annotation will do two things:

- It will ensure that the types of your instance variables use Python type hints, making your code more clear.

- It will save a lot of time writing boilerplate code.

## SQLAlchemy Overview

SQLAlchemy is a popular tool that combines a SQL expressions library that can be used on its own with an ORM that uses the expressions library. For many years, SQLAlchemy has been the most popular ORM for Python. The only exception to this popularity is among the Django community since the Django web framework contains and is integrated with its own Object Relational Mapping classes.

## The Data for Our Example

I'm not that vain in the sense of taking endless selfies and posting them on social media, but I do have a similar quirk when it comes to the data from this blog, which I like to download and manipulate. Since the blog runs on WordPress, it features a built-in API I can use to download posts, the categories to which they belong, and other data. Fair warning, if you use this data, it's fairly large since it includes the contents of the posts. However, the dataclasses we'll create will only map a subset of the JSON data that the WordPress API exposes.

With that caveat out of the way, here are the links to the data that we'll use with the code examples:

- [Post Data](https://codesolid.com/wp-json/wp/v2/posts?orderby=date&order=desc)

- [Post Categories](https://codesolid.com/wp-json/wp/v2/categories)

## Creating the Basic SQLAlchemy Dataclasses

Before we get started, we can install the dependencies we need into a virtual environment using the following:

```bash
pip install sqlalchemy>=2.0.0
pip install ipython
```

(IPython is just here so we can easily run some experiments as we go along).

As we can see from the data we're dealing with, we will need at least two entities, Categories and Posts. Setting aside for the moment the issue of the relationship between them, the code below defines a base class for all our SQLAlchemy dataclass objects, then creates the two classes that we need:

```python
# post_tables.py

from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass

class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""
    pass

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(init=True, primary_key=True)
    name: Mapped[str]

class Post(Base):
    __tablename__ = "post"
    id: Mapped[int] = mapped_column(init=True, primary_key=True)
    title: Mapped[str]
    url: Mapped[str]
```

As you can see, when it comes to defining the columns, we've used two different styles. For the primary keys, we use the mapped\_column function in order to be able to specify first of all that it's a primary key and, secondly, that we want the key added to the \_\_init\_\_ method. This is a bit unusual, but in our case, we want to use the original primary keys from WordPress, not create new ones, so adding it to init is what we want. For the remaining fields, we use the type annotated form of mapped\_column, which will add the fields to the \_\_init\_\_ method by default. Both of these forms are [described in detail](https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html) in the SQLAlchemy documentation.

Inside IPython, we can load this code using `%load post_tables.py` . (You'll need to press enter a couple of times to get back to a prompt.

Once this is done, we can try creating a Post. Let's verify that our init method has the fields we want, which we can prove to ourselves by omitting them and seeing the error:

```python
In [7]: post = Post()
-------------------------------------------------------
# SQLAlchemy DataClass Example...
TypeError: __init__() missing 3 required positional arguments: 'id', 'title', and 'url'
```

Supplying the correct arguments, we can create the post object now:

```python
post = Post(42, "Flipping Pancakes in Python", "https://codesolid.com/flapjack")
```

Because the Post class is a dataclass, we also get a \_\_repr\_\_ method for free to display our post object neatly. Here we do that and verify that \_\_repr\_\_ is the method that's being used:

```python
In [11]: post
Out[11]: Post(id=42, title='Flipping Pancakes in Python', url='https://codesolid.com/flapjack')

In [12]: post.__repr__()
Out[12]: "Post(id=42, title='Flipping Pancakes in Python', url='https://codesolid.com/flapjack')"
```

## Implementing a Many-to-Many Relationship

In WordPress, a post can have more than one category, and categories can, of course, apply to more than one post. We can model such a many-to-many relationship with a third table that contains the ID of the two tables we're joining as foreign keys. We must also relate each of the two tables back to the join table.

Here is the posts\_tables.py file with these new features added:

```python
# post_tables.py

from typing import List

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import MappedAsDataclass
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, ForeignKey

class Base(MappedAsDataclass, DeclarativeBase):
    """subclasses will be converted to dataclasses"""
    pass
    
posts_to_category = Table(
    "posts_to_category",
    Base.metadata,
    Column("category_id", ForeignKey("category.id")),
    Column("post_id", ForeignKey("post.id")),
)

class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(init=True, primary_key=True)
    posts: Mapped[List["Post"]] = relationship(secondary=posts_to_category, 
        init=False, back_populates="categories")
    name: Mapped[str]

class Post(Base):
    __tablename__ = "post"
    categories: Mapped[List["Category"]] = relationship(secondary=posts_to_category, 
        init=False, back_populates="posts")
    id: Mapped[int] = mapped_column(init=True, primary_key=True)
    title: Mapped[str]
    url: Mapped[str]
```

Getting ahead of ourselves somewhat, once our data is populated, this will allow us to join and select posts in a given category, for example, using the query below:

```sql
SELECT post.id, title, url 
    FROM post
    LEFT OUTER JOIN posts_to_category 
    ON post.id = posts_to_category.post_id
    LEFT OUTER JOIN category
    ON posts_to_category.category_id = category.id
    WHERE category.name = 'Python Practice';
```

Running queries outside Python requires a separate client executable such as SQLLite3 (see [downloads](https://www.sqlite.org/download.html)). Before we get to that point, however, we need to see how we can use the classes we've developed so far to create and populate the actual SQL tables.

## Creating the Tables and Loading the Data

In the following code, we'll use the ORM dataclasses and the join table we've already defined. Here are the tasks that remain to be done:

- Connect to a database using the SQLAlchemy create\_engine method. Again, we'll use SQLLite since it's simple, runs in-process, and comes with Python.

- Create the tables based on the code we have so far.

- Read the JSON for the categories and posts, and populate the data appropriately.

Here's the code:

```python
#run.py

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import json
from post_tables import Post, Category, posts_to_category

engine = create_engine("sqlite+pysqlite:///./posts.db", echo=True)

def create_tables():
    Category.__table__.create(engine, checkfirst=True)
    Post.__table__.create(engine, checkfirst=True)
    posts_to_category.create(engine, checkfirst=True)


def get_categories_from_json():
    """Loads the categories JSON file and converts the id (key)"""
    with open("categories.json", "r") as fp:
        loaded = json.load(fp)
        categories = {int(k): v for k, v in loaded.items()}
        return categories

def get_posts_from_json():
    with open("posts.json", "r") as fp:
        return json.load(fp)

def save_categories():
    categories = get_categories_from_json()
    with Session(engine) as session:
        for id, name in categories.items():
            session.merge(Category(id, name))        
        session.commit()

def save_posts():
    posts = get_posts_from_json()
    categories = get_categories_from_json()
    with Session(engine) as session:
        for post in posts:
            post_categories = [Category(id=id, name=categories.get(id)) for id in post.get("categories")]
            current = Post(id=post.get("id"), title=post.get("title").get("rendered"), url=post.get("link"))
            print(f'A post {current} with categories {post_categories}')
            current.categories = post_categories
            session.merge(current)
        session.commit()
    

if __name__ == "__main__":
    create_tables()
    save_categories()
    save_posts()
```

On line 8, we create a SQLAlchemy "engine," which is how we connect to the database. The `create_tables` function (beginning on line 10) uses the engine to create each of the three database tables we need to create. The "`checkFirst`" argument is needed to make our Python program re-entrant -- without it, we could only run it once.

On lines 16-25, our two JSON loading functions are relatively straightforward. In the case of categories, however, we convert the primary keys from strings into integers.

In the `save_categories()` method (lines 27-32), we call the load method to get the categories as a list of key/value pairs. We then use a SQLAlchemy Session object to control the transaction. For each of the categories, we call the `Session.merge` function, passing a new Category class constructed from the information we loaded from the JSON file.

As we did when we created the tables, we needed to find a way to make our saves "re-entrant" To accomplish this, we use `Session.merge` rather than `Session.add` to overwrite whatever is actually in the table already, if anything.

Beginning on line 34 save\_posts() is similar to save\_categories(). However, since each post contains a list of categories to which it belongs, there's on line 39, we use a list comprehension to turn this list of category IDs into a list of category objects. We create the post object on line 40, and add the categories on line 42. Finally, we're ready to call Session.merge on line 43. As with save\_categrories(), our last step is to call commit to save our data while still within the context manager for the session.

## Closing Thoughts

Even though this example was somewhat short and perhaps a bit contrived, we've covered quite a lot of ground. In particular, we learned that creating a SQLAlchemy ORM object as a Python dataclass is as simple as adding MappedAsDataclass as a parent (grandparent, etc.) of the class. We saw how to create classes declaratively and two methods for defining fields on the class.

Finally, we learned how to create a database connection, create tables based on our dataclass definitions, and use the classes in lieu of raw SQL to save data to the database.
