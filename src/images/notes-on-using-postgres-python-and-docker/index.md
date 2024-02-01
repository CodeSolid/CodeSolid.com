---
title: "Using Postgres, Python, and Docker"
date: "2022-12-08"
categories: 
  - "miscellaneous"
---

PostgreSQL advertises itself as "the most advanced open source relational database", and because of that, it is an excellent skill to have in your toolkit. Although production Postgres databases often don't use container technology such as Docker, being able to use Docker and Postgres together has some advantages:

- It allows developers working on different machines to run Postgres consistently.

- It allows you to set up test data quickly when the container comes up so that unit tests can be run quickly against the latest schema changes.

Together these features mean that developers can run their tests against the same database stack that runs in production. (This is a topic that you may not think is very important if you haven't bumped into it, but it's near to the heart of everyone who has ever had to "fix" a bug where a unit test against an in-memory database behaved differently from a real production server).

This article will discuss some different ways you can approach working with Docker, Postgres, and Python.

- One approach is to run a Postgres server using Docker and connect to it from your client machine.

- Alternatively, you can run both Postgres and your client Python program in containers and network them with docker-compose.

- Finally, there's no reason you can't connect and develop locally while still iteratively building a client container as you go.

## Postgres Docker / Client on the Host

Let's
