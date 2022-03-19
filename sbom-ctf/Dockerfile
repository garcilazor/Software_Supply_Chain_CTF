FROM ubuntu:20.04

WORKDIR /projects/

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y\
    && apt-get install -y python3.8-venv\
    && apt-get install -y vim\
    && DEBIAN_FRONTEND='noninteractive' apt-get install -y npm

RUN pip3 install --upgrade pip

COPY ./projects /projects/
