FROM ubuntu:20.04

RUN apt-get update && apt-get upgrade -y && \
    echo "debconf debconf/frontend select noninteractive" | debconf-set-selections && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y xvfb wget sudo curl 
    #libnotify4 libnss3 gnupg libsecret-1-0 libgtk-3-0 libxss1

RUN wget -O code.deb https://update.code.visualstudio.com/1.37.1/linux-deb-x64/stable && \
    apt-get install -y ./code.deb && rm code.deb
RUN wget -O ext.vsix https://github.com/microsoft/vscode-python/releases/download/2019.9.34911/ms-python-release.vsix && \
    useradd -u 1001 user -M -d /home && chown -R user:user /home && sudo --user='#1001' bash -c "code --install-extension ./ext.vsix" && rm ext.vsix

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]