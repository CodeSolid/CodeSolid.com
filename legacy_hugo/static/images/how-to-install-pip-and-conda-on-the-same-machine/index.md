---
title: "How To Install Pip and Conda on the Same Machine"
date: "2022-02-01"
categories: 
  - "python-tools"
coverImage: "coding-with-python-book-small.jpeg"
---

Installing Pip and Conda on the same machine is easy to do with pyenv. Maybe you work on testing a product for different environments, or maybe you just want to try out the two packaging tools to see which one you like best. Either way, pyenv lets you install and manage both with no conflicts.

Table of Contents

- [The Basics First: Pip, Pyenv, Anaconda and Miniconda](#the-basics-first-pip-pyenv-anaconda-and-miniconda)
- [Using Pyenv to Support Both Pip and Miniconda](#using-pyenv-to-support-both-pip-and-miniconda)
- [Closing Thoughts on Pyenv](#closing-thoughts-on-pyenv)

## The Basics First: Pip, Pyenv, Anaconda and Miniconda

For the benefit of those who may not be deeply entrenched Python nerds like me, I should probably back up a bit here and give an overview first. Feel free to skip this section if this is old hat to you. With that, here's an overview of what these tools are:

- **Pip** is probably the best known tool on the list. It is the Package Installer for Python. Pip is how most Python developers third party packages, that is to say, libraries that don't come with Python by default.
- **Anaconda** is a very heavyweight Python distribution, that includes Python, a tool called conda for installing third party packages, and many, many Python packages, especially those that relate to data science. Those who like Anaconda don't mind installing the Internet on their computers in exchange for the convenience of getting straight to work. But for many other folks, Anaconda is a form of bloatware that's unnecessary.
- **Miniconda** is a more lightweight distribution for people who want the benefits of using the conda tool without all the bloat that Anaconda installs. Miniconda installs a Python version, pip, and the minimal libraries needed to run conda.
- **Pyenv** is a tool for managing multiple Python installations. Unlike the `venv` tool, which creates isolated environments for different sets of packages using the default python3 installation, for example, with `pyenv` you can install multiple versions of Python itself. Let's say you have one project that you work on that's on Python 3.6.2, and another that's on 3.10.1, and you need to be able to switch easily between the two. Pyenv lets you do this.

## Using Pyenv to Support Both Pip and Miniconda

Assuming you have a reason to want to support having some projects on your machine based on pip and others based on conda, this can easily be done using pyenv. For more information on pyenv, see our article, [Installing Pyenv on a Mac](https://codesolid.com/installing-pyenv-on-a-mac/). Windows users should follow the [installation instructions for the pyenv-win project](https://github.com/pyenv-win/pyenv-win#installation).

Assuming you have pyenv installed and configured, you likely have a pyenv global configuration already set up. For example, on my case in a directory without a local python configuration set up, I can query the python version and what pyenv is managing locally like this:

```bash
% python --version
Python 3.10.1
% pyenv global
3.10.1
```

I wanted to be able to work with conda, so first I created a directory for conda to manage:

```
mkdir conda
cd conda
```

Next, I queried pyenv using `pyenv install -l` to see if I could narrow down the latest miniconda versions.

```
pyenv install -l | grep miniconda | grep latest

miniconda-latest
miniconda2-latest
miniconda3-latest
```

As a side note, I later learned that the Python version for miniconda that was marked as "latest" in pyenv was not the most recent. It was about two point revisions behind the latest stable release, but this did not impact me. If you leave off the `"| grep latest"` pipe above, of course, you can choose any version more precisely.

The next step is to install the version you want and to activate it locally.

```bash
pyenv install miniconda3-latest
...
pyenv local miniconda3-latest
```

At this point, conda is installed, and you can start using it. (Note, that for certain commands below, you maybe be prompted to run `conda init` and re-start the shell first).

To use conda, we can create a shell and install some starter packages at the same time. For example:

```
conda create --name datasci pandas matplotlib jupyterlab jupyter
```

  
This creates an environment called "datasci" and installs several packages into it. You'll be prompted to continue, and when the installation completes, you'll see something like this:

```bash
#
# To activate this environment, use
#
#     $ conda activate datasci
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

You can now activate the environment as shown, and then run "`jupyter lab`" for example to launch a Jupyter lab environment and start coding in Jupyter notebooks.

Of course, there's a lot more that you can do with conda than this -- for a more complete list, a good starting point is the [conda commands reference page](https://docs.conda.io/projects/conda/en/latest/commands.html).

## Closing Thoughts on Pyenv

The more I work with pyenv, the more I like how cleanly it separates environments, and now that I've learned that being able to control conda and pip environments separately, I'm even more of a fan.

For example, given the example above, from the conda environment, when you're done, simply run "`conda deactivate`" to deactivate the conda environment. At that point, move out of the conda directory (where miniconda is active locally for pyenv), and you're back to a "regular" Python world that you can manage with pip and the venv module.

This gives you complete freedom to try out both tools, and if it turns out you really love conda's way of doing things, you can always install it as the default with "`pyenv global`".

One limitation I'm aware of with this approach is that conda also has the ability to manage complete Python environments -- including different Python versions -- so there's some overlap between what it does and what pyenv does. I suppose if I came from a conda "tradition" that would seem natural to me, but for now I'll manage the global environment -- including miniconda -- using pyenv.
