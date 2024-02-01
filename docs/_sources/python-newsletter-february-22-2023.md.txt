---
title: "Python Newsletter February 22, 2023"
date: "2023-02-22"
categories: 
  - "newsletter"
---
# Python Newsletter February 22, 2023
Hi From CodeSolid!

I realize it’s been a while; I just got back from a lovely vacation in Colombia.  I realize you’re not hanging on my every word, but let me nevertheless tender a self-serving “Sorry for the delay.”  Here’s the latest from CodeSolid and around the web.

## New On CodeSolid

[SQLAlchemy Dataclass Example](https://codesolid.com/sqlalchemy-dataclass-example/)  
The recent release of SQLAlchemy 2.0 included improved support for mapping database entities as Python dataclasses.  I wanted to check this out, so I wrote a brief example featuring some data from my blog as input.  I used SQLLite3 to avoid having a complicated database setup, so it’s pretty straightforward.

## Around the Python Interwebs

[Switching Between Data Streams in a Single Thread](https://rednafi.github.io/reflections/switching-between-multiple-data-streams-in-a-single-thread.html)  
Redowan Delowar wanted to be able to use generators to consume two data streams simultaneously, without using separate threads or processes.  This interesting article was the result.

[Discussion of Python Projects Using “Best Practices”](https://www.reddit.com/r/Python/comments/111y9o2/python_projects_with_best_practices_on_github/)  
This Reddit thread is worth a look if you want to get a feel for what projects the “Python community” thinks are well-maintained, worth learning, or otherwise representative of Python practices.

[Doggy Morse Code](https://github.com/Trainraider/doggymorse)  
Speaking of “best practices”, newcomers to Python often ask “What project should I work on?”  Here’s a project that proves: 1) It doesn’t matter, just so long as you’re practicing and 2) You should do something whimsical because… 3) See #1.

[A Python Derivative Calculator](https://www.reddit.com/r/Python/comments/1184ijg/i_made_a_derivative_calculator_using_python/)  
Here’s another “side project” that’s quite a bit more advanced than Doggy Morse Code.  It’s notable too for the sources it quotes

[Happy Birthday to Python](https://tomaszs2.medium.com/happy-birthday-python-you-31yo-bada-b94aaa59e15f)  
Python turned 32 a few days ago.  I hope it likes the nice newsletter I got it.

[Polars List of Resources](https://github.com/ddotta/awesome-polars)  
As readers of this blog may know, I’m a big fan of [Polars as an alternative to Pandas](https://codesolid.com/alternatives-to-pandas-python-polars/).  This curated list of other resources about Polars is a good starting point for learning more about this awesome Python library.

[Installing NGINX, Gunicorn, Uvicorn, and FastAPI](https://dylancastillo.co/fastapi-nginx-gunicorn/)  
This tutorial shows you how to launch a single, production-ready FastAPI instance fronted by NGINX as a reverse proxy.  This is a good introduction to all the pieces, but one drawback is that it teaches them as a somewhat manual, interactive process (rather than automating it all as a DevOps engineer might want). 

[New VS Code Python Extension Release](https://devblogs.microsoft.com/python/python-in-visual-studio-code-february-2023-release/)  
The February 2023 VS Code extension release is one I need to check out since it boasts a feature that’s been on my wishlist for some time – the ability to automatically detect a Python environment when launched from a terminal with a Conda environment or virtual environment (venv) active.
