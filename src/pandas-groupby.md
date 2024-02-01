---
title: "How to Use the Pandas Groupby Method?"
date: "2022-09-08"
categories: 
  - "pandas"
coverImage: "programmer-with-coffee.jpg"
---
# How to Use the Pandas Groupby Method?
## Contents

- [What is The Pandas Groupby Function?](#aioseo-what-is-pandas-groupby-function)
- [Sample Data We'll Be Using](#aioseo-example-of-data-for-using-pandas-groupby-method)
- [Splitting Data into Groups Using Pandas Groupby](#aioseo-splitting-data-into-groups-using-pandas-groupby)
    - [Creating a Group Based on One Column](#aioseo-creating-a-group-based-on-one-column)
    - [Creating Groups Based on Two Columns](#aioseo-creating-groups-based-on-two-columns)
    - [Grouping By Three Columns](#aioseo-grouping-by-three-columns)
- [Getting a Specific Group](#aioseo-getting-a-specific-group)
- [Pandas Groupby Output Format](#aioseo-groupby-output-format)
- [Iterating Through Groups in Pandas Groupby](#aioseo-iterating-through-groups-in-pandas-groupby)
- [Finding the Percentage of Grouped Data](#aioseo-finding-the-percentage-of-grouped-data)
- [Different Built-in Functions](#aioseo-different-built-in-functions)
    - [Aggregation](#aioseo-aggregation)
    - [Filtering](#aioseo-filtering)
    - [Transformation](#aioseo-transformation)
    - [Apply](#aioseo-apply)
- [Saving Grouped Pandas DataFrame in Different Formats](#aioseo-saving-grouped-pandas-dataframe-in-different-formats)
    - [Saving a Pandas DataFrame As a CSV File](#aioseo-saving-pandas-dataframe-as-csv-file)
    - [Saving Pandas DataFrame as an Excel file](#aioseo-saving-pandas-dataframe-as-excel-file)
- [Summary](#aioseo-summary)
- [You May Also Enjoy](#aioseo-you-may-also-enjoy)

## What is The Pandas Groupby Function?

The groupby function in Pandas is a powerful and versatile tool in Python. Using this method, we may split our data, apply different operations to different subsets, and then merge the final results. This may be used to process enormous amounts of data for various computations.

This tutorial will cover splitting, grouping, and selecting data from Pandas groupby. By the end, you will have a solid knowledge of Pandas groupby. You can easily apply this method to your dataset and save it as CSV and Excel files.

As part of this tutorial, we will use a CSV file with not so much data for training purposes. You can [download](https://raw.githubusercontent.com/CodeSolid/CodeSolid.github.io/main/booksource/data/AQ.csv) this file later and practice on your own.

## Sample Data We'll Be Using

Our dataset csv file (AQ.csv) contains the following data:

```
Country,Air Quality Index,Year,Status,Continent
Bangladesh,173,2021,Poor,South Asia
Chad,147,2021,Poor,Africa
Pakistan,131,2021,Poor,South Asia
Tajikistan,116,2021,Poor,Central Asia
Mongolia,107,2021,Poor,Asia
Uganda,99,2021,Moderate,Africa
United Arab Emirates,95,2021,Moderate,Asia
Uzbekistan,90,2021,Moderate,Central Asia
India,88,2021,Moderate,South Asia
Kyrgyzstan,61,2021,Moderate,Central Asia
```

<table><tbody><tr><td></td></tr></tbody></table>

Now let’s open our example CSV file and see our data using the Pandas `read_csv` function.

Let's use the Pandas `read_csv` function to look at our sample CSV file and its contents.

```python
# importing pandas
import pandas as pd

# openning our csv file
df = pd.read_csv("AQ.csv")

# showing the content of our CSV file
df
```

Output:

![Table
<div></div>
Description automatically generated](https://lh5.googleusercontent.com/Yz_G_OM2Rz9P7lHSPdmlol4fA4V2lW6otWmBBYzxx6lhXtWajbMuszs6kcfNyF9grlVHudEm2oZNXRSvwnuEgF-3lZF8LhU_AxwMGVny-hVvCay3a68nWrRVSx0vf7Cn5a7JytoKTlmmJ6MDmjKu3-fmVqGwpIZjpnb8PPtfxeWeT5TyapaTS8ND0Q)

## Splitting Data into Groups Using Pandas Groupby

In the result above, we can see that we have at least three categories by which we can group our data: "Year", "Status" and "Continent". To group our data by, for instance, the continent, we can type `df.groupby('Continent')` given that your DataFrame is called "df" and that the column is called "Continent".

We are going to use the groupby method to group a DataFrame based on one, two, three, or more columns.

### Creating a Group Based on One Column

Now let’s start with the simplest example – grouping data by one column. 

```python
# grouping data by one column
cont = df.groupby('Continent')

# printing the dataset after using 'groupby' by 'Continent'
print(cont)
```

Output:

```bash
<pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000018F426AC760>
```

The result shows us that we have successfully created a group of pandas objects, but, in general, it gives us nothing. In the output, we can see that whenever we try to use the print function to see our grouped data, it prints the object, not the data itself inside the object. 

Let’s now look at the group we just created using the ‘group method’. 

```python
# printing the data from the object using groups method
print(cont.groups)
```

Output:

```bash
{'Africa': [1, 5], 'Asia': [4, 6], 'Central Asia': [3, 7, 9], 'South Asia': [0, 2, 8]}
```

Notice that in the output above we see the grouped data with indexes. Now, let’s show it in the table:

```python
# showing the groups in the table using 'count' method
print(cont.count())
```

Output:

![A picture containing text
<div></div>
Description automatically generated](https://lh4.googleusercontent.com/qJufc7IcMLbMjKK5m6HORSXlwGehwK0cQRdyW63MdPLS3ZrKEeulzPQI6j1slMSehsYey_MW85cJLYXTbrXIkx3rMoSVuNVKHZNHxdA8EOL6QVA8-JwGX0LWx0qB8IeyRgHRsh3iKng6sak-Heh3tFZOAACBJnT2luWBi38gzmtAroJAO8KxmM1Shw)

This was all about how to group DataFrame based on one column. Let’s proceed with the grouping based on multiple columns.

### Creating Groups Based on Two Columns

```python
# grouping data by two columns 'Status' and 'Continent'
AQ = df.groupby(['Status','Continent'])

# printing grouped data
print(AQ.groups)
```

Output:

```bash
{('Moderate', 'Africa'): [5], ('Moderate', 'Asia'): [6], ('Moderate', 'Central Asia'): [7, 9], ('Moderate', 'South Asia'): [8], ('Poor', 'Africa'): [1], ('Poor', 'Asia'): [4], ('Poor', 'Central Asia'): [3], ('Poor', 'South Asia'): [0, 2]}
```

To show it in the table using `count` method like in the code below:

```python
# showing the groups based on two columns in the table using 'count' method
print(AQ.count())
```

Output:

![Table
<div></div>
Description automatically generated](https://lh5.googleusercontent.com/POCM5YVdku0TeUk2KDEI6FpC-Fe8LLsjsVsdYC_8tJw4DrgYiR3-BI6ZkhT72UX9Kw5qQtOXYVMJx7gQ9TFXYL2sUfD4necpExGhPMR7Z8kky5gSio8Wam-J0pEhvr1EgJGxMPOBBM18_vl_n5ZxajANttdgv00qiBRZDETYkf_fwkLH2W2V4GHppA)

### Grouping By Three Columns

Use the same idea for grouping by three columns and showing the grouped data in a table.

```python
# grouping data by three columns 'Status','Continent' and 'Country'
AQ = df.groupby(['Status','Continent','Country'])

# printing grouped data using ‘count’ method
print(AQ.count())
```

Output:

![Text
<div></div>
Description automatically generated with medium confidence](https://lh5.googleusercontent.com/916l7Q2oJf8-MXVESkGxJmk-NoLgdtdkT9T4rMIBjvjzTHOuqdt2_9JWqk2rCVPgCA3h8rmxROssudhEKQHeqh1dEtKyPW30y1_Z_yz3dcjNnnIZncyJV6SJrPwME1kyKxKYX46RAUJSiPAteMP4ol-EOhLDciUFbkd9XqKF--dcREgo03gF54I_dw)

## Getting a Specific Group

If we have multiple groups, we can select one of these groups as shown below.

```python
# calling 'get_group' method to access a specific group from all the groups
groups.get_group('Asia')
```

Output:

![Table
<div></div>
Description automatically generated](https://lh3.googleusercontent.com/_eOPsoA_MkOI8O_UXcNdx4H6nhui1vw-27t91z8xS5jh210dzcvxWkB6X2nL7UnsXm9vdaKeGh9XP57yx5TA1KDmyKqW6kgufWVxvTTDJtc8JRW-uFAXO5yVNrUndmSF9z-kf9XPWbDRze3ksmQvXi2NFGomoHsI9JVlTU74ntrcAMAoTk9p6mUBHw)

Using `get_group` to multiple values:

```python
# creating groups by two columns
groups = df.groupby(["Continent","Status"])

# calling 'get_group' method to access to two grouped columns values
asia = groups.get_group(("South Asia","Poor"))

# printing the result
print(asia)
```

Output:

![Text, letter
<div></div>
Description automatically generated](https://lh3.googleusercontent.com/Q2GSHQXuvvr_PQt2swGsjbW-jLZXSVF7r_o_qBX9VE9pyV-qWg4hx4rLA-FIjKOxDjESyaKbiHjqETy_4-3BQLjBWJu-NIHX-cpOsgs_SR2c0pvWqSgOfztia413rrfw5Koa1UVeGvl9e984l_XwwkwvV0wy8uCutPGQzWT-kMxldFUVwQW8GKoOMQ)

The results show us that we printed only countries with the “Poor” status from the “Continent” group’s column “South Asia”.

We can also apply different aggregations to a specific group using the same `get_group` method and any other aggregation functions.

```python
# calling 'get_group' method to access a specific group from all the groups
asia = groups.get_group('Asia')

# applying mean() function to the specific column
mean = asia['Air Quality Index'].mean()

# pinting the mean
print("Air quality index's mean value of Asia is", mean)
```

Output:

![](https://lh3.googleusercontent.com/dDXL74qKGhpyw0WJB43cRMIcphcYZbpJs0eOLbj7yefGMZlAnSkWyHLMu-h3BcO1kTTMnaHpiJu3b_5LbA17V04698AQZ87LT0O8SZDXwKxn8Qa-Nj4kZjouuwukB3fw8ssqDzBTIi9PKxCzyyIBCaxcRdca4AXORGg5qyg2IoV6A69Er0CFgRsVgA)

## Pandas Groupby Output Format

The output of groupby and aggregate operations differs between Pandas Series and Pandas DataFrames, which can be confusing. 

Typically, if you compute the result with more than one column, your result will be a DataFrame. For single-column results, aggregation functions will generate a Series by default. We can change this setting by selecting a different operation column:

```python
# producing Pandas Series
# using 'mean()' method to find the average air quality index for each continent
# rounding the mean using 'round()' function

round(df.groupby('Continent')['Air Quality Index'].mean(), 1)
```

Output: 

![Table
<div></div>
Description automatically generated](https://lh4.googleusercontent.com/Zf7-Q6lBzpegUmhEqNFIV1r_gP-hraKbKYk3YcNJeC9FScnTkmUDIuXeczxzevZHT_kF9Y-ZnTKFJRMp1g4YJ3D5ZBkSHUpicyf0hZyIOo41FKNY2C1qZBz5zeZ5_bz_OWi8i4F5SvDB4eFiM7movzZkougKd8XbZKWpaI3TyB-PZIIDP2Bfy09oUQ)

Output in this case is in Pandas Series. 

Now let’s try to get Pandas DataFrame as a result:

```python
# producing Pandas DataFrame
# using 'mean()' method to find the average air quality index for each continent
# rounding the mean using 'round()' function

round(df.groupby('Continent')[['Air Quality Index']].mean(), 1)
```

Output:

![Table
<div></div>
Description automatically generated](https://lh5.googleusercontent.com/DMDBChdUI5oEd-Ew09Ou_RDPf3WB-KqFz5-idj_ft3E_ZXPGKiq6NAa3sEBX91Rvbnt0ZLJwOPoi7MVxRpldjW2YEJjRCSSkXmwCm0GymcF2pu3wxh-sV4xXTaTxShVTca_FmqWZEN8A8t_siKkI_-JUfHUrFqarSKRaIvEu9pZLcyyGbJM2y_bm0g)

This way we can get different output formats depending on our request.

## Iterating Through Groups in Pandas Groupby

We already know how to use Pandas groupby function with one and multiple groups (columns), which is returning pandas object, which is iterable. 

Now let’s iterate through the objects using the for loop and print the data.

```python
# impoting pandas
import pandas as pd

# openning dataset
df = pd.read_csv("AQ.csv")

# creating group based on one column using pandas groupby method
groups = df.groupby("Continent")

# iterating over groups using for loop
for continent, value in groups:
    print(continent)
    print(value)
```

Output:

![A screenshot of a computer
<div></div>
Description automatically generated with low confidence](https://lh3.googleusercontent.com/VSCrtflKpURrnDz8FUPmDFeRmgoVamjzh9K-c1Mr37JW5flpp-vHMbgjTaA-0zTJtg3M7TemilTJySt8YveoKP07JCIfIqnbc6Uby_T7DuBePk2n4xkNw0iaQCVpUjBxV2d7LbhglkSCG3BUMEegI0N9WybdhWS_UtYoPG_4KOZ5-zp55bfzGhj8ZA)

Now let’s see what the result will be if we will iterate through two groups:

```python
# creating group based on two columns using pandas groupby method
groups = df.groupby(["Continent","Status"])

# iterating over groups using for loop
for continent, value in groups:
    print(continent)
    print(value)
```

Output:

![Text
<div></div>
Description automatically generated](https://lh5.googleusercontent.com/tnkUa61gB04d8kRLQOv7AnXGd-F0vXyooHTcC1Tnm2TdqI-_C4tUupzSu4RUxcIFqCKJZiaf0mPWeleH2tYJ1RKlP2l6TeVQG8SB_6FerHrYeVw5K7iJ7BPoM82wKeegn3tr13bC4x3YP5R1ox-uZtUOW_QvoEJy3STha78RkYSAiCaqUfQ9-qwEpw)

In the same way, let's try to use for loop for the three groups.

```python
# creating group based on three columns using pandas groupby method
groups = df.groupby(["Continent","Country","Status"])

# iterating over groups using for loop
for continent, value in groups:
    print(continent)
    print(value)
```

Output:

![A close-up of a document
<div></div>
Description automatically generated with medium confidence](https://lh6.googleusercontent.com/c4Fy-2pK5NO0dx_9IET07AT4Jo1dOa2ibuOrYdkz-kDAIYpjkN2Cgzap4gASbSWgKVAiGhEjhL40qerbD6zSJteVQdJkIBdp6hrUoijYn01VdLtjlCRjnZCSW9ctm2-kx3jWtPfTq0xyEVWpBoyr3LRsfjcFfDZb_UujpwLx4tADpRvc31VqWpyAcA)

That was all about using for loop through one and multiple columns. 

## Finding the Percentage of Grouped Data

Moreover, we can use different functions over our grouped data. For example, let’s use a lambda function to see the percentage of the grouped data.

```python
# creating groups by three columns

# applying 'size()' property to represent the number of elements in this object
groups = df.groupby(["Continent","Status"]).size()

# calculating the percentage on the level of status for each continent using lambda function
perc = groups.groupby(level=0).apply(lambda x:100*x/float(x.sum()))

# showing the result
print(perc)
```

Output:

![Table
<div></div>
Description automatically generated](https://lh3.googleusercontent.com/g0keTahtmN3mbWM5anK9ly0PamrNdGXTe3In64cRQ64ccq3_6PavfSytVHy7OgAWwNu7aA8_vBodWKwpkmsRH8LcwoStv1Rj-J_YdxY1uW94AQ7u1nm2KHbupBLndh_qg3DPPijYhgbtfcEw0LaLjJVsWVg_42p8IGxcZ4b0qvKImuREPCnsqHq4yg)

## Different Built-in Functions

Up to this point, we used `mean`, `count`, and other functions, which are built-in Pandas aggregation, but they’re not the only ones.

The following table summarizes some other built-in Pandas aggregations:

<table><tbody><tr><td><strong>Aggregation</strong></td><td><strong>Description</strong></td></tr><tr><td><code>count()</code></td><td>Total number of items</td></tr><tr><td><code>first(),&nbsp;last()</code></td><td>First and last item</td></tr><tr><td><code>mean(),&nbsp;median()</code></td><td>Mean and median</td></tr><tr><td><code>min(),&nbsp;max()</code></td><td>Minimum and maximum</td></tr><tr><td><code>std(),&nbsp;var()</code></td><td>Standard deviation and variance</td></tr><tr><td><code>mad()</code></td><td>Mean absolute deviation</td></tr><tr><td><code>prod()</code></td><td>Product of all items</td></tr><tr><td><code>sum()</code></td><td>Sum of all items</td></tr></tbody></table>

Take a look at this example:

```python
# using describe function over each continents' air quality indexes

df.groupby('Continent')['Air Quality Index'].describe()
```

In this code, we’re using `[‘Air Quality Index’]` to specify over which group we want to apply a describe function. 

Output:

![Table
<div></div>
Description automatically generated](https://lh5.googleusercontent.com/TNFzvs9FdIRNDqBHgHYUqZjDl5sAYXt_dMCKW6oQ-0R0_9-34J485HCvaMAKedch2n5BSSjb7zpz-trsT8w0t9YkxMqUn-QClYGELaDqTlCETF3wJFiajqiMCygBC2LghsJz3wd2fqiZigHBUPy0y8zzl3ObO1qty1R4km5ggYdvjloglFOwKXkKtA)

Before it, we mainly used built-in functions separately like `mean()`, `sum()`, etc. Still, groupby objects have `aggregate()`, `filter()`, `transform()`, and `apply()` methods that easily execute a bunch of useful operations before combining the grouped data.

### Aggregation

The `aggregate()` method allows us to use several different aggregations and compute all of them at once.

```python
# importing pandas 
import pandas as pd

# importing numpy
import numpy as np

# using multiple aggregations like min(),mean(),max()
agg = df.groupby(["Continent","Year"]).agg([np.min,np.mean,np.max])

# printing the result
print(agg)
```

Output:

![Table
<div></div>
Description automatically generated with medium confidence](https://lh5.googleusercontent.com/39zXn0s3u5DHU6vfKnViCkUdVZoAnSaBM4Y_jWw-d5dap_wOpphPhEqY36TcG56MINifV7PHxV96lCGXrAqb6RyJRF1y8C3mYkrOpnFHippdOUlbHSUp0iwhvGI7bea7A0CfrIu8ttGHboJ8EpuQhDDQhD9cyLEho96gkL_YWmWtrRXeBtvFBpeNmw)

In the output, we see that we implemented three functions at once to get each continent's minimum, mean, and maximum values of the air quality index. 

### Filtering

The `filter()` operation allows us to discard data based on group properties. For example, we may want to keep only one needed group with some needed properties.

```python
# importing pandas 
import pandas as pd

# reading dataset
df = pd.read_csv("AQ.csv")

# applying filter() method to our dataset
groups = df.filter(['Continent', 'Air Quality Index'])

# grouping by continents
groups.groupby("Continent").mean()
```

Output:

![Table
<div></div>
Description automatically generated](https://lh6.googleusercontent.com/jNDpfxSM8DjCWq-0CxxdlgIu7Hjeo2MpNY4vWu6qGSY9UfvcBp7OzZEVYZIPuHFyjk9grSZgtilzrh1m5TfIMSTrLAUg-cm2Xb7I9m5o0tFXK9mdczlJhjfOGnHYkNYL3eHbwxI_ZIBJDvPjLsAKOZJt80p3c_A2xV5Ucswa0IuYOr6evRRGmFw08w)

### Transformation

The `transform()` function returns a transformed version of the entire data for the recombination. The output result has the same form as the input before.

```python
# defining function of square 
def function(x):
    return x**2

# getting air quality index from a data frame
AQI = df['Air Quality Index']

# using transfor function over air quality index
print(AQI.transform(function))
```

Output:

![Table
<div></div>
Description automatically generated with medium confidence](https://lh5.googleusercontent.com/jn8KseUc3jUCrxBbxjhxxa_YyqZBP-0l_v0-EbmIqMQASWdVcX_zVkCkHSe7zbJarMf-ilfJwEaU35MV7lEBgTeuXosuSFSJmyCfteMfIPC52PTrITr61Ikj0cOdUMQWdzZ7lbEGwfjc7P9cGKYkIVSbX7UCw2h4O7S5qglKJg463-EZT4QKoev5hg)

###  Apply

Apply() function allows us to apply various other functions to the groups.

```python
# applying lambda function 
AQI = df.groupby(['Continent'])['Air Quality Index'].apply(lambda x: x - x.min())

# printing the result
print(AQI)
```

Output:

![A picture containing table
<div></div>
Description automatically generated](https://lh3.googleusercontent.com/jG3wLGuvSWGkZBv3XVoY5Z4COnTeQZUWWMtTnZdeFG9HjDJRtmwF6qFtigwiAtITtMe8YZFs-KmeMYUbxyVME0ktUA2jOJIT7M_PDGoQDDlubFOp10njqYhh9CUbTWM44ldxnccn3N1UDaPRukfiNoDUj240UtinZuOK7J3_D-LHN27EadetA87TAg)

## Saving Grouped Pandas DataFrame in Different Formats

In the last section of this tutorial, we’re going to learn how to convert our groupby to CSV and Excel files. However, do not forget that we must reset our indexes for both types of data savings. 

### Saving a Pandas DataFrame As a CSV File

To save our data as a CSV file, we will use `to_csv` method. See the example below:

```python
# importing pandas
import pandas as pd

# reading our datset
df = pd.read_csv("AQ.csv")

# grouping by the continent
groups = df.groupby(['Continent'])

# resetting index and finding size of the elements in each continent
my_df = groups.size().reset_index()

# converting groupby to csv file using to_csv function
my_df.to_csv("grouped_file.csv", index = True)

# checking saved file 
check = pd.read_csv("grouped_file.csv")
print(check)
```

Output:

![Table
<div></div>
Description automatically generated](https://lh6.googleusercontent.com/6U4XJjNFbdSepLZnaq9jxrOcs0eAL1uImW9nFUlWcL_W_5mfy1hgZAoqr6Q2cl2pRSYs8E4lFRKeszS1Ki5mzhr0V95wGorSsJJ9eIoNs-L6MFsd8ClbAhn5FXhR0zeiDSe-tJZ1DRFDjuCpKXsrc4mskdCxtHFqtgLvmhIvcQYP7m0PPec9D-B7dQ)

### Saving Pandas DataFrame as an Excel file

To save our data as an Excel file we will use `to_excel` method. 

See the example below:

```python
# importing pandas
import pandas as pd

# reading our datset
df = pd.read_csv("AQ.csv")

# grouping by the continent
groups = df.groupby(['Continent'])

# resetting index and finding size of the elements in each continent
my_df = groups.size().reset_index()

# converting groupby to excel file using to_xlsx function
my_df.to_excel("grouped_file.xlsx", index = False)

# checking saved file
check = pd.read_csv("grouped_file.csv")
print(check)
```

Output:

![Table
<div></div>
Description automatically generated](https://lh4.googleusercontent.com/ztJfBT2aEreLPI0hMV41wukzsQymYh8R5RR-YuOKLIpqC4r-3_7EfkiTby4keilRqJhd9mbwgP7lsf-ZypAUyX2a1jF3oAcwHm7rgar7WrQe9Oarf5YYPDlu1Ko71b79SqMwb1PHOuPlej6_VZ2AYgHy8cpzG2xzcIz_nT3WbkzRQ_j5ZBFs3Alprw)

## Summary

In this tutorial, we looked at the groupby function, which divides our data into different groups by category. The result of the groupby function is iterable, indicating that we can iterate the groups independently, using various functions at each step of the process. We've looked at how to select a particular group and how to work with them. We also learned how to apply different aggregations to one or more groups and finally learned how to save our data as CSV or Excel files.

## You May Also Enjoy

- [Pandas Examples and Review Questions to Make You an Expert](https://codesolid.com/pandas-practice-examples/)
