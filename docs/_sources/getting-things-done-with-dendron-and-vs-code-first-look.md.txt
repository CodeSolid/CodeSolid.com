---
title: "Getting Things Done With Dendron and VS Code -- First Look"
date: "2021-12-18"
categories: 
  - "miscellaneous"
tags: 
  - "getting-things-done"
  - "gtd"
  - "visual-studio-code"
---
# Getting Things Done With Dendron and VS Code -- First Look
Last week, I wrote an article about [Getting Things Done (GTD) using VS Code](https://codesolid.com/2021/12/11/getting-things-done-with-github-markdown-and-visual-studio-code/), and one of my smart colleagues suggested I take a look at the Dendron extension. I've been using this extension fairly heavily since then. I've also been figuring out how I want to integrate it into a GTD workflow. Since Friday is the day that I've set aside for my "weekly review" and I just completed the first one, I thought I'd take a moment to share my thoughts about Dendron VSCode.

## The Good

- Cmd-L (Or Ctrl-L on Windows). This brings up the lookup window, which is by far Dendron's coolest feature. I can look up an existing note or create a new one from the keyboard, instantly. Once in the lookup window, I can choose "Create New" or type a few letters of what I'm looking for, a down arrow or two, and BAM! I'm there. So if I want to review something -- my inbox or next-actions pages, for example -- I can do it in about 3 seconds.
- The information hierarchy. Dendron files are simple markdown that you can organize any way you like by filename. For example, for getting things done, I have several files in the pattern project.\[project-name\].md files. This article, similarly, was originally drafted as: "writing.getting-things-done-dendron-first-look.md".
- Dendron supports wiki style links `[[link]]`, with intelligent lookup there too. If I wanted to link to my inbox from for example I can type the first two brackets + in, hit enter to select it, and done!
- Great tagging support. Just enter a hashtag, for example: "#some-category". Dendron will treat that as a document - tags.some-category.md. All by itself, a whole blank document for a tag sounds pretty silly, but Dendron's backlink view means that if you're in that document you can follow the links to whatever documents are tagged that way.

After a while, this system of linked information really does start to feel like the interconnected neurons in a second brain. And there you have the origin of the name "Dendron" as well.

## The Bad

- My initial new user experience with Dendron was pretty dismal, but I tried to reproduce it a moment ago, and it looks like an update pushed two days ago took care of some of that. It looks like Dendron now can either set up a global style "Second Brain" or integrate well into your existing VS Code project. I've since added a Dendron "vault" (folder) to an existing project I have for my coding course development, and that worked quite well. So this was a really needed update. Still, it's prudent that you make such changes on a git branch or the like, or otherwise back up your work before you add Dendron.
- The calendar view is not easy to navigate. Today for my weekly review I had to add some appointments to next month, and it was more of a chore than it needed to be. An easy way to add a new "daily.journal.\[date\].md" file (calendar entry) from the command palette or look up "today" would be a great addition! For me that's not a deal-breaker, as I don't often schedule things, but if your use case relies heavily on scheduling or appointments or the like (managers, salespeople, etc.), Dendron is not best suited to the task.

## The Indifferent

Dendron has support for schemas. I haven't yet found them useful yet, since they seemed a bit heavy to set up for my needs at this point. However, if you really want to describe and organize the hierarchical structure I mentioned above, schemas are the way to do it.

## Overall Impressions

If you're a VS Code user already and want to organize your notes and projects in an intuitive way, get Dendron -- it's absolutely awesome. Except for a few rough edges, I am really a fan. I'm writing this post in a Dendron-enabled project now, for example, so that should tell you something. It also supports a "Getting Things Done" workflow extremely well. However, you will have to spend a little time thinking about how you want to set up contexts, projects, and the like, as Dendron is not a dedicated GTD tool.

## Try It Yourself

Like all Visual Studio Code Extensions, you can browse and [install the extension in the usual way](https://code.visualstudio.com/docs/editor/extension-marketplace#_browse-for-extensions). Simply browse for "dendron" and install it. You can read about Dendron on the [Dendron Wiki](https://wiki.dendron.so/).
