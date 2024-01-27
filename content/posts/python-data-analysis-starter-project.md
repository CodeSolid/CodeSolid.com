---
title: "Python Data Analysis Starter Project"
date: "2022-12-05"
categories: 
  - "pandas"
coverImage: "colored-scatter-plot.png"
---

## Installing the Tools for the Pandas Series

This article contains the instructions for installing the Python modules that you'll need to run the code in our Pandas Series. If you need to do this, you can skip ahead to the section "Using the Project," or feel free to read the next section for more background.

## Why A Data Analysis Starter Project?

As someone who not only blogs about Python himself but also reviews and publishes work from other authors, I sometimes struggle with the issue of how much detail to provide about project setup and dependencies. I want newcomers to Python to be able to install what they need easily for any article they find on my website, but ensuring this means repeating the same instructions across multiple articles. Yet advanced readers may not need this information, and can quickly install whatever they need.

Because of this, I thought it was time to post at least a minimal "starter project" for the community to use. I believe the minimal set of features for this are as follows:

- It should support the most popular Python packaging tools (pip and conda).

- It must make it easy for beginners with only a recent version of python3 installed to get started, with detailed instructions for what to do.

- It should assume no knowledge of Git or GitHub, but also might be usable as a GitHub template by other users.

## Installing the Project Tools

### Using Pip: (Recommended If You Have Python Installed)

If you already have Python 3.4 or later installed, you can do everything you need with pip and the Python  
"venv" (virtual environment) module.

There are basically three main steps involved.

First, we create and activate a virtual environment from a command prompt:

```bash
# Create the environment:
python -m venv venv

# Activate it (Linux or Mac):
source venv/bin/activate

# If you're on Windows, activate it this way:
venv\scripts\activate.bat
```

Secondly, we need to install what we need. Download this [requirements.txt](https://github.com/CodeSolid/data-analysis-starter/blob/main/requirements.txt) file locally, then run:

```bash
pip install -r requrements.txt
```

### Using Conda

Conda users may prefer using it to the pip instructions above. Also, if you don't yet have Python installed, I've found that [miniconda](https://docs.conda.io/en/latest/miniconda.html) is a great way to manage complete Python environments (even including being able to run different versions of Python).

To use conda to install and activate our data science starter, start by downloading and saving the [environment.yml](https://raw.githubusercontent.com/CodeSolid/data-analysis-starter/main/environment.yml) file.

Next, run the following two commands to create and activate the environment:

```bash
conda env create -f environment.yml
conda activate data-analysis
```

## Running and Using Jupyter Lab

At this point, you're ready to start coding any notebook in the Panda Series. You can launch an interactive notebook to do this with the following command:

```bash
jupyter lab
```

## What's Included in the Starter Project

In addition to Jupyter, the starter project includes Seaborn, which also gets you access to Pandas, NumPy, and Matplotlib. We've also included scikit-learn, the popular machine learning package for Python with many built-in tools for data preparation beyond those provided by Pandas alone.

If you try to import something and get an error "ModuleNotFoundError: No module named (whatever)" you may need to install an additional module. You should stop Jupyter Notebook, then install the module, then re-run it. Use `pip install [package-name]` or `conda install [package-name]`, as appropriate.

## Next Steps

If you're new to Jupyter Notebook and want to read more about getting started with the tool, you might check out [Jupyter Notebook: A Complete Introduction](https://codesolid.com/jupyter-notebook-a-complete-introduction/).

Our [Pandas category page](https://codesolid.com/python/pandas/) features many articles about various aspects of using Pandas to get you started, while the [Learn Python](https://codesolid.com/learn-python/) page indexes not just our Data Science articles, but many more general Python articles you may find useful.
