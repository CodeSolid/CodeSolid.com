---
title: "Is Python Slow?  Separating the Myths from the Facts"
date: "2022-01-17"
categories: 
  - "python"
coverImage: "footreace.jpg"
---

Yes, it's true that Python is slower at runtime than some other languages, but it's fast enough for the tasks for which it is commonly used. For the most common tasks, the popular libraries use well-optimized C code -- but you don't need to know C to use them. We separate the facts from the myths.

As someone who writes extensively about Python, naturally I would love to be able to tell you that Python is amazingly fast -- but that simply wouldn't be true. For really speed critical uses like Kernel Development, GPU drivers, and embedded computing, C would be a much better choice. Ironically, that's the first language I spent serious time learning -- so clearly there's something else about Python that I love.

You could discount my position, I suppose, if I were a lone voice in the wilderness arguing a minority position, saying things like "OK, people, stop what you're doing and go learn ALGOL!" But as I write this, Python is the most popular programming language, at least according to the top three Google results and other research I've done on my own both on search engines and job boards.

That's a weird result for a slow language. What's going on? Is Python really fast in some respects? Is there something else about it that people love? Are changes in the industry responsible?

We're going to dig into all that. Read on!

## Python vs. Java Performance: Long Running Speed vs Cold Start

Naturally, whenever we talk about one programming language being slow, we're not talking about it in isolation. We're talking about it in comparison to some other language. A popular language to compare Python performance against is Java, another language that is compiled to bytecode like Python before it is executed.

It is true that for a long-running process, Java executes tasks much more quickly than Python. But pay attention to the qualifier there: "for a long-running process". Java takes a few milliseconds to start up, and this long "cold start" time is one of the reasons that Python has become the tool of choice for serverless environments like AWS lambda. AWS Lambda allows you to run a single function to execute a task, and bills both on the memory consumed and the duration that the function is running.

To give you an idea of how this works out with a simple example, let's look at the performance of loops, since it's a favorite target of the "Python is slow" argument. Let's display some representative results for counting to a million in Java and Python:

```bash
Elapsed time for 1 million count Java was .161 seconds
Elapsed time for 1 million count Python was .100 seconds
```

Python doesn't look that slow in this case, does it? But don't worry, Java fans, if we let the Java process run long enough to pay the heavy startup fee, it can win the race quite decisively. Here we use the same code to count to 10 million:

```
Elapsed time for 10 million count Java was .234 seconds
Elapsed time for 10 million count Python was 5.160 seconds
```

##   
What is Python Used For?

Guido van Rossum, Python's creator, [wrote in 1999](https://en.wikipedia.org/wiki/Guido_van_Rossum#1999_%22Computer_Programming_for_Everybody%22_proposal) that he designed Python to be intuitive and easy to use, and "\[suitable\] for everyday tasks allowing for short development times". Long considered a scripting language or a "glue language" for doing things like testing C libraries, Python has now become a favorite tool of Data Scientists and specialists in Machine Learning -- as well as for general scientific computing.

This enthusiasm stems from the fact that Python allows for rapid interactive development in tools like Jupyter Notebook and IPython. Moreover, for data science and general scientific work, a huge majority of the important libraries like Pandas, SciPy, and TensorFlow are not pure Python. They either consist C, C++ code, or another high-performance language wrapped in Python code. Many are based on or work with NumPy, a library written in C.

Are there comparable libraries, for example, for Java? Yes, there are, but I haven't found any evidence that their popularity even comes close to that of NumPy. Google trends, for example, shows sixty-four queries per day on average for NumPy, and zero each for "SciJava" and "Java JAMA". (In the latter case, I originally saw some results without "Java" added, but recall that JAMA is also the "Journal of the American Medical Association", and even with the doctors thrown in, NumPy had better search volume).

## Development Speed vs Runtime Speed

In the simple loop benchmarks we discussed above, we saw that startup times of Python were much better than for Java, but Java was faster for long-running processes. Yet for scientific computing and data science, the Java libraries trailed far behind those of Python.

How are we to account for this? Is it that the Java libraries are just worse? Well, they might be, but I suspect if there were enough demand to do data science in Java, they would improve. And in fairness, Java does figure prominently for many big data tasks where pure processing speed is an advantage, like Hadoop MapReduce. But in data science and machine learning generally, the mind share advantage overwhelmingly belongs to Python. So I don't think the libraries are to blame here.

Instead, what accounts for the difference in popularity between the Java data science stack and the Python one is the convenience, developer productivity, and ease of use of the language itself. It is simpler, easier, and faster to get things done in Python than in Java. I'm not saying this as a guy who only knows Python and so it's easy for me -- I say this as someone who quite honestly has more years of development experience in Java than in Python. Python is a more productive language, both for beginners and experienced developers alike.

If the only measure of the success of a programming language were raw machine performance, Python wouldn't win -- but neither would Java, because Java itself is slower than C.

I'm tempted to say that if all we cared about is performance, we'd all be coding in C. But I know that if I do, there'll be a disgruntled Assembly Language programmer lurking somewhere to call me to task. Yes, even C is slow if you frame the argument correctly.

Looking back over my own career, the history of the languages I've used most often roughly maps a progression from "faster and less convenient" to "slower and more convenient". Beginning with C and C++, both highly performant languages, I later learned Java and enjoyed it because it was more convenient, partly because of automatic garbage collection, and partly because it was a simpler language syntactically than C++. Much later, when I really started to work with Python, the rapid productivity and less verbose code had me saying no to Java opportunities whenever I could.

## Python Is an "Interpreted" Language

People will sometimes say that Python is slow because it is interpreted, which sounds like it has a certain plausibility. They'll then make the claim that it has to be compiled every time it is run, and that actually is not quite right. For a script that hasn't changed since it was last run, Python can use a cached, binary version of the script to prevent having to compile the code again. You're familiar with this if you ever created a built a package for distribution, or even if you've run enough Python and wondered about those \_\_pycache\_\_ folders and .pyc files that are left lying around.

It's probably more correct to say that the Python runtime is dynamic and more purely object-oriented than other languages, so the runtime spends more time on things like type checking and exception handling than it might otherwise.

## Python and the GIL

In addition to processing speed, another detail that we should also discuss in the context of speed is the fact that Python is effectively single-threaded, as a result of something called the Global Interpreter Lock, or GIL. The Python GIL prevents deadlocks and other issues that typically crop up in multithreaded code from affecting the execution of Python bytecode. This effectively means that generally speaking, Python runs in a single thread, and this is true even in the case of using the `threading` package.

There are a number of ways to speed Python up to the extent this is the issue you're dealing with. We can only discuss these at a high level here, but check the Python documentation for more information. In addition, Brett Slatkin's "Effective Python" has an excellent chapter devoted to concurrency and parallelism that goes over these topics in much greater depth.  
  
First, it's important to understand that the threading package still works fine if your processing is I/O-bound, and needs to run a limited number of I/O-bound tasks. Threads do come with an overhead, however (in Python and in other languages), both in terms of memory and in the time involved in switching between them. So they are only appropriate for managing a small number of I/O-bound tasks simultaneously. To handle much larger numbers of simultaneous I/O tasks efficiently, Python 3.7 introduced coroutines. Coroutines are defined using the `async` keyword, and called using `await <function_name>` To use coroutines, the main event loop needs to be started by an `asyncio` function such as `asyncio`.`ru`n.

For true parallelism, that is to say, running Python code on multiple cores for tasks that are CPU-bound, you can use the `multiprocessing` package. If you used threads in your code but found that you were still running into CPU bottlenecks, you'll find that the multiprocessing package has an interface that's intentionally quite similar. This is also true of other packages that allow you to run threads or processes. For example, code that uses the `ThreadPoolExecutor` class in the `concurrent.futures` package can easily be made to run on multiple cores by swapping it out with the `ProcessPoolExecutor` class instead.

## Library Selection and Other Self-Inflicted Wounds

Many times that "problem with the language" is not a problem with the language at all, it's a problem in my code or someone else's on my team.

I was on a team once where we evaluated and chose a third party library for a REST API we were working on. This API seemed to be promising as it offered non-dictionary data models that were strongly typed and validated. However, there was an unintended consequence of this choice. Since the REST API handled data that was doing three-dimensional geological mapping, one of the core elements of the request contained a list of three-dimensional points as x,y,z coordinates. Since there could easily be several million points sent, we found that the fact that the data validation the library we were using was doing on each point was slowing the request to a crawl. Our solution was to write hand validation for the rest of the request, and to remove the library altogether, treating the list of points as a simple JSON list.

My point here is that even though Python is not as performant as Java or C, if things have really crawled to a halt, blaming the language should be a last resort. I've been successful in troubleshooting a few Java performance issues in the past as well, and they always boiled down to a bug in our codebase.

## Future Improvements

Python's original design goals were to create a scripting language emphasizing simplicity, readable code and developer productivity. As we've seen, although high performance wasn't an original design goal, the scientific and data science communities contributed libraries based on C and other high-performance languages.

Still, the core Python development team is working to improve the performance of "native" Python. For this subject, I can strongly recommend a fascinating article entitled [Guido van Rossum’s Ambitious Plans for Improving Python Performance](https://thenewstack.io/guido-van-rossums-ambitious-plans-for-improving-python-performance/). The video interview touches on performance only briefly but is still interesting. The rest of the article gives a lot of helpful background and links on the topic, showing what the core team will be working on for the next several releases.

I'm for one am looking forward to seeing what they can do, and I'll continue working in this "fast enough" language where I can be highly productive in the meantime!

## You May Also Like

[Learning C++ and Python: The Perfect Duo for Success](https://codesolid.com/learning-c-and-python-the-perfect-duo-for-success/)

[How to Profile Python Code](https://codesolid.com/how-do-i-profile-python-code/)
