# jupyter-devbox [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/jakoch/jupyter-devbox/release.yml?branch=main&style=flat&logo=github&label=Image%20published%20on%20GHCR)](https://github.com/jakoch/jupyter-devbox) ![Latest Version](https://ghcr-badge.egpl.dev/jakoch/jupyter-devbox/latest_tag?trim=major&label=latest+version&ignore=sha*) ![Image Size](https://ghcr-badge.egpl.dev/jakoch/jupyter-devbox/size?color=%2344cc11&tag=latest&label=image+size&trim=)

A Docker development box for [Jupyter Notebooks][jupyter_website] with a focus on
Computer Vision, Machine Learning, Finance, Statistics and Visualization.

The following sections describe the container images, including their packages,
how to build or download them, and how to set them up.

#### What is this?

This is a Docker container supporting multiple architectures based on Debian Linux ([amd64][amd64_dockerfile] & [arm64][arm64_dockerfile]).

It sets up an Jupyter Notebook development environment for interactive Python programming for [Visual Studio Code][vscode_website].

It has preinstalled scientific computing packages (including OpenCV, Tensorflow, Keras, Numpy, Pandas, DuckDB,
Sklearn, Scipy, Matplotlib, Seaborn, Imutils, SqlAlchemy).

The images of this repository are available on Github Container Registry (GHCR).

#### What is pre-installed?

Base: Debian 12 - Bookworm

On top of the base image the following tools are installed:

- zsh, git, cmake, nano
- curl, wget
- imagemagick, gnuplot, graphviz

These programming languages are included:

- Python 3 (including  pip, setuptools, wheel, venv)
- C & C++ (g++)

The installed Python libraries are:

- jupyter ipykernel docutils pyyaml pylint
- h5py
- tensorflow keras
- pandas pandas-datareader
- duckdb
- numpy scipy sklearn
- matplotlib seaborn plotly graphviz
- opencv-python-headless
- imutils
- sqlalchemy
- pyautogui
- yfinance alpha_vantage nasdaq-data-link
- financetoolkit financedatabase
- statsmodels
- requests_cache

You can find a list of all installed packages in the [notebooks/check_devbox.ipynb][check_devbox_ipynb_main] Notebook.

#### Prerequisites

You need the following things to run this:

- Docker
- Visual Studio Code

#### How to run this?

There are two ways of setting the container up.

Either by building the container image locally or by fetching the prebuilt container image from the Github container registry.

##### Building the Container Image locally using VSCode

- **Step 1.** Get the source: clone this repository using git or download the zip

- **Step 2. (optional)** The repository contains multiple images.

  You select an image by modifying the `dockerFile` to use in `./devcontainer/devcontainer.json`:

  By default `"dockerFile": "amd64/Dockerfile"` is set.

  For an image with architecture:
  - amd64 set `amd64/Dockerfile`
  - arm64, aarch64, arm64v8 set `arm64v8/Dockerfile`

- **Step 3.** In VSCode open the folder in a container (`Remote Containers: Open Folder in Container`):

  This will build the container image (`Starting Dev Container (show log): Building image..`)

  Which takes a while...

  Then, finally...

- **Step 4.** Open the file `notebooks\test.ipynb`

- **Step 5.** You might get a warning message for "untrusted" Notebook content.

  Click `Trust` to allow running the content of the Notebook.

- **Step 6.** You are now able to edit cells and run their content interactively in VSCode.

  You might also run your scripts inside your browser at http://localhost:8888/

- Enjoy! :sunglasses:

##### Fetching the prebuilt container image

This container image is published to the Github Container Registry (GHCR).

You may find the package here: [https://github.com/jakoch/jupyter-devbox/pkgs/container/jupyter-devbox][github_packages].

You can install the container image from the command line:

```bash
docker pull ghcr.io/jakoch/jupyter-devbox:latest
```

You might also use this container image as a base image in your own Dockerfile:

```bash
FROM ghcr.io/jakoch/jupyter-devbox:latest
```

## Supported CPU Architectures

- x86_64 - linux/amd64
  - [./devcontainer/amd64/Dockerfile][amd64_dockerfile]
- aarch64 - linux/aarch64, linux/arm64/v8, linux/arm64v8
  - [./devcontainer/arm64v8/Dockerfile][arm64_dockerfile]
- not supported:
  - armel
  - armhf, linux/arm64/v7, linux/arm64v7

- You can check your platform and available features with
  - `dpkg --print-architecture`
  - `cat /proc/cpuinfo`

<!-- Section for Reference Links -->

[jupyter_website]:https://jupyter.org/
[vscode_website]:https://code.visualstudio.com/
[check_devbox_ipynb_main]:https://github.com/jakoch/jupyter-devbox/blob/main/notebooks/check_devbox.ipynb
[amd64_dockerfile]:https://github.com/jakoch/jupyter-devbox/blob/main/.devcontainer/amd64/Dockerfile
[arm64_dockerfile]:https://github.com/jakoch/jupyter-devbox/blob/main/.devcontainer/arm64/Dockerfile
[github_packages]: https://github.com/jakoch/jupyter-devbox/pkgs/container/jupyter-devbox
