# Changelog

All changes to the project will be documented in this file.

- The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
- The date format is YYYY-MM-DD.
- The upcoming release version is named `vNext` and links to the changes between latest version tag and git HEAD.

## [vNext] - unreleased

"It was a bright day in April, and the clocks were striking thirteen." - 1984

## [2.0.1] - 2026-01-16

This release focuses on two main areas:

1. Integration of language server support for standalone Python and JupyterLab.
2. Improvement of code formatting using the Black formatter.

### Added

- added python packages:
  - black isort
  - jupyterlab-lsp
  - python-lsp-server, python-lsp-black, python-lsp-ruff, python-lsp-isort
  - jupyterlab-spellchecker
  - jupyterlab-execute-time
- added automatic formatting of Python code cells using Black
  - to Jupyter using `c.JupyterLabCodeFormatter` in `jupyter_notebook_config.py`
  - to VSCode using `customizations.vscode.settings` in `devcontainer.json`
- added `.virtual_documents` to `.gitignore`
  (The folder stores temporary copies of unsaved documents for LSP access.)
- added "dot-files" to `.dockerignore`, updated `.editorconfig`

## [2.0.0] - 2026-01-13

### Added

- added python packages:
  - python-lsp-server (which provides Python Language Server support)

### Changed

- reduced number of layers by combining/concatenating some ENV and RUN commands
- synced python packages between images:
  - added ruff and jupyterlab-code-formatter to arm64v8 image
  - removed Pillow from the direct requirements of arm64v8;
    it is already fetched as a transitive dependency of another package.

### Removed

- removed the installation of Rust from the arm64v8 image

## [1.9.0] - 2025-11-29

- updated Debian to v13 (trixie)
- fixed some minor issues on finance.ipynb, due to changed APIs
- added an rule-of-72.ipynb, a finance notebook demonstrating how to use Markdown
  and LaTeX to render mathematical formulas.

## [1.8.0] - 2025-07-30

- added python package manager uv and adjusted the python installation step accordingly

## [1.7.0] - 2025-06-12

- Updated an action in GHA release workflow.

## [1.6.0] - 2025-01-26

### Changes

- bumped copyright year to 2025

## [1.5.0] - 2024-06-25

- added Github Community Standard documents
- enabled scheduled releases (weekly)
- added ./docs/faq.md

## [1.4.0] - 2024-02-16

### Added

- added Dockerfile for arm64v8 architecture into folder ".devcontainer/arm64v8"
- added `.gitignore` and codeowners file
- added python packages:
  - watermark
  - plotly
  - graphviz
  - nasdaq-data-link
  - finnhub-python
  - finacetoolkit
  - financedatabase
  - duckdb
- added vscode extension:
  - ms-python.black-formatter
- added/improved notebook examples:
  - added FRED/GDP visualization example to finance notebook
  - added statsmodels example
  - added check_devbox, which includes listing of installed packages
- added debian packages:
  - ca-certificates
  - tzdata
  - locales
- devcontainer.json:
  - added python.terminal.activateEnvironment
  - added python.defaultInterpreterPath ([#6](https://github.com/jakoch/jupyter-devbox/issues/6))

### Changed

- Dockerfile:
  - use multiple pip install runs, else the dependencies do not resolve correctly
  - reduced number of run sections
  - added locale setup
  - changed ipykernel name ("jupyter_debvox") and display_name
- jupyter_notebook_config.py:
  - used the ipykernel name as c.MultiKernelManager.default_kernel_name
  - renamed deprecated c.ServerApp.token to c.IdentityProvider.token
- moved Dockerfile for amd64 into folder ".devcontainer/amd64"
- changed github workflow to build a multi-arch container for amd64 and arm64
  - firstly, build each container image and a digest/manifest,
  - secondly, upload the merged digests as one manifest file
- changed python packages:
  - opencv-python to opencv-python-headless

### Removed

- removed python packages:
  - pydotplus
  - quandl (deprecated, replaced by nasdaq-data-link)

## [1.3.0] - 2024-02-05

### Added

- run installation of ipykernel
- added jupyterhub to python packages

### Changed

- updated notebook config, replaced `c.NotebookApp` with `c.ServerApp`

### Removed

- removed the tensorboard port from "appPort" in devcontainer.json
- removed apt package python3-opencv, because version too old (4.6.0)

## [1.2.0] - 2023-07-22

### Added

- added vscode.extensions:
  - ms-toolsai.jupyter
  - ms-toolsai.jupyter-renderers
  - editorconfig.editorconfig
  - streetsidesoftware.code-spell-checker
- scan container image for vulnerabilities using trivy and upload sarif report
- user is now added to sudoers.d to allow package installation
- added python packages:
  - statsmodels

### Changed

- updated Debian to v12 (bookworm)
- make use of virtual env for Python, because Debian 12 enforces pep668
- improved pip config (disabled progressbar, caching, pip-version-check)
- renamed `run-jupyter.sh` to `start-notebook.sh`

## [1.1.0] - 2023-02-15

### Added

- added Github Actions release workflow for publishing the container image to GHCR
- added python packages:
  - pandas-datareader
  - requests_cache
  - alpha_vantage
  - quandl
- added vscode.extensions:
  - yzhang.markdown-all-in-one
- added .editorconfig and dependabot.yml

### Changed

- The default remote user was changed from "root" to "vscode"

## [1.0.0] - 2023-02-14

### Added

- added python packages:
  - yfinance

### Changed

- updated to Debian 11 bullseye

### Removed

- dropped the deprecated Python 2

<!-- Section for Reference Links -->

[vNext]: https://github.com/jakoch/jupyter-devbox/compare/v2.0.1...HEAD
[2.0.1]: https://github.com/jakoch/jupyter-devbox/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.9.0...v2.0.0
[1.9.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.8.0...v1.9.0
[1.8.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.7.0...v1.8.0
[1.7.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.6.0...v1.7.0
[1.6.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jakoch/jupyter-devbox/releases/tag/v1.0.0
