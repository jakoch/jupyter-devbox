# SPDX-FileCopyrightText: 2021-2025 Jens A. Koch
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/jakoch/jupyter-devbox

# +-----------------------------+
# | BASE IMAGE             ~32MB|        See https://hub.docker.com/_/debian
# +-----------------------------+

# Platform/Architecture = linux/arm64v8 = linux/arm64/v8 = arm64 = aarch64

FROM arm64v8/debian:bookworm-slim

# +-----------------------------+
# | METADATA                    |
# +-----------------------------+

LABEL org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.vendor="Jens A. Koch" \
      org.opencontainers.image.authors="Jens A. Koch <jakoch@web.de>" \
      org.opencontainers.image.source="https://github.com/jakoch/jupyter-devbox"
# +-----------------------------+
# | ARGS                        |
# +-----------------------------+

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# +-----------------------------+
# | ENV                         |
# +-----------------------------+

ENV DEBIAN_FRONTEND=noninteractive \
    DEBCONF_NONINTERACTIVE_SEEN=true

# +-----------------------------+
# | SETUP PACKAGES              |
# +-----------------------------+

# avoid debconf delaying package configuration, since apt-utils is not installed
RUN apt-get update && \
    apt-get -y install --no-install-recommends apt-utils dialog sudo 2>&1

# Setup User and enable sudo
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME && \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME && \
    chmod 0440 /etc/sudoers.d/$USERNAME

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
        git zsh curl wget nano openssh-client ca-certificates tzdata locales \
        gcc g++ build-essential cmake ninja-build \
        zip unzip bzip2

# Set locale and timezone
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG=en_US.utf8 TZ=Etc/UTC

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > /tmp/rustup.sh \
  && sh /tmp/rustup.sh -y --default-toolchain stable
ENV HOME=/root
ENV PATH=$HOME/.cargo/bin:$PATH
#RUN rustup --version && cargo --version && rustc --version
#RUN rustup update

RUN apt-get -y install --no-install-recommends \
        libjpeg-dev libpng-dev libpq-dev \
        imagemagick gnuplot gnuplot-x11 libssl-dev libzmq3-dev graphviz \
        re2c libffi-dev libffi8 gfortran libxsimd-dev libhdf5-serial-dev \
        libxml2-dev libxslt-dev \
    # OPENCV
        libopencv-dev \
    # BLAS and LAPACK, OPENBLAS and BLIS
        libblas-dev liblapack-dev libopenblas-dev libblis-dev \
    # py3
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        python3-wheel \
        python3-setuptools

# Cleanup
RUN apt-get autoremove -fy && \
    apt-get clean && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/*

# Use a virtual environment for Python (to avoid PEP668 "externally managed environment" error).
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python Packages (base)
RUN pip config --user set global.disable-pip-version-check true && \
    pip config --user set global.progress_bar off && \
    pip config --user set global.no-cache-dir true && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade wheel && \
    pip install uv

# Install Python Packages using uv
RUN uv pip install \
    ipykernel docutils jupyter notebook jupyterhub \
    watermark pyyaml pylint h5py \
    tensorflow \
    matplotlib pillow seaborn plotly graphviz \
    keras \
    opencv-python-headless \
    imutils \
    numpy pandas pandas-datareader bottleneck \
    scipy scikit-learn \
    duckdb \
    sqlalchemy \
    pyautogui \
    requests_cache \
    yfinance alpha_vantage nasdaq-data-link finnhub-python financetoolkit financedatabase \
    statsmodels

# Install ipykernel
RUN /opt/venv/bin/python -m ipykernel install --user --name="jupyter_devbox" --display-name="jupyter_devbox_python3_venv"

# Re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog
