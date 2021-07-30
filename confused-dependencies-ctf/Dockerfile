FROM ubuntu:latest


RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install vim -y \
    && apt-get install python3 -y \
    && apt-get install python3.8-venv -y

RUN pip3 install --upgrade pip
RUN pip3 install twine
RUN pip3 install keyrings.alt
RUN python3 -m pip config set global.extra-index-url "http://0.0.0.0:8080/ http://0.0.0.0:8000/"
COPY ./.pypirc /root/
COPY ./packages/* /root/packages

ENTRYPOINT /bin/bash

