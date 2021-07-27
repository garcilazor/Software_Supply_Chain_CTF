FROM ubuntu:latest


RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install vim -y \
    && apt-get install python3 -y \
    && apt-get install python3.8-venv -y

RUN pip3 install --upgrade pip
RUN python3 -m pip config set global.extra-index-url "http://localhost:8080/simple/ http://localhost:8000/simple/"
COPY ./.pypirc /root/
COPY ./packages/* /root/packages

ENTRYPOINT /bin/bash

