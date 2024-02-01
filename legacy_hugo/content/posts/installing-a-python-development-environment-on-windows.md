---
title: "Installing a Python and Git Development Environment on Windows"
date: "2021-12-29"
categories: 
  - "python-tools"
---

I recently posted a two-part video tutorial to our YouTube Channel that detail the steps for installing the following tools on Windows to have a complete Python and Git development environment.

To help you walk through the steps, I've also prepared an edited transcript you can refer to if you want.

Part 1 is below.

[Part 2 is here](https://codesolid.com/installing-a-python-and-git-development-environment-on-windows-part-2/) when you're ready, and covers installing Visual Studio Code and the GitHub Command Line Interface.

Part 1 Contents

- [Video](#htoc-part-i-video)
- [Transcript Introduction](#htoc-transcript-introduction)
- [Overview of What We'll Be Doing](#htoc-overview-of-what-we-ll-be-doing)
- [Installing Windows Terminal](#htoc-installing-windows-terminal)
- [Installing Python for Windows](#htoc-installing-python-for-windows)
- [Validating the Python Install](#htoc-validating-the-python-install)
- [Installing Git for Windows](#htoc-installing-git-for-windows)
- [Making Windows Terminal Use Git Bash By Default](#htoc-making-windows-terminal-use-git-bash-by-default)
- [Conclusion of Part 1](#htoc-conclusion-of-part-1)

## Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/jZIjOLV5jZ0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Transcript Introduction

In this video, the first thing we’re going to need is to get our tools set up so that we could start to do our work. Now we’ve got a lot to do, don’t let it intimidate you. There are several tools we need to install, let me show them to you now. 

## Overview of What We'll Be Doing

First, we want to install Windows Terminal. This will allow us to set up an environment that looks pretty much the same on Windows and Mac. That way, I can teach on the Mac and you can follow along on Windows. And 99.9% of what we’ll be doing will be exactly identical. Where it’s not, I’ll point out what the differences are and there’ll be no problem with that. 

The next thing we want to install on Windows will be Python so we can write our code and test it and debug it. The next thing will be Git so that once we have code written, tested, we can publish it. And also, so that we can go back in time and we can get back to an earlier state of our code if we find we’ve made a mistake somewhere along the way. 

Next on the list, Visual Studio Code, this is a very good general-purpose editor that also handles Python quite well, in addition, and we can set up a nice development environment and a development workflow in Visual Studio Code. It’s also a useful editor for other programming languages you may encounter, so it’s a nice general-purpose tool. It also has the advantage of free, as all the rest of these tools are, by the way. 

And then finally, one last tool that’s really optional, but I love it because it makes working with GitHub a lot easier than it would be otherwise, we want to install the GitHub Command Line Interface or CLI. 

## Installing Windows Terminal

So, with that, let’s pause the slideshow and let’s go into our most useful programming tool, and that’s Google. And we’ll go in and we’ll just start get started with the Windows Terminal. If we look up Windows Terminal, we can click through here. And now this is going to ask us to bring up Windows Store—Open Microsoft Store. Sure, go ahead and do it. And we’ll click on Install. Okay, now that that’s done, let’s go ahead and click on Open here. And as you can see, I’ve moved it over from my other monitor.

There is one more thing I like to do with Windows Terminal, or with any terminal software, and that is to pin it to the taskbar. So let me go ahead and do that now. I’m going to go down here to hover over the icon that represents the Windows Terminal, and I’m going to right-click on it, and just click "Pin to Taskbar".

## Installing Python for Windows

The next thing we want to do is to install Python on Windows. On Windows 10, Microsoft has made this really simple to do, because they have a version of Python, the installer for which is already on your system. So, all you have to do is essentially type “python” and it will bring up the Microsoft Store. That will install Python, and it does it correctly.

So, let’s go ahead and do that right now. Let’s just go to the Terminal prompt for the Windows terminal app that we just installed, and let’s type python. That’s going to bring up the Microsoft Store version of Python 3.9 in this case. I’ll go ahead and click Install here. And as always, we’ll pause that because it will take some time to install. And when it finishes, we’re not going to even have to do anything else. 

## Validating the Python Install

So, let’s go in and validate our installation real quick and make sure Python got installed correctly. Let’s go to our back to our terminal window and let’s type python again. But this time, let’s add two hyphens, a couple of dashes and the word “version”, all lowercase. And that’ll give us the Python version that’s installed. And sure enough, it’s 3.9.9 which is just what we expect. 

Let’s do the same thing for a program called PIP, that’s P-I-P. And once again, we’re going to type two hyphens and version. And we see the PIP version which is kind of unimportant to us but what is important is at the end, it says it’s pointing to Python 3.9, which is what we want, we want to make sure that PIP doesn’t point to a Python 2 version we may have kicking around. 

So, with that, Python is completely installed, and we’re ready to go on to the next section. 

## Installing Git for Windows

In this next part, what we want to install is Git for Windows. Now, Git for Windows has a lot more options to choose from and the installer, but we’ll walk through that together. So first, let’s go to our favorite program or helper, Google, and let’s find where Git for Windows can be located. Let’s type in Git for Windows here. Sure enough, this top one, the Gitforwindows.org, that is fine. And right here, we’re going to go ahead and download it. And we will accept the default location for Git and click Next. 

In this next dialog, we have a lot of things to look at. Let’s go ahead and put the additional icons. Windows Explorer Integration? Yeah, let’s leave that as it is. The rest of it, let’s leave all of that as it is. And then the final thing we want to check is this “Add a Git Bash Profile to Windows Terminal”. Remember, we just installed Windows Terminal a couple of programs ago, and this will allow us to all be on the same page by using a bash style terminal. And let’s click Next at this point. 

Here, it’s prompting for the window that we’re going to create. Let’s go ahead and click Next. Now here, it’s asking for a default editor that Git is going to pull up. Let’s leave that as vim for now. At this window, let’s override the default branch name for new repositories. And you see here that it suggests main. There’s a long history to this, but long story short, GitHub is now using main instead of master as the default branch. So we want to be compatible as possible with GitHub to save us some steps, so let’s click Next. 

Here, we want to leave the default. We want to have Git available from the command line and from third party software. We don’t want to use it from bash only. And we don’t want to override this because that will change the behavior of some of our Windows programs. So let’s go ahead and go Next. Here we want to install an external Open SSH. So let’s select that. Here we want to use Open SSL library so we’ll leave that as it is. Click Next. 

This is a good option to have; this is basically Windows and UNIX have different lifestyle endings. This will make sure that if you’re working on Windows, you’ll always have Windows lifestyle endings while you’re working. But when you check things into Git, it will have Unix lifestyle ending so people on Unix will be okay, that’s sort of the standard. And then they of course set their machines up so that it always uses Unix lifestyle endings. So that way you’re compatible no matter who you’re sharing code with. Let’s go ahead and click Next. Here, let’s leave the default. Let’s leave the default here. 

Here, we’re asked if we want to use a credential helper. Let’s leave that as is. Here, we’ll just click Next. And here we’ve reached the final batch of settings finally, and we will go ahead and just leave these as is and we’ll click Install. Once again, we’ll pause the video. 

When the installation finishes, it will ask you if you want to view the release notes. I am going to uncheck that. And then it also asks if you want to launch Git Bash. Let’s take a look at that really quickly. Let’s click Finish here. And that will launch a terminal prompt with Git Bash as the default. Now what we want to do—and if you’ll remember, we checked the box to say add this sort of terminal to our Windows Terminal program which works a lot better and is a lot easier to see, quite frankly. So let’s go ahead and get rid of this bash terminal, and let’s set that up now.

## Making Windows Terminal Use Git Bash By Default

If we go over back to our Windows Terminal program that we installed earlier, and we have it in the taskbar. If you click this little down arrow over here—we’re not seeing it yet, but if we close this and go back in and now click the down arrow, you can see that Git Bash is available as an option. Let’s do one more thing. Let’s go into settings. In the settings, what we want to do is we want to pick our default terminal and our default terminal, we’re going to set it to Git Bash, and save. 

Now to test that out really quickly, let’s go back into Windows Terminal one more time, click on it. And Git Bash comes up as the default. Just to test that we have Git available on our path, let’s just type Git. Let’s try version—that’s always a good trick to see if we can try. And sure enough, Git Version 2.34.1 for Windows and so forth. 

And Git does not change that frequently, so if you have a slightly different version than this, I would not worry about it. The same is true of later Python 3 versions, whether you’re on 3.8, 3.9, or a later version of Python, this course should still continue to work perfectly well with those versions as well, because we don’t do a lot of version-specific stuff in this course, as you can imagine. So, at this point, we can type exit out of the Windows Terminal. And that will close Windows Terminal, and we’re ready to take a look at what we’ve done so far. 

## Conclusion of Part 1

Well, as you can see, we are more than halfway through, and especially that last Git for Windows install, that was a beast, wasn’t it? The rest of them will go fairly easily. But we are almost out of time for this video. So, with that, let’s cut it short for now and in our next video, we’ll go ahead and install Visual Studio Code as well as the GitHub CLI. We’ll set up Visual Studio Code so that it uses the same terminal we set up Windows Terminal for, so we’ll have a nice, consistent developer experience all throughout. And we’ll see you in the [next video](https://codesolid.com/installing-a-python-and-git-development-environment-on-windows-part-2/). Thanks for watching!
