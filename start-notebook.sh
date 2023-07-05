#!/usr/bin/env bash

# copy jupyter notebook config to root user
cp -rf conf/.jupyter /root

# copy zsh config to root user
cp -rf .devcontainer/.zshrc /root

# adding "/root/.local/bin" for pylint (isort, epylint, pylint, etc.)
export PATH="/root/.local/bin:$PATH"

export DISPLAY=:0

jupyter kernelspec list

jupyter notebook "$@" &
