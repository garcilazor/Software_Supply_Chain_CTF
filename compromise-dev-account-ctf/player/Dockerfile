FROM ubuntu:latest

WORKDIR /home/user

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip git vim build-essential 

RUN git clone https://github.com/vanhauser-thc/thc-hydra.git
RUN cd thc-hydra && ./configure && make && make install

COPY ./malicious_script.py /home/user/
COPY ./rockyou.txt /home/user/

RUN chmod a+x /home/user/malicious_script.py
