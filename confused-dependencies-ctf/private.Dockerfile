# TODO: Is there a way to share a common builder with the private repo?
FROM pypiserver/pypiserver:v1.4.2 AS builder
RUN apk add gcc musl-dev openssl-dev libffi-dev
RUN python3 -m pip install build
WORKDIR /root/
RUN mkdir ./packages

COPY ./test-app/mysoftlog ./mysoftlog
RUN python3 -m pip download ./mysoftlog -d ./packages

###############################

FROM pypiserver/pypiserver:v1.4.2

# Copy packages into container
COPY --from=builder /root/packages /data/packages

# Copy auth information into container
COPY ./auth /data/auth

CMD [ \
    "-P", "/data/auth/internal/.htpasswd", \
    "-a", "update,download,list", \
    "/data/packages"]

