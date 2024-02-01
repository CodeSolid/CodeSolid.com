---
title: "Large Data Sets in Python:  Pandas And The Alternatives"
date: "2022-11-18"
categories: 
  - "pandas"
coverImage: "pexels-pixabay-210607.jpg"
---

Table of Contents

- [Approaches to Optimizing DataFrame Load Times](#htoc-approaches-to-optimizing-dataframe-load-times)
- [Setting Up Our Environment](#htoc-setting-up-our-environment)
- [Polars: A Fast DataFrame implementation with a Slick API](#htoc-polars-a-fast-dataframe-implementation-with-a-slick-api)
- [Large Data Sets With Alternate File Types](#htoc-large-data-sets-with-alternate-file-types)
- [Speeding Things Up With Lazy Mode](#htoc-speeding-things-up-with-lazy-mode)
- [Dask vs. Polars: Lazy Mode Showdown](#htoc-dask-vs-polars)
    - [Lazy Loading of Rows in Dask](#htoc-lazy-loading-of-rows-in-dask)
    - [Lazy Mode in Polars](#htoc-lazy-mode-in-polars)
- [Closing Thoughts](#htoc-closing-thoughts)
- [You May Also Like](#htoc-you-may-also-like)

Pandas is an excellent tool for representing in-memory DataFrames. Still, it is limited by system memory and is not always the most efficient tool for dealing with large data sets. Beyond a certain point, we even have to set aside Pandas and consider "big-data" tools such as Hadoop and Spark.

Even before that point, we may find we want to optimize performance, especially during data load. We may think nothing of loading a gigabyte dataset or more into memory on a modern machine, but the performance might not be ideal.

In this article, we'll discuss and explore several approaches to this problem. A Jupyter Notebook with the source on which the article was based can be found in this [GitHub repository](https://github.com/CodeSolid/large-datasets).

## Approaches to Optimizing DataFrame Load Times

There are several ways to approach this problem.

First, we might try giving Pandas more information, such as pre-loading the column types when loading CSV, so Pandas doesn't have to add "figuring out the schema" to the other things it has to do during load. Though this works well and saves time, the savings are not substantial, as we'll see below.

Another approach is to save the DataFrame to another file type where the load time can be reduced. Of course, this does beg the question of poor performance on the first load, but it can make subsequent analyses less painful.

Finally, some alternatives to Pandas have appeared that can either load the complete data set faster than Pandas can or that work in a "lazy" fashion, which may only load portions of the data as needed to fulfill a request.

In this article, we'll use the same data set suggested in the [Kaggle Tutorial on Large Datasets](https://www.kaggle.com/code/rohanrao/tutorial-on-reading-large-datasets), the [Riiid Answer Prediction Dataset](https://www.kaggle.com/c/riiid-test-answer-prediction). This is a data set of student test scores over time, which aimed to show how students would perform in the future given their past learning history. More to the point for our purposes, the training dataset (in training.csv) weighs in at some 5.4 Gb, so it's large enough that loading it is a challenge.

## Setting Up Our Environment

To create our environment, we installed a clean Python 3.11 release using conda, then set up a virtual environment using Pip. We did not use Conda to install the packages because some of them had dependency conflicts, so we opted for the (more permissive) pip tool to install everything successfully.

We used the following commands to accomplish this. You can easily skip the first two lines if you don't have Conda installed.

```bash
conda create -n python3.11 python=3.11
conda activate python3.11
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install jupyterlab ipython pandas dask polars fastparquet
```

We timed some initial tests using timeit programmatically, as described in How to Profile Python Code. Still, since timeit can be a bit unwieldy for running several tests, we improved upon some code we found that did a reasonable job of setting up a timer in a context manager, so we could easily test a block of code. Here is that code in timer.py

```python
import time

class Timer(object):
    """Allows setting up a timer as a context manager, for example:
       with Timer("My process"):
           # Code you want to time here
    """
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.perf_counter()

    def __exit__(self, type, value, traceback):
        if self.name:
            print('[%s]' % self.name,)
        elapsed = time.perf_counter() - self.tstart
        print(f"Elapsed time: {elapsed:.2f} seconds")
```

We first wanted to determine our baseline performance for loading the CSV in Pandas as we usually would.

```python
# Read from CSV
from timer import Timer
import pandas as pd
with Timer("Pandas plain read_csv"):
    df = pd.read_csv("data/train.csv")
```

Output (typical):

```bash
[Pandas plain read_csv]
Elapsted time: 35.65 seconds
```

Before dealing with other file types or non-Pandas libraries, let's try the "minimally invasive" approach of making the data types explicit. Pandas tend to load everything as a float64, but we can be more precise about things. Looking at the data using `df.head()`, we can set up the following dictionary of column names to data types for the data that's displayed:

```python
import numpy as np
dtypes = {
'row_id': np.int64,
 'timestamp': np.int32, 
 'user_id': np.int32, 
 'content_id': np.int32, 
 'content_type_id': np.int32,
'task_container_id': np.int32, 
'user_answer': np.int32, 
'answered_correctly': np.int32,
'prior_question_elapsed_time': np.float64, 
'prior_question_had_explanation': object
}
```

With this in place, let's see if we did any good.

```
# Read from CSV with types specified
from timer import Timer
import pandas as pd
with Timer("Pandas read_csv with types"):
    df = pd.read_csv("data/train.csv", dtype=dtypes)
```

Output:

```bash
[Pandas read_csv with types]
Elapsed time: 31.82 seconds
```

OK, we've shaved off a little less than three seconds, so it's something, but it's still not great.

Let's see if we can do any better with a different library.

## Polars: A Fast DataFrame implementation with a Slick API

Polars is billed as a "Lightning-fast DataFrame library for Rust and Python." It features faster read performance (which we'll show in a minute) and a lazy mode where expressions (such as grouping, selecting rows, etc.) are optimized and run in parallel.

As a bonus, I also believe that the expression syntax is often far more intuitive in Polars than indexing methods in Pandas, such as `loc` and `iloc`.

Before getting into some of these advanced features, let's do a non-lazy read of the whole DataFrame in Polars to see how it compares to read\_csv in Pandas. For this operation, the function name we want is the same.

```python
import polars as pl
from timer import Timer

with Timer("Read csv using polars"):
    df = pl.read_csv("data/train.csv")
```

Output:

```bash
[Read csv using polars]
Elapsed time: 9.98 seconds
```

Well, that's much better -- now we're loading the file in about 1/3 the time it took to load using Pandas. In fairness, I should point out that the 9.98 seconds is on the low end of the Polars results, using a brand new kernel. When running interactively in Jupyter Notebook, times of 12-14 seconds are more typical, but that's still a big improvement on the load times for Pandas.

## Large Data Sets With Alternate File Types

In addition to selecting a different library, another approach to improving file load performance is to use an alternate file type. Data files are often available in CSV format. Still, CSV's popularity comes from being human-readable and widely supported, not because it can be loaded quickly for large files.

One issue with this approach is that the libraries that support other file types don't always work in all environments. Especially on my M1 (Apple Silicon) Mac, building these libraries have been problematic. For example, the Pandas "feather" format relies on PyArrow, which is not readily installable (though there may be [workarounds](https://github.com/python-poetry/poetry/issues/3627) if you need to install it).

I've had better luck with reading and writing parquet files using fastparquet. Still, even with this, the to\_parquet method of the Pandas DataFrame threw a data type conversion error after several seconds.

I was able to both write the file and read it back successfully using Polars, and once this was done, it also became readable using Pandas. The downside is that loading the code in Polars from CSV and writing it back to parquet format took about 30 seconds. Once this is done, however, reading the same data set in parquet format sped things up considerably compared to CSV, both for Pandas and Polars. Here are the code and the results:

```python
import polars as pl
import pandas as pd

from timer import Timer

# Be patient, this will take several seconds
df = pl.read_csv("data/train.csv")
df.write_parquet("data/train.parquet")

df = None
with Timer("Time to read from parquet in Pandas"):
    df = pd.read_parquet("data/train.parquet")

df = None
with Timer("Time to read from parquet in Polars"):
    df = pl.read_parquet("data/train.parquet")
```

```bash
[Time to read from parquet in Pandas]
Elapsed time: 7.07 seconds
[Time to read from parquet in Polars]
Elapsed time: 4.51 seconds
```

## Speeding Things Up With Lazy Mode

So far, our discussion of load times has been mainly concerned with a single question: How can we move 5.4 gigabytes (or some similar, large amount) of data as efficiently as possible from disk storage into an in-memory DataFrame so we can further manipulate it?

In this section, we want to take a step back and ask: Is moving 5.4 gigabytes from disk storage to memory the right approach? Reading data and moving it around takes time. (That's always true even for small data sets like the 150 rows and five columns of iris.csv, but for such tiny data sets we don't notice the problem).

Instead of reading it all in data and manipulating it, what if we could plan our query in advance to only load the rows and columns we need for our analysis?

This question brings us to the heart of what Polars calls "lazy mode," but the solution is not unique to Polars. In Spark, both Spark SQL and Spark DataFrames work using a common Catalyst optimizer, a query optimizer that finds an efficient way to fetch data satisfying a group of Spark expressions. Similarly, Dask DataFrames has an API that is similar to Pandas on the face of it, except that data is lazily loaded from a file when compute is called on a query.

## Dask vs. Polars: Lazy Mode Showdown

This section contains some background, a confession, and a spoiler alert.

Let's do it in just that order.

- **The background:** For this article, it was somewhat impractical to review every solution and library we tried to show how lazy loading might work. Developing a large test suite to exercise different queries was also not something we had time to engineer for this article, so we had to make some choices. Specifically, we decided to focus on a simple test case, fetching rows for a given user.

- **The confession:** After I'd run my tests in Dask, I saw this caveat on their [Dask best practices](https://docs.dask.org/en/stable/dataframe-best-practices.html) page. "_For data that fits into RAM, pandas can often be faster and easier to use than Dask DataFrame. While "Big Data" tools can be exciting, they are almost always worse than normal data tools while those remain appropriate."_ This is again proof of the age-old axiom that if you want to hide something from a developer, put it in the manual. So it may be that a really fair test between Dask would be at a larger scale. However, [this benchmark](https://h2oai.github.io/db-benchmark/ "this benchmark") suggests that even at that scale, Polars will do better.

- **The spoiler alert:** OK, I spilled the beans in the last bullet point, but here if you missed it is the spoiler alert. Polars worked better than Dask. A lot better.

I wanted to give you the background and the confession first because I know a lot of time and effort went into Dask, so I don't want any Dask developers or fans to think I walked into this comparison wanting to make it look bad.

Now that we know the result we arrived at, let's share the details of how we got there.

### Lazy Loading of Rows in Dask

Unlike Polars, but like Pandas, many operations for selecting rows depend on what index is set. The Dask documentation advises us to set the index once since it's expensive and to cache it back to the dataframe object.

Let's take a look at the cost of this and the results for retrieving a set of rows from fairly early in the file. (We use both the "dtype" setting and the low\_memory setting on read\_csv to avoid a warning in Dask).

```python
from dask import dataframe
from timer import Timer

import numpy as np
dtypes = {
'row_id': np.int64,
 'timestamp': np.int32, 
 'user_id': np.int32, 
 'content_id': np.int32, 
 'content_type_id': np.int32,
'task_container_id': np.int32, 
'user_answer': np.int32, 
'answered_correctly': np.int32,
'prior_question_elapsed_time': np.float64, 
'prior_question_had_explanation': object
}

with Timer("dask read_csv"):
    df = dataframe.read_csv("data/train.csv", low_memory=False)
    
with Timer("set_index.csv"):
    df = df.set_index("user_id")
```

Output:

```bash
[dask read_csv]
Elapsed time: 0.03 seconds
[set_index.csv]
Elapsed time: 33.62 seconds
```

Note that the read\_csv operation only took about 30 milliseconds. No data is really fetched in Dask until you do a "compute". The next line, setting the index, took about as long as reading the whole file in memory took using Pandas. Let's see if it was worth it as we retrieve the rows for the user with ID 40828; we'll save them as we would to display them or operate on them further

```python
with Timer("Get rows for user_id 40828"):
    rows = df.loc[40828].compute()
```

Output:

```bash
[Get rows for user_id 40828]
Elapsed time: 32.70 seconds
```

Once again, even with the index set, it still took over half a minute to read the rows! Pandas could surely do better than this in memory. In fact, let's find out. This is with the data reloaded using read\_csv in Pandas:

```python
with Timer("Pandas set_index_and_fetch"):
    df.set_index("user_id")
    rows = df.loc[40828]

with Timer("Fetch portion only"):
    rows = df.loc[40828]
```

Output:

```bash
[Pandas set_index_and_fetch]
Elapsed time: 4.29 seconds
[Fetch portion only]
Elapsed time: 0.00 seconds
```

### Lazy Mode in Polars

Now let's see if we can use lazy mode in Polars to just retrieve a few rows. To do this, we'll use the `scan_csv` method, which does not read the whole file in memory as `read_csv` does, instead, it will only retrieve the rows that match the filter expression. We won't have to set an index as we would in Dask or Pandas.

We'll try to select the same user from early in the file as we did with Dask and Pandas, then we'll do the same thing for a user later in the file.

```python
import polars as pl
from timer import Timer 

with Timer("Scan CSV for early user (Polars)"):
    df = pl.scan_csv("data/train.csv").filter(pl.col('user_id') == 40828).collect()

with Timer("Read CSV for later user (Polars)"):
    df = pl.scan_csv("data/train.csv").filter(pl.col('user_id') == 2147470777).collect()
```

Output:

```bash
Scan CSV for early user (Polars)]
Elapsed time: 3.53 seconds
[Read CSV for later user (Polars)]
Elapsed time: 3.10 seconds
```

## Closing Thoughts

I have been looking for an opportunity to evaluate Dask. I'm open to the possibility that it might be worthwhile for other use cases, but it didn't work well for the things I tried. I would be inclined to look at PySpark next rather than spend more time on it.

On the other hand, Polars has turned in some extremely impressive results here.

We began our discussion loading a 5.4 Gb CSV file into Pandas in about 35 seconds, and we're now able to locate and extract rows for a given user in about 1/10th of that time using Polars. Along the way, we were also able to show that Polars loaded large CSV files into memory about three times faster than Pandas.

Pandas still maintains an edge for selecting rows once an index is set (which itself takes about 4 seconds). However, for the "everything in memory case", Polars can still retrieve the same set of rows fairly quickly too (about 90 milliseconds or so).

Given that interactive data analysis involves a lot of ad-hoc queries where you may be doing filtering on different columns, I see this as a win. In Polars, if you want to filter on a different column or set of columns, you don't need to switch indexes to do it.

Another interesting feature of Polars is that it's written in Rust and has a Rust API, which in principle allows the optimization of key operations. I haven't yet been able to demonstrate a significant improvement on file read, so it does appear that most of the time spent here is on simple IO rather than at the Rust/Python boundary. However, but it may be that for other operations there are savings to be had.

## You May Also Like

[How to Use the Pandas GroupBy Method](https://codesolid.com/pandas-groupby/)

[Pandas Practice Questions](https://codesolid.com/python-format-strings/)

[Python Operators: The Building Blocks of Successful Code](https://codesolid.com/python-operators/)

[Python Function Arguments: The Complete Guide](https://codesolid.com/python-function-arguments-and-parameters-examples/)
