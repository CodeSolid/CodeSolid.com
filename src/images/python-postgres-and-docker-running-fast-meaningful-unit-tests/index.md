---
title: "Python, Postgres, and Docker:  Running Fast, Meaningful Unit Tests"
date: "2022-11-29"
categories: 
  - "miscellaneous"
---

Table of Contents

- [Why Testing Databases Is Hard](#htoc-why-testing-databases-is-hard)
- [Database Testing Mistakes](#htoc-database-testing-mistakes)
- [Unit Testing Apples, Running Apples in Production](#htoc-unit-testing-apples-running-oranges-in-production)

## Why Testing Databases Is Hard

Testing database code can be much more challenging than testing other code. This is because the very techniques we've learned to test other code no longer work perfectly well when testing a database.

There are at least three ways in which database testing is more difficult than testing other types of code.

First, a fundamental principle of unit testing is that we test some aspect of our code in isolation from other things. More specifically, unit tests should be completely stateless -- the result of one test should not impact the results of the next. Yet if unit tests should be stateless, a database, in contrast, is as "stateful" as it gets. That's the whole job of a database -- to allow recording and retrieving of application state.

Secondly, testing database code is also challenging because we want our tests to run quickly, yet setting up a database can be a time-consuming process.

Finally, testing a database can be challenging because the teams may be different. As application developers, we can test non-database-related code fine, because we own that code. In the case of the database, a separate team of DBAs may have more final responsibility for the state of the data as well as more domain specific knowledge that we may not have.

## Database Testing Mistakes

Because database testing is difficult, it's an area that's ripe for mistakes.

I once worked on a project that made a classic mistake that developers make when running database tests: testing against an in-memory database.

In this specific case, the team (who worked in Java) had developed an application that ran on MySQL in production, used the Hibernate ORM to access the database, and ran the unit tests against H2 -- an in memory database.

I came onto the team when this stack was mature, and was tasked with fixing a bug that only appeared in the unit tests -- it worked fine in production. Before joining the team, I had several years of experience developing database drivers, so I understood that we were essentially testing against one software stack while running in production against a separate stack, a fact that was completely lost on my application-developer colleagues. They couldn't believe that the behavior could be different since "Hibernate will do the right thing."

I never was able to fix my colleague's misconception that this was a perfectly OK thing to do. In the end, I had to fix the bug by going outside of Hibernate and coding a SQL query by hand that provided the right behavior both on MySQL and against the unit tests. You read that right, _to fix the bug I had to change code that was working fine in production._

Sometimes a team will test against SQLite on developer's machines since it's "easy to set up and remove", but use Postgres (for example) in production. This is another flavor of the same mistake.

## Unit Testing Apples, Running Apples in Production

This article takes as a starting point the idea that the more your test environment differs from your production environment, the more likely you are to have a suite of unit tests that provides low value testing that runs incredibly fast. So

We will develop an example using SQLAlchemy and Postgres, using Docker to set up a baseline database in as little time as possible. Our solution will take have the following features:

- We'll use SQLAlchemy both as our application layer and as a utility to create our test database, taking advantage of SQLAlchemy's ability to apply DDL (Data Definition Language) statements to set up our tables for us.

- Though we won't use an in-memory database, we'll take advantage of Docker Layer Caching and Postgres
