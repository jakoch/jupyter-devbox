#!/bin/bash

# copy jupyter notebook config to user home
cp -rf conf/.jupyter ~/

# adding "/root/.local/bin" for pylint (isort, epylint, pylint, etc.)
export PATH="/root/.local/bin:$PATH"

export DISPLAY=:0

#nohup bash -c 'jupyter notebook "$@" &'
jupyter notebook "$@" &
