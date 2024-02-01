---
title: "Python Configuration: Top Built-In and Third-Party Libraries"
date: "2022-11-10"
categories: 
  - "python-tools"
coverImage: "woman-configuring-equipment.jpg"
---

## Introduction

One of the first things many beginning Python programming tutorials teach is the input function, a simple and beginner-friendly approach to getting input into a program. However, once we get past the thrill of asking ourselves our name so we can change "Hello, world!" into "Hello, Bob!", we realize that configuring a real-world application has many more options than the simple "input" function allows., and that more advanced command line tools usually don't accept input interactively.

Instead, at a high level, program configuration often involves some combination of one or more of the following three techniques:

- Reading the command line arguments passed to the program. The simplest scripts can simply read `sys.argv` for this. More advanced ones will use Python's argparse module or a third-party command line processor such as Click.

- Reading environment variables. This is easy to do by importing the "os" module and reading `os.environ` as though it were a dictionary.

- Reading program configuration from a file.

In this article, we want to focus primarily on the last item here, configuring a Python program using a file. We'll look at several built-in and third-party options for configuration files, and focus in each case on loading configuration from files rather than building and writing configuration files.

## Best Python Configuration Tools: An Overview

Before we begin our detailed discussion of several popular options, let's summarize some of the built-in and third-party libraries that we can use to configure Python applications. We will give examples of some of these in later sections.

<table><tbody><tr><td class="has-text-align-left" data-align="left">Library or Tool</td><td>Availability</td><td>Pros</td><td>Cons</td></tr><tr><td class="has-text-align-left" data-align="left">Simple Python Dictionaries</td><td>Built-in</td><td>Easy to use and understand. Values are of any type.</td><td>No clear separation of configuration and code.</td></tr><tr><td class="has-text-align-left" data-align="left">ConfigParser</td><td>Built-in (Standard Library)</td><td>Many Python versions supported</td><td>Values are always strings. Windows style in files. Somewhat unintuitive.</td></tr><tr><td class="has-text-align-left" data-align="left">Localconfig</td><td>PyPi (pip install only)</td><td>Adds support for dot notation and type guessing to ConfigParser.</td><td>None except additional dependency.</td></tr><tr><td class="has-text-align-left" data-align="left">Json</td><td>Built-in (Standard Library)</td><td>Highly structured. Loads to a dictionary. Wide developer familiarity.</td><td>JSON is verbose to edit. No support for comments.</td></tr><tr><td class="has-text-align-left" data-align="left">Tomllib</td><td>Built-in (Standard Library)</td><td>Extremely easy to use. Format designed for configuration. Supports comments. Typed values. Loads as a dictionary. This is a top pick (see the section below).</td><td>Python 3.11 and later only.</td></tr><tr><td class="has-text-align-left" data-align="left">Toml</td><td>Installable with pip or conda</td><td>Excellent drop-in "replacement" for tomllib for Python versions before 3.11. See tomllib for details. This is a top pick (see the section below).</td><td>None except additional dependency.</td></tr><tr><td class="has-text-align-left" data-align="left">Pyaml</td><td>Installable with pip or conda</td><td>Loads to a plain dictionary, values are typed (not plain strings).</td><td>Yaml is easy to break during editing.</td></tr></tbody></table>

## Python Dictionaries: A Common Structure

Today, English provides a common human language today for technology and business, in much the same way that Latin provided a common language to Medieval and Renaissance Europe.

When configuring a Python application, we can think of the Python dictionary as a common target, in the sense of being a way to model configuration options internally. Many configuration libraries can load a file into a dictionary directly. For others, they load a file into an object structure that 1) behaves like a dictionary in some respects and/or 2) can be easily converted to a dictionary.

## The Python Dictionary as a Configuration Option

If we're going to treat the Python dictionary as a common "target" data structure for application configuration, one question that arises is "OK, so why not use a dictionary directly?"

To some extent, this is actually a viable option. For example, suppose we added a config dictionary to a file, configuration.py:

```python
# configuration.py

"""This is our application's configuration."""
config = {
    "url": "https://codesolid.com",
    "main_topic": "Python"
}
```

This actually works OK, of course, and using it is as simple as importing the config object:

```python
from configuration import config
print(config["url"] == "https://codesolid.com")

# Output:
# True
```

Using code as configuration like this is not all that unreasonable in Python, and in fact, is similar to the approach that Django takes of using [a module with top-level variables](https://docs.djangoproject.com/en/4.1/topics/settings/) as a settings file.

One disadvantage to this approach, however, is that it blurs the line between the application code and the configuration code. For example, QA engineers and system administrators may be comfortable with changing configuration files, but they may be used to the idea that they should "leave code changes to the developers." To the extent that that's true, using code as configuration violates the idea of a separation of concerns. Externalizing the configuration into a non-Python file helps to clarify the intent of the file.

## Python Built-in Configuration: ConfigParser

Python's configparser module is part of the standard library. It lets you parse files in a format that may be familiar to you if you remember old versions of Windows, where the files had an extension of ".ini". So-called "ini files" were organized by sections, as shown here in "example.ini":

```properties
[DEFAULT]
# This is a comment that's supported by configparser
# Items in these sections will be added under all later keys
# unless they are overriden there.
description = "Unknown" 
port = 8888
remote = False

[codesolid.com]
description = "CodeSolid - Python" 
port = 443
remote=True

[localhost]
description = "Jupyter Lab"
```

The code to load such a file takes a little getting used to, but is shown below:

```python
import configparser
config = configparser.ConfigParser()
with open('example.ini', 'r') as fp:
    config.read_file(fp)

print(f"A configuration with sections:  {config.sections()}.")
```

Output:

```bash
A configuration with sections:  ['codesolid.com', 'localhost'].
```

Note that the ConfigParser "config" object is not a loader, per se. So the read\_file method does not load a new configuration and return it, it instead configures the config object itself.

The "DEFAULT" section does not appear when we list the sections. However, those values are used as defaults for any other sections. For example, we don't explicitly set the port in the "localhost" section, so we get the value that was set in the default section:

```python
localhost_port = config["localhost"]["port"]
print(localhost_port)
```

Output:

```bash
8888
```

Although you can treat the config object as a nested dictionary, it does not directly convert to a dictionary structure. However, if you wanted to view it as such (for example, to view the whole configuration at a glance), you could use the following code to convert it and display it:

```python
from pprint import pprint
from typing import Dict

def to_dictionary(config: configparser.ConfigParser) -> Dict:
    """converts a ConfigParser to a dictionary with sections as top level keys"""
    return {section: dict(config[section]) for section in config.sections()}

config_as_dict = to_dictionary(config)
pprint(config_as_dict)
```

Output:

```bash
{'codesolid.com': {'description': '"CodeSolid - Python"',
                   'port': '443',
                   'remote': 'True'},
 'localhost': {'description': '"Jupyter Lab"',
               'port': '8888',
               'remote': 'False'}}
```

We can see in the output above that the types read from the configuration file were never interpreted at all, but instead were loaded as strings. If we know the type we want, however, the configuration object does have some utility methods to support conversions. For example:

```python
print(type(config["codesolid.com"]["remote"]))
print(type(config.getboolean("codesolid.com", "remote")))
```

Output:

```bash
<class 'str'>
<class 'bool'>
```

The third-party `localconfig` module makes

```python
import localconfig
with open('example.ini', 'r') as fp:
    config = localconfig.LocalConfig('example.ini')

print(config.localhost.port)
print(type(config.localhost.port))
```

Output:

```bash
8888
<class 'int'>
```

Here we see the support for using dot-syntax access (for sections and keys that follow Python variable naming conventions only). Also note that the port value was guessed to be an int type, rather than left as a string.

## Top Picks: Tomllib and Toml

Two very similar libraries for reading configuration files that are written in TOML format are tomllib and toml. TOML -- an acronym for Tom's Obvious Minimal Language -- "aims to be a minimal configuration file format that's easy to read due to obvious semantics."[1](https://toml.io/en/)

Tomllib is built-in to Python, but only since Python 3.11. If you're on an older version of Python, the toml library -- which you can install using either pip or Conda -- works in a similar way and produces results that we found to be identical to that of Tommlib in the tests we ran.

Either of these libraries would be an excellent choice for Python Configuration, and the reason is the nature of TOML itself. First, TOML has useful types such as integers (including binary and hexadecimal with the appropriate prefixes), floats, booleans, and even dates, times, and arrays. When parsed, therefore, you don't have to deal with type conversions as you would in ConfigParser.

Secondly, TOML is designed as a configuration file format, so unlike JSON, it is not too verbose to edit. Also, unlike YAML, it is easy to edit it and not make a mistake that will lead you to parser errors.

Overall, TOML's richness and ease of use are part of the reason that the Python ecosystem has moved toward adopting the convention of storing [project metadata](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/#declaring-project-metadata) and build information in pyproject.toml. For example, setuptools now [supports this convention](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html).

Of course, tools like toml and tomllib can be used to parse project metadata in pyproject.toml, or any other custom configuration schema you wish to support for your application.

Let's see how we might parse the following short TOML file, example.toml, which is a modified version of the TOML author's example.

```toml
# This is a TOML document

title = "A Short TOML Example"

[original_creator]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[codesolid_version]
example_modified = true
article = "https://codesolid.com/python-configuration"
constants = [3.14159, 2.71828]
```

Let's try parsing this first with the built-in tomllib library that's available to us as of Python 3.11. To do this we first need to read the file in binary mode using Python's open function.

```python
import tomllib
from pprint import pprint

with open('example.toml', 'rb') as fp:
    toml_311 = tomllib.load(fp)
pprint(toml_311)
```

Output:

```bash
{'codesolid_version': {'article': 'https://codesolid.com/python-configuration',
                       'constants': [3.14159, 2.71828],
                       'example_modified': True},
 'original_creator': {'dob': datetime.datetime(1979, 5, 27, 7, 32, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=57600))),
                      'name': 'Tom Preston-Werner'},
 'title': 'A Short TOML Example'}
```

We can see that the file was loaded for us as a convenient Python dictionary, and we can verify that the types of the values are what we expect.

```python
print(type(toml_311["original_creator"]["dob"]))
print(type(toml_311["codesolid_version"]["constants"]))
print(type(toml_311["codesolid_version"]["constants"][0]))
```

Output:

```bash
<class 'datetime.datetime'>
<class 'list'>
<class 'float'>
```

If we instead use the third-party "toml" library, we get exactly the same results for the format of the loaded data, including the types of the various dictionary values. However, the code to load the configuration is a little bit more concise and convenient, since we can bypass the "open" function.

```python
# Load TOML file if you're not using Python 3.11

import toml
toml_pre_311 = toml.load('example.toml')
```

## The Road Not Taken: JSON and YAML

For reasons we've already discussed, JSON and YAML can be somewhat troublesome to maintain, so they're not our first choices for Python configuration formats. That said, there is support for both formats available to you in Python. In the case of JSON, that support is part of the Python standard library. We covered the issue of how to [load JSON files](https://codesolid.com/python-json-easily-work-with-dictionaries-files-and-custom-objects/#htoc-reading-and-writing-json-files-in-python) in Python separately, so that article can help if that's the use case.

In the case of YAML, you'll need to install the third-party pyyaml module using either pip or Conda.

Here's a sample YAML file we loaded using pyyaml:

```yaml
---
site: "codesolid.com"
subject: "Python"
posts_published: 101
subtopics:
  - Python Tools
  - Python Math and Science
  - Python for Beginners
```

With pyyaml installed, the following code loads the configuration from this file and displays it:

```python
from yaml import Loader, load
from pprint import pprint

with open("example.yaml", "r") as fp:
    yml = load(fp, Loader=Loader)

pprint(yml)
```

Output:

```bash
{'posts_published': 101,
 'site': 'codesolid.com',
 'subject': 'Python',
 'subtopics': ['Python Tools',
               'Python Math and Science',
               'Python for Beginners']}
```
