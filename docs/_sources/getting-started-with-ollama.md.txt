 ---
title: "Getting Started with Ollama"
date: "2025-04-07"
categories: 
  - "AI Engineering"
coverImage: "coding-with-python-book-small.jpeg"
---
# Getting Started With Ollama

## What it Is
If you've been working with online Language models as an AI Engineer -- or even if you've just kicked the tires on ChatGPT or Anthropic's Claude or the like -- you may have wondered if it's possible to run an LLM locally on your own local computer. If so, you're probably ready to test drive Ollama. 

Ollama is a free, open-source tool that lets you run large language models (LLMs) locally on your computer (Mac, Linux, and Windows are supported). With it, you can run and experiment with a variety of large language models, including Gemma3, Llama 3.3, Mistral, and many others.

## Ollama Pros and Cons in Brief
Ollama has several features that make it worthy of a first look. Since all the models run locally, your data never leaves your machine, so it's great for security-conscious users. It's easy to install, without additional dependencies on Docker or other tools.  It's also quite simple to switch models -- you simply specify a different model name (though each model will take some time to download the first time you run it). Running a model from the terminal opens a prompt with which you can interact with the model, as well as an API endpoint, which means you can also use Ollama from LangChain or LangGraph (as we'll demonstrate below). Unlike the case with online providers, you won't have to set up separate accounts and pay a separate minimum fee to get started. Finally, for users familiar with Docker, many of Ollama's commands are quite intuitive, since they have many analogues in Docker commands.

Of course, as with everything in a world of engineering trade-offs, it's reasonable to ask, "OK, so what's the bad news?" The first word in "Large Language Models" gives the game away: LLMs are large (in terms of size), and resource-intensive (in terms of both memory and compute power). On my iMac (with an M1 processor and 16Gb), running gemma3:4b used about 4.5 Gb of memory (and took up 3.3 Gb of disk space), while running gemma3:12b used between 9.2 and 11 Gb of memory (at 8.1 Gb of disk space). Also, the models we're able to run on a typical developer machine run much more slowly and are much less full-featured than commercial models available online.

## Installing and Running

Installing Ollama is quite easy by downloading or running the appropriate installer [here](https://ollama.com/download/). On the Mac program, this consisted of a zip file with an app file inside.  Running this will let you install the app. The first time it runs, the GUI application will prompt you to install the Ollama command line, so you can then run ```ollama``` from a terminal or command prompt window.

Before running anything, it's a good idea to check the [models page](https://ollama.com/search) and look at various "parameter sizes" to find the download size and any system requirements.  I decided on "gemma3:4b", 
The first command I ran was "ollama run gemma3:4b".  As mentioned earlier, the first time you run a given model it will download the model locally, so there'll be a wait for that.  On later runs, it will open the ollama prompt more directly, as shown here:
```bash
> ollama run gemma3:4b
>>> Send a message ("/? for help")
```
At this point you can start ending natural language commands.  Here's a brief session to give you an idea:

```bash
>>> multiply 3 and 7
3 multiplied by 7 is 21.

3 * 7 = 21


>>> my name is John
Hi John! It's nice to meet you. 😊

Is there anything you'd like to chat about, or were you just saying hello?

>>> Send a message (/? for help)
```
(Note: you can exit the prompt using CTRL-D or /bye.)

It's also possible to run ollama non-interactively by passing it a command (in quotes after the model name) Here we'll pass it a two-line command (with backslashes as new lines).  First we set the temperature to zero to focus on a precise and to the point answer, then we'll ask it a mathematical question.

```
ollama run gemma3:4b "/set parameter temperature 0 \What is the square root of 2"
The square root of 2 is approximately **1.41421356**.
```

Since ollama runs at the command line, you can also redirect either input from a prompt or the output from it, or both, as shown here:

```bash
ollama run gemma3:4b < koan.txt > koan_answer.txt
```

The koan.text file consists simply of the ever-popular "What is the sound of one hand clapping?" -- with the answer left as an exercise to the reader and Ollama.

## Saving Sessions and Using Ollama Create

The two main ways that Large Language Models are further enhanced after they are trained are post-training and Resource Assisted Generation (RAG). Post-training seeks to fine-tune a model's performance to add new information or tune parameters to create a new model, so the result is a brand new model.  RAG consists of providing new information such as web search results or other documents to an existing model (typically using the prompt), so the model is unchanged, but in the context of the request, it can provide more accurate results.

Without getting too far into the details of these techniques in this "first look" article, let's take a look at some lightweight ways we can easily create new models using some of ollama's built-in tools. There are two main ways to do this:

* The ```/save <model>``` method can be used to save session from within an interactive prompt.  Note, however, that save does not seem to work with the technique shown earlier of redirecting input to the prompt from a file.
* A more flexible technique for creating new models is to use the ```ollama create <model>``` from a command (terminal) prompt. By default, this looks for a file named "Modelfile" in the working directory, but this can be customized using ```-f <filename>```.

Let's briefly demonstrate these two techniques.

### Using Ollama's /save Method in a prompt.

Let's first see what models we have installed using the list command:

```bash
$ ollama ls
NAME             ID              SIZE      MODIFIED
gemma3:12b       f4031aab637d    8.1 Gb    2 days ago
gemma3:4b        a2af6cc3eb7f    3.3 Gb    8 days ago
gemma3:latest    a2af6cc3eb7f    3.3 Gb    8 days ago
$
```
Your output may be different, of course.  Let's verify that gemma doesn't know our name yet:

```
$ ollama run gemma3:4b "What's my name?"
As an AI, I have no way of knowing your name! I don't have access to
personal information.

You'll have to tell me your name! 😊

Would you like to tell me?

$
```

Next, we'll run a model, teach it our name, and save the session.  The ```/save``` command takes as an argument a name for the model, which can be used to load the model using ```ollama run```.

```
$ ollama run gemma3:4b
>>> My name is John
Okay, John! It's nice to meet you. 😊

Is there anything you’d like to chat about, or were you just letting me
know your name?

>>> /save myname
Created new model 'myname'

/bye
```

Now let's verify that we have a new model, for example:

```
$ ollama ls | grep myname
myname:latest    89694f32b51d    3.3 Gb    5 minutes ago
```

Now let's ask our new model the same question:

```bash
$ ollama run myname "What's my name?"
Your name is John! 😊

I just confirmed it when you told me your name. 😄
```
Gemma is a bit too fond of emojis, but at least this new model has one new fact.

### Using Ollama Create
In addition to saving the current session based on an existing model to create a new model, Ollama's "create" option lets you build a new model from a file containing a base model to build from, parameters to set on the model, and messages to run, and a number of other options (see the [Modelfile documentation](https://ollama.readthedocs.io/en/modelfile) for a complete list).

To give you a sense of how it works, we've put together a contrived example. At present, neither Ollama nor many commercial AI models (Anthropic's Claude excluded) seem to "know" the last line in the movie Cool Hand Luke. (Spoiler alert, I'm about to tell you, so skip to the next section if you plan to view it this weekend.) Granted this is a pretty limited benchmark for intelligence, but I thought I'd teach it to a lightweight model with some facts about me.  Here's the model file:

#### A Sample Modelfile
```

FROM gemma3:4b

# Prefer concise and fact-based answers.
PARAMETER temperature 0.0

# Teach it a basic fact about myself.

MESSAGE user My name is John.
MESSAGE user I live in Charlotte.

# Teach it how to respond correctly to a question about Cool Hand Luke

MESSAGE system You are a helpful movie bot that \
remembers the following information: The complete \ 
last line spoken by Cool Hand Luke in the movie of \
the same name is 'What we got here is a failure to \
communicate.' He has many lines before it, but \
that's the last line, verbatim.
```
By the way, before running this, if you want to see some serial hallucination, try asking "What is the last line Cool Hand Luke says in the movie by the same name?" to gemma3:4b, and it will make up an answer. Ask it the same question again, and it will apologize and make up a different answer.

Now, let's run it to see that answer we get. Note that the -f switch is not strictly needed if you named your file "Modelfile", but it's worth knowing if you want to experiment with more than one file.

```
$ ollama create -f Modelfile coolhand
```
You'll see that -- much like ```Docker build``` -- it will put together a mix of existing layers and some new ones based on the contents of your Modelfile.

Once this has run, you can run the new model as you normally would.  

```
$ ollama run coolhand
>>> My name is John.
>>> I live in Charlotte.
>>> Send a message (/? for help)
```
As you can see, the user messages are displayed, but the system message was not. If we now ask our movie trivia question, we should get the right answer:

```
>>> What is the last line Cool Hand Luke says in the movie by the same name?
The last line Cool Hand Luke says in the movie *Cool Hand Luke* is: 
“What we got here is a failure to communicate.”
```
If you ask it again, this time the model will stick by its guns, so to speak.

## Working With the API endpoint

When Ollama is running, there'll be an api endpoint listening on the default port of 11434, so running localhost:11434 in your browser should show you a status message.  The [Ollama API reference](https://ollama.readthedocs.io/en/api/) lists the various endpoints and gives examples using CURL, but of course you can use any http client such as the Postman, the Python requests library, etc.

I was especially glad to see because Ollama sports an API endpoint, this means that LangChain supports Ollama. LangChain support makes it easy to use Ollama models in a LangGraph application. LangGraph is a very popular tool for creating complex AI agent workflows, and integrating such agents with locally running tolls written in Python.  The [LangGraph course](https://academy.langchain.com/courses/intro-to-langgraph) offers a great introduction to it if you're interested in learning more.

LangChain itself offers a common API for working with LLM models from various vendors.  To show just a simple example, I put together a more basic demo of sending a request to Ollama using a LangChain model.  If you're not logged into Github, [here is the output](/ollama_langchain_demo/), and if you are, see the [source here](https://github.com/CodeSolid/CodeSolid.com/blob/main/src/ollama_langchain_demo.ipynb)


