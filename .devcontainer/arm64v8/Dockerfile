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

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN=true

# +-----------------------------+
# | PRE-REQUISITES/INIT PACKAGES |
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
        gcc g++ build-essential cmake ninja-build

# Install Rust
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > /tmp/rustup.sh \
  && sh /tmp/rustup.sh -y --default-toolchain stable
ENV HOME /root
ENV PATH $HOME/.cargo/bin:$PATH
#RUN rustup --version && cargo --version && rustc --version
#RUN rustup update

RUN apt-get -y install --no-install-recommends \
        unzip libjpeg-dev libpng-dev libpq-dev \
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
# Let pip fetch prebuild wheels from piwheels.org
#RUN echo "[global]\nextra-index-url=https://www.piwheels.org/simple" > /etc/pip.conf
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python Packages
RUN pip3 config --user set global.disable-pip-version-check true && \
    pip3 config --user set global.progress_bar off && \
    pip3 config --user set global.no-cache-dir true && \
    pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools && \
    pip3 install --upgrade wheel

# prefer-binary = prefer to download the precompiled wheel, even if source is newer
RUN pip3 install --prefer-binary --no-cache-dir \
    ipykernel docutils jupyter notebook jupyterhub

RUN pip3 install --prefer-binary --no-cache-dir \
    watermark \
    pyyaml \
    pylint \
    h5py

RUN pip3 install --prefer-binary --no-cache-dir \
    tensorflow \
    matplotlib seaborn plotly graphviz

RUN pip3 install --prefer-binary --no-cache-dir \
    keras --no-deps \
    opencv-python-headless \
    imutils

RUN pip3 install --prefer-binary --no-cache-dir \
    numpy pandas pandas-datareader bottleneck \
    scipy scikit-learn \
    duckdb

RUN pip3 install --prefer-binary --no-cache-dir \
    sqlalchemy \
    pyautogui \
    requests_cache \
    yfinance alpha_vantage nasdaq-data-link finnhub-python financetoolkit financedatabase \
    statsmodels

# Install ipykernel
RUN /opt/venv/bin/python -m ipykernel install --user --name="Python_3"

# Re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog
