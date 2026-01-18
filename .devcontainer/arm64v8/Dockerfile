# SPDX-FileCopyrightText: 2021-2026 Jens A. Koch
# SPDX-License-Identifier: MIT
# This file is part of https://github.com/jakoch/jupyter-devbox

# +-----------------------------+
# | BASE IMAGE             ~32MB|        See https://hub.docker.com/_/debian
# +-----------------------------+

# Platform/Architecture = linux/arm64v8 = linux/arm64/v8 = arm64 = aarch64

FROM arm64v8/debian:trixie-slim

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
    zip unzip bzip2 \
    libjpeg-dev libpng-dev libpq-dev \
    imagemagick gnuplot gnuplot-x11 libssl-dev libzmq3-dev graphviz \
    pandoc libxml2-dev libxslt-dev \
    # opencv
    libopencv-dev \
    # py3
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    python3-wheel \
    python3-setuptools && \
    # Cleanup
    apt-get autoremove -fy && \
    apt-get clean && \
    apt-get autoclean -y && \
    rm -rf /var/lib/apt/lists/*

# Set locale and timezone
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG=en_US.utf8 TZ=Etc/UTC

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
    # Jupyter
    ipykernel jupyter notebook jupyterhub jupyter-book \
    # Jupyterlab Extensions
    jupyterlab-code-formatter \
    jupyterlab-lsp \
    jupyterlab-spellchecker \
    jupyterlab-execute-time \
    # Jupyter Tools
    nbconvert papermill[black] \
    # Python
    pyyaml pylint ruff black[jupyter] isort \
    python-lsp-server python-lsp-black python-lsp-ruff python-lsp-isort \
    docutils watermark bottleneck requests_cache \
    # Learning
    tensorflow keras \
    # Graphics and Visualization
    matplotlib seaborn plotly bokeh graphviz imutils \
    # CPU-only OpenCV
    opencv-python-headless \
    # Data Analysis
    numpy pandas pandas-datareader \
    # ML
    scipy scikit-learn topt statsmodels \
    # DB
    duckdb sqlalchemy \
    # Automation
    pyautogui \
    # Finance
    yfinance alpha_vantage nasdaq-data-link finnhub-python financetoolkit financedatabase \
    # Data
    h5py

# Install ipykernel
RUN /opt/venv/bin/python -m ipykernel install --user --name="jupyter_devbox" --display-name="jupyter_devbox_python3_venv"

# +----------------------------------------------------------------------+
# | Setup zsh, ohmyzsh, powerline fonts.                                 |
# | Setup zsh plugins: autosuggestions, autocompletions, history search. |
# +----------------------------------------------------------------------+

ENV TERM=xterm-256color \
    ZSH_THEME=agnoster

# Setup zsh for the root user
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN echo "ZSH" && \
    apt-get update && apt-get install --no-install-recommends --assume-yes \
    zsh fontconfig fonts-powerline && \
    # Install Oh My Zsh
    curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh | sh && \
    # Add Zsh plugins
    git clone --depth=1 --no-tags https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions && \
    git clone --depth=1 --no-tags https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/zsh-completions && \
    git clone --depth=1 --no-tags https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search && \
    # Update .zshrc
    sed -i \
      -e 's/^plugins=(git.*)/plugins=(git zsh-completions zsh-autosuggestions zsh-history-substring-search)/' \
      -e 's/^ZSH_THEME="[^"]*"/ZSH_THEME="robbyrussell"/' \
      -e 's/^# *DISABLE_UPDATE_PROMPT="true"/DISABLE_UPDATE_PROMPT="true"/' \
      -e 's/^# *DISABLE_AUTO_UPDATE="true"/DISABLE_AUTO_UPDATE="true"/' \
    /root/.zshrc && \
	# Cleanup
	apt-get autoremove -y && \
    apt-get clean autoclean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Set the default shell to zsh after it is installed
ENV SHELL=/bin/zsh

# Re-enable dialog mode for apt-get
ENV DEBIAN_FRONTEND=dialog
