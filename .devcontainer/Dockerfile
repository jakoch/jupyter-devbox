# +-----------------------------+
# | BASE IMAGE             ~27MB|        See https://hub.docker.com/_/debian
# +-----------------------------+

FROM debian:buster-slim

# +-----------------------------+
# | ARGS                        |
# +-----------------------------+

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# +-----------------------------+
# | ENV                         |
# +-----------------------------+

ENV DEBIAN_FRONTEND=noninteractive

# +-----------------------------+
# | PRE-REQUISITES/INIT PACKAGES |
# +-----------------------------+

# avoid debconf delaying package configuration, since apt-utils is not installed
RUN apt-get update && \
    apt-get -y install --no-install-recommends apt-utils dialog 2>&1

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        sudo git zsh curl wget \
        gcc g++ build-essential cmake build-essential \
        unzip libjpeg-dev libpng-dev libpq-dev \
        imagemagick gnuplot gnuplot-x11 libssl-dev libzmq3-dev graphviz \
        # py2
        python-dev python-pip \
        # py3
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        python3-wheel \
        python3-setuptools \
        python3-opencv \
        libopencv-dev

# Cleanup
RUN apt-get autoremove -y && \
    apt-get clean autoclean && \
    rm -rf /var/lib/apt/lists/*

# Install Python Packages
RUN pip3 install --upgrade pip && \
    pip3 install setuptools --upgrade && \
    pip3 install wheel && \
    pip3 install tensorflow && \
    pip3 install ipykernel docutils jupyter pyyaml pylint h5py && \
    pip3 install numpy pandas sklearn scipy && \
    pip3 install matplotlib seaborn pydotplus && \
    pip3 install keras --no-deps && \
    pip3 install opencv-python && \
    pip3 install imutils && \
    pip3 install sqlalchemy && \
    pip3 install pyautogui

# re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog
