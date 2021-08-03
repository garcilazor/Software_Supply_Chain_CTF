FROM ubuntu:latest


RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install vim -y \
    && apt-get install python3 -y \
    && apt-get install python3.8-venv -y

RUN pip3 install --upgrade pip
RUN pip3 install twine
RUN python3 -m pip config set global.index-url "http://pypi-server:8000/"
RUN python3 -m pip config set global.extra-index-url "http://internal-server:8080/"
RUN python3 -m pip config set global.trusted-host "internal-server pypi-server"
COPY ./.pypirc /root/


ENTRYPOINT /bin/bash

