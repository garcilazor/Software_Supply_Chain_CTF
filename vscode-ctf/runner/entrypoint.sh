#!/bin/sh

Xvfb :99 -screen 0 640x480x8 -nolisten tcp &
export DISPLAY=":99"

# Code launches this stuff in a new process anyways
code repo --user-data-dir ~/

# open any python file to trigger pylint execution
code repo/*.py --user-data-dir ~/
sleep "$WAIT_TIME"
