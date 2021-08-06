# TODO: Is there a way to share a common builder with the private repo?
FROM pypiserver/pypiserver:v1.4.2 AS builder
RUN apk add gcc musl-dev openssl-dev libffi-dev
RUN python3 -m pip install build
WORKDIR /root/
RUN mkdir ./packages

COPY ./test-app/mysoftlog ./mysoftlog
RUN python3 -m pip download ./mysoftlog -d ./packages

COPY ./test-app/public_requirements.txt public_requirements.txt
RUN python3 -m pip download -r ./public_requirements.txt -d ./packages
RUN ls ./packages

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

