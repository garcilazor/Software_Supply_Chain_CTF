FROM gitea/gitea:1.14.5

ENV USER_UID=1000
ENV USER_GID=1000
ENV GITEA__datbase__DB_TYPE=mysql
ENV GITEA__database__HOST=db:3306
ENV GITEA__database__NAME=gitea
ENV GITEA__database__USER=gitea
ENV GITEA__database__PASSWD=gitea

COPY ./gitea/git /data/git
COPY ./gitea/gitea /data/gitea
COPY ./gitea/ssh /data/ssh

#set ports in docker compose

