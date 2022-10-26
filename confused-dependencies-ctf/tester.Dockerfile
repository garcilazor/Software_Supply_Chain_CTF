FROM ubuntu:22.04

RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip \
    && apt-get install vim -y \
    && apt-get install python3 -y \
    && apt-get install python3.8-venv -y

RUN pip3 install --upgrade pip
RUN pip3 install twine
RUN pip install --user --upgrade pip
RUN pip install keyrings.alt
RUN python3 -m pip config set global.index-url "http://user:malicious@pypi-server:8080/simple/"
RUN python3 -m pip config set global.extra-index-url "http://employee:qwer1234@internal-server:8080/simple/"
RUN python3 -m pip config set global.trusted-host "internal-server pypi-server"
COPY ./tester.pypirc /root/.pypirc

# Create flag
RUN mkdir /root/.ssh
COPY ./flag /root/.ssh/id_rsa
COPY ./run_test.sh /run_test.sh
COPY ./test-app/userwidgetserv /root/userwidgetserv

WORKDIR /root

ENTRYPOINT "/run_test.sh"

