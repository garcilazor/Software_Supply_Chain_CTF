FROM ubuntu:kinetic-20220830

COPY . /app

WORKDIR /app

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install git -y \
    && apt-get install vim -y
RUN pip3 install getch
RUN pip3 install --upgrade pip

COPY ./* /app/
