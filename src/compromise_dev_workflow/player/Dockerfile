FROM ubuntu:latest

RUN apt-get update && apt-get install -y ssh
RUN useradd --create-home user

WORKDIR /home/user
USER user
COPY ./README.md .
