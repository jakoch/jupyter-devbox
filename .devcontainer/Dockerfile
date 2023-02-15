# +-----------------------------+
# | BASE IMAGE             ~32MB|        See https://hub.docker.com/_/debian
# +-----------------------------+

FROM debian:bullseye-slim

# +-----------------------------+
# | METADATA                    |
# +-----------------------------+

LABEL org.opencontainers.image.vendor = "Jens A. Koch"
LABEL org.opencontainers.image.source = "https://github.com/jakoch/jupyter-devbox"

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

# Setup User
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    #
    # [Optional] Add Sudo support for this user.
    # Drop if you don't need to install software after connecting.
    apt-get update && \
    apt-get install -y sudo && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

# avoid debconf delaying package configuration, since apt-utils is not installed
RUN apt-get update && \
    apt-get -y install --no-install-recommends apt-utils dialog 2>&1

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        sudo git zsh curl wget \
        gcc g++ build-essential cmake build-essential \
        unzip libjpeg-dev libpng-dev libpq-dev \
        imagemagick gnuplot gnuplot-x11 libssl-dev libzmq3-dev graphviz \
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
RUN apt-get autoremove -fy && \
    apt-get clean && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/*

# Install Python Packages
RUN pip3 config --user set global.progress_bar off && \
    pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir --upgrade setuptools && \
    pip3 install --no-cache-dir --upgrade wheel && \
    pip3 install --no-cache-dir tensorflow && \
    pip3 install --no-cache-dir ipykernel docutils jupyter pyyaml pylint h5py && \
    pip3 install --no-cache-dir numpy pandas sklearn scipy && \
    pip3 install --no-cache-dir matplotlib seaborn pydotplus && \
    pip3 install --no-cache-dir keras --no-deps && \
    pip3 install --no-cache-dir opencv-python && \
    pip3 install --no-cache-dir imutils && \
    pip3 install --no-cache-dir sqlalchemy && \
    pip3 install --no-cache-dir pyautogui && \
    pip3 install --no-cache-dir pandas-datareader requests_cache && \
    pip3 install --no-cache-dir yfinance alpha_vantage quandl

# re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog
