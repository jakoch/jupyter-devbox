# Changelog

All changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
The project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- this is a placeholder

### Added

- added `.gitignore` and codeowners file
- added python packages:
  - watermark
  - plotly
  - graphviz
  - nasdaq-data-link
  - finnhub-python
  - finacetoolkit
  - finacnedatabase
- added vscode extension:
  - ms-python.black-formatter
- added/improved notebook examples:
  - added FRED/GDP visualization example to finance notebook
  - added statsmodels example
  - added check_devbox, which includes listing of installed packages

### Changed

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
- scan container image for vulnerabilites using trivy and upload sarif report
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

- The default remoteuser was changed from "root" to "vscode"

## [1.0.0] - 2023-02-14

### Added

- added "yfinance" python packages:
  - yfinance

### Changed

- updated to Debian 11 bullseye

### Removed

- dropped the deprecated Python 2

[unreleased]: https://github.com/jakoch/jupyter-devbox/compare/v1.3.0...HEAD
[1.3.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jakoch/jupyter-devbox/releases/tag/v1.0.0
