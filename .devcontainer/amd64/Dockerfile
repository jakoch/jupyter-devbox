# +-----------------------------+
# | BASE IMAGE             ~32MB|        See https://hub.docker.com/_/debian
# +-----------------------------+

# Platform/Architecture = linux/amd64

FROM debian:bookworm-slim

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
        git zsh curl wget nano openssh-client \
        gcc g++ build-essential cmake build-essential \
        unzip libjpeg-dev libpng-dev libpq-dev \
        imagemagick gnuplot gnuplot-x11 libssl-dev libzmq3-dev graphviz \
        # opencv
        libopencv-dev \
    # py3
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        python3-wheel \
        python3-setuptools
        #python3-opencv \ # 4.6.0

# Cleanup
RUN apt-get autoremove -fy && \
    apt-get clean && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/*

# Use a virtual environment for Python (to avoid PEP668 "externally managed environment" error).
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python Packages
RUN pip config --user set global.disable-pip-version-check true && \
    pip config --user set global.progress_bar off && \
    pip config --user set global.no-cache-dir true && \
    pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --upgrade wheel && \
    pip install ipykernel docutils jupyter notebook jupyterhub && \
    pip install watermark pyyaml pylint h5py && \
    pip install tensorflow && \
    pip install matplotlib seaborn plotly graphviz && \
    pip install numpy pandas pandas-datareader scipy scikit-learn && \
    pip install duckdb && \
    pip install keras --no-deps && \
    pip install opencv-python-headless && \
    pip install imutils && \
    pip install sqlalchemy && \
    pip install pyautogui && \
    pip install requests_cache && \
    pip install yfinance alpha_vantage nasdaq-data-link finnhub-python financetoolkit financedatabase && \
    pip install statsmodels

# Install ipykernel
RUN /opt/venv/bin/python -m ipykernel install --user --name="Python_3"

# Re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog
