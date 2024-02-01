---
title: "Simplicity is your Friend:  PyCharm vs. VS Code for Teaching Programming"
date: "2021-12-05"
categories: 
  - "python-tools"
---

![](/images/simplicity-is-your-friend-python-vs-vs-code-for-teaching-software/pexels-koolshooters-9944253-1024x683.jpg)

Recently, I have been doing a lot of work trying to understand what tools I want to use in the software development course / boot camp I’ll be teaching.  I’ve had a good idea of course topics I want to deliver for some time now: 

- Markdown, Git, and GitHub in the early lessons, so that we can emphasize the skills needed to build public, attractive portfolio projects from the outset.

- Core Python from a beginner level to intermediate.  The initial lessons at the beginner level should be appropriate for those for whom Python is a first programming language.  

- More advanced Python topics later in the course.

- Special projects and specialty/career focused topics.

  
Honestly, the outline fell into place fairly easily, but it has been more of a chore selecting the tools for the students to use.  My own preference at my day job is to use JetBrains’s PyCharm for most of my Python work, while using Visual Studio for more lightweight file editing tasks and the superior developer experience for Markdown.  I was thinking of going in the same direction, using the community version of PyCharm for the course.  For some time, I even considered making portions of it available using their cool EduTools plugin.

Finally, though, several factors convinced me to just do the whole course in Visual Studio Code:

- The overhead of switching between two development environments, one for Python and one for Markdown and quick edits, is fine if you’re a veteran like me who likes his quirky workflow.  For or beginner programmers, in contrast, a course where they have to switch between tools while trying to ramp up on a version control system and their first programming language really is a bit much.  Having a single IDE really is a win here.  Moreover, VS Code is a tool that students with some experience in other languages may already know.

- The JetBrains EduTools plugin is a cool tool for self-checking coding tests and the like, but it changes the developer experience while working.  For example, when code is run in the standard fashion (without the EduTools plugin “Check” button), the output is not automatically displayed as it is for a non-EduTools project.  I don’t really want to be teaching the plugin.

- More importantly, Visual Studio Code has two mature remote development options that integrate well with GitHub:  Gitpod and Codespaces.  See [this article](https://www.freecodecamp.org/news/github-codespaces-vs-gitpod-cloud-based-dev-environments/) for a comparison, but my own take so far is that Gitpod will better fit the bill.  JetBrains lags far behind in this area, with remote development tools that are slower and more difficult to set up.  Moreover, their proprietary backend (“Space”) does not have the universal cachet of GitHub.  

- JetBrains Fleet is their lightweight, remote-friendly editor that might integrate better with Gitpod (maybe someday).  At this point, though, all indications are that they’re promoting it as connecting to their “Space” back-end. For now, it’s only available to certain early experience users, so whatever hotness it may have in the future we can deal with when it gets here.

- I’ve done some further work in Visual Studio Code over the last few days to validate that it has sufficient features to be used for most basic debugging and testing needs. Yes, the tools for run configuration are a little more user-friendly in PyCharm, but the way one does it in VS Code are nothing I can’t get my head around enough to simplify for my students.

## You May Also Like

[Pycharm vs. VS Code: Which Is Better and Why?](https://codesolid.com/pycharm-vs-vs-code/)

[How to Profile Python Code](https://codesolid.com/how-do-i-profile-python-code/)
