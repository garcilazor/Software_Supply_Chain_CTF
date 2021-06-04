#!/bin/sh

git clone "$GIT_URL" repo
sudo --user=user code repo &
pid="$!"
sleep "$EXECUTION_MAX_SECONDS"
kill $!
