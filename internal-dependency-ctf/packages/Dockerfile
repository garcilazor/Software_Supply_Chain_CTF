FROM ubuntu:latest

WORKDIR /app

COPY . /app

RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip\
    && apt-get install git -y\
    && apt-get install vim -y\
    && apt-get install patator -y \
    && apt-get install curl -y

RUN pip3 install --upgrade pip
RUN pip3 install twine
RUN pip3 install keyrings.alt

RUN chmod a+x /app/setup.sh

ENTRYPOINT ["/app/setup.sh"]