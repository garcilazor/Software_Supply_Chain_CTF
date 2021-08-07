FROM ubuntu:latest

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install vim -y \
    && apt-get install python3 -y \
    && apt-get install python3.8-venv -y

RUN pip3 install --upgrade pip
RUN pip3 install twine
RUN pip install --user --upgrade pip
RUN pip install keyrings.alt
RUN python3 -m pip config set global.index-url "http://pypi-server:8000/simple/"
RUN python3 -m pip config set global.extra-index-url "http://internal-server:8080/simple/"
RUN python3 -m pip config set global.trusted-host "internal-server pypi-server"
COPY ./.pypirc /root/

# Copy current source code in (can say that the player somehow acquired it)
RUN mkdir /root/src
COPY ./test-app/userwidgetserv /root/src/
COPY ./test-app/mysoftlog /root/src/
COPY ./test-app/player-README.md /root/src/README.md


ENTRYPOINT /bin/bash

