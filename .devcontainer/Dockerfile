# FROM python:3.11-bullseye
FROM mcr.microsoft.com/devcontainers/python:0-3.11-bullseye 

COPY packages.txt /tmp/
COPY requirements.txt /tmp

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install $(cat /tmp/packages.txt)

RUN pip3 install -r /tmp/requirements.txt

# Make scripts avaialble
RUN echo export PATH="/workspaces/cpp-book/scripts:$PATH" >> ~/.bashrc

# [Optional] Uncomment this section to install additional vcpkg ports.
# RUN su vscode -c "${VCPKG_ROOT}/vcpkg install <your-port-name-here>"

