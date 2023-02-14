# jupyter-devbox

A Docker development box for Jupyter Notebook's with a focus on Computer Vision, Machine Learning, Statistics and Visualization.

#### What is this?

This is a Docker container based on Debian Linux (see [Dockerfile](https://github.com/jakoch/jupyter-devbox/blob/main/.devcontainer/Dockerfile)).
It sets up a Python/Jupyter Notebook development environment for Visual Studio Code.
The pre-installed libraries include OpenCV, Tensorflow, Keras, Numpy, Pandas, Sklearn, Scipy, Matplotlib, Seaborn, Imutils, SqlAlchemy.

#### What is pre-installed?

Base: Debian 11 - Bullseye

On top of the base image the following tools are installed:
- zsh, git, cmake
- curl, wget
- imagemagick, gnuplot, graphviz

These programming languages are included:
 - Python 3 (including wheel, setuptools, pip)
 - C & C++ (g++)

The installed Python libraries are:
 - jupyter ipykernel docutils pyyaml pylint h5py
 - tensorflow keras
 - numpy pandas sklearn scipy
 - matplotlib seaborn
 - opencv-python
 - imutils
 - sqlalchemy
 - pyautogui
 - yfinance

#### Prerequisites

You need the following things to run this:

- Docker
- Visual Studio Code

#### How to run this?

1. Get the source: clone this repository using git or download the zip
2. In VSCode open the folder in a container (`Remote Containers: Open Folder in Container`):

   This will build the container image (`Starting Dev Container (show log): Building image..`)

   Which takes a while...

   Then, finally...

4. Open the file `notebooks\test.ipynb`
5. You might get a warning message for "untrusted" Notebook content.

   Click `Trust` to allow executing the content of the Notebook.

6. You are now able to edit cells and run their content interactively.

   You might also run your scripts inside your browser at http://localhost:8888/

   And you can also read and run your scripts via the Github website: [notebooks/test.ipynb](https://github.com/jakoch/jupyter-devbox/blob/main/notebooks/test.ipynb).

7. Enjoy! :sunglasses:
