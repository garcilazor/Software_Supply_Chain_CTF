#!/bin/sh

mkdir repo
mkdir data
Xvfb :99 -screen 0 640x480x8 -nolisten tcp &
export DISPLAY=":99"
bash -c "code repo --user-data-dir data" &
sleep "5"
