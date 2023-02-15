#!/usr/bin/env bash

# copy jupyter notebook config to root user
cp -rf conf/.jupyter /root

# adding "/root/.local/bin" for pylint (isort, epylint, pylint, etc.)
export PATH="/root/.local/bin:$PATH"

export DISPLAY=:0

jupyter notebook "$@" &