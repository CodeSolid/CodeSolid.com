---
title: "Mastering The Take-Home Coding Exercise: A Simple Checklist To Make It Shine"
date: "2021-12-07"
categories: 
  - "learn-to-code"
---
# Mastering The Take-Home Coding Exercise: A Simple Checklist To Make It Shine
Like it or not, many companies have now started giving their software development job candidates take-home coding problems. Many of these are fairly non-trivial, meaning you'll spend a weekend or more on them before you even get a serious interview at the company you're applying for.

However, as with so much in life, a Tina Turner song provides the answer: "But I never lost a minute of sleeping / Worrying 'bout the way things might have been."

Admittedly, Proud Mary wasn't purpose-written for this article, so let me make the point more plainly: If you're going to invest that much time in working on a coding exercise, you should try to do everything you can to be successful at it. It's not like burning a weekend for a job you don't have yet is a fun game like Scrabble, so if you're going to play at all, you might as well play to win.

Before we begin, let me point out that some of the suggestions here may involve skills you haven't developed fully yet or tasks you won't have time for before submitting. That's totally OK. If you're not yet interviewing, you may have time to develop some skills before you do. If you're working on the exercise right now, you may not have time for all of this. If you don't, don't worry about it (we have a tip for that too -- see the last bullet item in the checklist).

## Take Home Coding Problem Checklist

- The most important thing you need to do before using anything else on this checklist is to read and understand the exercise the company you're interviewing for gave you, and finish whatever it says there. You should do this a couple of times:
    - Read it once carefully at the outset, and spend some time making an outline or notes of what you need to do _to be successful at the task as it's written._ If anything about the exercise problem is unclear, go back and ask for clarification if you can. Then get to work on the exercise as written, not this checklist. Make frequent git commits - losing work stinks!
    
    - When you're "done" with the exercise, before you move on to the rest of the checklist, read the exercise problem again. If you have time to catch any remaining issues, do that first.

- When you're done with the exercise, go back and remove any undone "to-do" notes and comments that include dead code or are otherwise ugly.

- If it makes sense for the standard of the code you're working on, document each function, or at least the non-trivial ones, with a short comment about what it does, what it takes as input and returns, etc. Also, make sure your names (variables, functions, event handlers, etc.) are descriptive of what they do. "function foo" may be cute in a tutorial, but production code uses descriptive names.

- Have you handled errors that might arise, especially from things like database calls, Ajax API calls, file operations, and the like? Are your error messages descriptive, and, if appropriate, do they tell the user how to recover from the error?

- Now is a good time to add a Markdown document, README.md, at the project's root with a basic line or two about what the project is (even though they know) -- this can even borrow language from or reference the assignment.  It should also have a section on how to build/run it (e.g., \`\`\`npm start\`\`\` or whatever).

- Does your editor have code formatting, or do you have a code linter installed? If so, commit your code first to save your work, then run it! Anything you can do to improve the formatting of your code at this point is a win.

- I realize you may not have much time left after the final features and clean up, but if you do, think about adding some unit tests, if you haven't already done so. If you have unit tests, you should also add instructions on running the unit tests to the README, "Running the unit tests:  \`\`\`npm test\`\`\` (or whatever)."  This might be good to do even if your coverage won't be complete.  (See next point too). 

- Anything you DON'T have time for, don't sweat it.  Now back in the README, you could maybe have a section:  
      
    \## Next Steps / Future Stories:  
    \* Demo to the team.  
    \* Add more unit tests to improve coverage.  
    \* \[Whatever else you can think of that you might have left undone\]  
      
    Note that the first bullet item suggests that you want to demo your work.  This is really a bit of sales technique that "closes" them to give you another chance to talk to them and the rest of the team.  It also shows you're proud of your work and not afraid to explain/discuss the choices and tradeoffs you made. You might also make the same offer in your email when you send it. 

## Final Thoughts

Once again, if you're going to spend a weekend or more on a company you're hoping to work for, you want to do everything you can to be successful at it. Having a checklist is a valuable tool that can help you remember what you want to review. It can also help before you even get in this situation to practice writing unit tests, crafting a good README, and using third-party tools to help enforce a consistent coding style.

In the end, remember, we all do what we have time for. If we're successful, great! If we're not -- that's more practice for the next time. Keep working at it, and I'm sure you'll make it look easy in the long run.

## You May Also Enjoy

[Pycharm vs. VS Code: Which Is Better and Why](https://codesolid.com/pycharm-vs-vs-code/)?

[Learning Git: What to Know When You're a Beginner](https://codesolid.com/learning-git-what-to-know-when-youre-a-beginner/)

[Python Classes Zero To Expert: A Tutorial With Exercises](https://codesolid.com/getting-started-with-python-classes/)
