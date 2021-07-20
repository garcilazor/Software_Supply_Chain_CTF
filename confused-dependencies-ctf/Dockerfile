FROM ubuntu:latest


RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install vim -y \
    && apt-get install python3 -y \
    && apt-get install python3.8-venv -y

RUN pip3 install --upgrade pip
RUN pip install devpi
RUN pip install supervisor
RUN devpi-init
RUN devpi-gen-config
RUN supervisord -c gen-config/supervisord.conf

ENTRYPOINT /bin/bash

