---
title: "Python and AWS:  Getting Started with the Cloud Development Kit (CDK)"
date: "2022-11-14"
categories: 
  - "miscellaneous"
---
# Python and AWS:  Getting Started with the Cloud Development Kit (CDK)
Several infrastructure-as-code tools can help us deploy our code to Amazon's cloud offering (Amazon Web Services or AWS). All such tools are essentially client applications of one sort or another, which deploy cloud infrastructure by calling into AWS's Rest APIs.

AWS's CLI (Command Line Interface tool), for example, allows you to interact with AWS via the command line, in much the same way that you can interact with Python by running Python or IPython interactively. Interestingly, under the covers, the AWS command line tool is built on Python's boto3 client library, which we introduced and discussed in [Python for AWS Lambda Functions: A Beginner’s Guide](https://codesolid.com/python-and-aws-lambda-functions/).

Boto3 is an awesome library, but it cannot manage complex infrastructure deployments easily by itself. Often, what individuals and DevOps teams want are tools that will help them manage their costs by allowing them to create and tear down reproducible sets of components.

The two major tools that fill that gap are CloudFormation, which is Amazon's proprietary solution, and Terraform, a third-party tool that supports multiple cloud vendors with pluggable "providers" (including one for AWS, of course).

As popular as these tools are, neither of them is written in a "real" programming language. Terraform files are written in HCL (Hashicorp Markup Language), a proprietary markup language. CloudFormation can be written either in JSON or YAML. These tools generally express simple relationships between infrastructure components well but lack the expressive power of languages like Python.

To restore such expressive power to infrastructure deployment and to allow developers to use tools they already know, AWS created the Cloud Development Kit (or CDK). The CDK provides a layer of abstraction on top of CloudFormation and allows it to be used from TypeScript, Python, and other languages.

## Getting Started: Basic Setup for the CDK for Python

This article assumes that you have an AWS account and that you have the AWS CLI [installed and configured](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

In addition to the AWS CLI, the CDK also depends on Node for the CDK command line tool.

The fact that you can easily install such extra tools into an environment is [one of many reasons](https://codesolid.com/conda-vs-pip/ "one of many reasons") I like to use conda, so if you have Anaconda or mini-conda installed, please use the next section. If you don't, we'll also walk you through the basics in the section "Using the CDK in a Python Virtual Environment", but you'll need to install [Node.js](https://nodejs.org/en/) separately in that case if you don't already have it. (If you're not sure, try typing "`node --version`" to see if it's available).

### Using the Python CDK With Conda

Conda makes it easy to set up an environment with Python and Node and to activate a separate environment. Note however that we still need to install the CDK library using pip.

To get started, use the following terminal commands:

```bash
# Create and activate the environment:
conda create -n aws-cdk python=3.11 nodejs --yes
conda activate aws-cdk

# Install the CDK (Command line tool)
npm install -g aws-cdk

# Install the CDK (library)
pip install aws-cdk-lib
```

### Using the CDK in a Python Virtual Environment

To create a virtual environment and install the Python Cloud Development Kit, use the following commands:

```
# Create and activate the environment:

python -m venv venv
source venv/bin/activate   # Linux or Mac
venv\scripts\activate.bat  # Windows

# Install the CDK
pip install aws-cdk-lib
```
