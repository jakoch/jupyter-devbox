# Changelog

All changes to the project will be documented in this file.

- The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
- The date format is YYYY-MM-DD.
- The upcoming release version is named `vNext` and links to the changes between latest version tag and git HEAD.

## [vNext] - unreleased

- just a placeholder

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

[vNext]: https://github.com/jakoch/jupyter-devbox/compare/v1.5.0...HEAD
[1.5.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.4.0...v1.5.0
[1.4.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jakoch/jupyter-devbox/releases/tag/v1.0.0
