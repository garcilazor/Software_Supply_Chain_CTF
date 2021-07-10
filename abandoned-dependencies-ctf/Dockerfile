FROM ubuntu:latest

COPY . /app

WORKDIR /app

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install git -y \
    && apt-get install vim -y
RUN pip3 install getch
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./* /app/
