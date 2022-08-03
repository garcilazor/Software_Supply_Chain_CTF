FROM ubuntu:22.04

WORKDIR /home/app

COPY ./main.py /home/app
COPY ./start.sh /home/app
COPY /sshkey /root

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y\
    && apt-get install vim -y

RUN pip3 install --upgrade pip

RUN pip3 install getch

RUN chmod a+x /home/app/start.sh


ENTRYPOINT ["/home/app/start.sh"]
