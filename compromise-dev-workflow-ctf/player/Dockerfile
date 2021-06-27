FROM ubuntu:latest

RUN apt-get update && apt-get install -y ssh curl vim nano

RUN useradd --create-home user

WORKDIR /home/user
USER user
COPY ./README.md .
COPY ./note_from_disgruntled_employee .
