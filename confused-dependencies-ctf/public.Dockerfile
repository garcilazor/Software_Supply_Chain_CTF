FROM pypiserver/pypiserver:v1.4.2 AS builder
RUN apk add gcc musl-dev openssl-dev libffi-dev
RUN python3 -m pip install build
WORKDIR /root/
RUN mkdir ./packages ./tmp-packages

COPY ./test-app/mysoftlog ./mysoftlog
RUN python3 -m pip wheel -w tmp-packages ./mysoftlog

COPY ./test-app/userwidgetserv ./userwidgetserv
RUN python3 -m pip wheel --find-links ./tmp-packages -w packages ./userwidgetserv
RUN python3 -m pip wheel -w packages wheel setuptools

# mysoftlog should only be in the private server
RUN rm ./packages/mysoftlog-1.7.3-py3-none-any.whl

################################

FROM pypiserver/pypiserver:v1.4.2

COPY --from=builder /root/packages /data/packages

# Copy auth information into container
COPY ./auth /data/auth

# TODO: Don't put both credential files into both containers
CMD [ \
    "-P", "/data/auth/local/.htpasswd", \
    "-a", "update,download,list", \
    "/data/packages"]

