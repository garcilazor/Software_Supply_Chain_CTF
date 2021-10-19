FROM ubuntu:21.10

# Install dependencies (DEBIAN_FRONTEND=noninteractive required to avoid timezone prompt)
RUN apt-get update && apt-get upgrade -y && \
    echo "debconf debconf/frontend select noninteractive" | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y xvfb wget curl
RUN wget -O code.deb https://update.code.visualstudio.com/1.37.1/linux-deb-x64/stable && \
    apt-get install -y ./code.deb && rm code.deb

ENV DATA_DIR=/root/.vscode

RUN mkdir $DATA_DIR && mkdir $DATA_DIR/User

# Setup VSCode config directory
COPY settings.json $DATA_DIR/User

# Install Python Extension
RUN wget -O ext.vsix https://github.com/microsoft/vscode-python/releases/download/2019.10.41019/ms-python-release.vsix && \
    bash -c "code --user-data-dir $DATA_DIR --install-extension ./ext.vsix" && rm ext.vsix

# Setup flag
RUN mkdir /root/.ssh
COPY flag /root/.ssh/id_rsa

# in seconds
ENV WAIT_TIME=20

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
