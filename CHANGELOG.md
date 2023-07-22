# Changelog

All changes to the project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
The project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

- this is a placeholder

### Added

- tba

### Changed

- tba

## [1.2.0] - 2023-07-22

### Added

- added the vscode.extension:
  - ms-toolsai.jupyter
  - ms-toolsai.jupyter-renderers
  - editorconfig.editorconfig
  - streetsidesoftware.code-spell-checker
- scan container image for vulnerabilites using trivy and upload sarif report
- user is now added to sudoers.d to allow package installation
- added statsmodels to python packages

### Changed

- updated Debian to v12 (bookworm)
- make use of virtual env for Python, because Debian 12 enforces pep668
- improved pip config (disabled progressbar, caching, pip-version-check)
- renamed `run-jupyter.sh` to `start-notebook.sh`

## [1.1.0] - 2023-02-15

### Added

- added Github Actions release workflow for publishing the container image to GHCR
- added some more python packages for finance, including:
  pandas-datareader, requests_cache, yfinance, alpha_vantage, quandl
- added the vscode.extension: yzhang.markdown-all-in-one
- added .editorconfig and dependabot.yml

### Changed

- The default remoteuser was changed from "root" to "vscode"

## [1.0.0] - 2023-02-14

### Added

- added "yfinance" python package

### Changed

- updated to Debian 11 bullseye

### Removed

- dropped the deprecated Python 2

[unreleased]: https://github.com/jakoch/jupyter-devbox/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jakoch/jupyter-devbox/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jakoch/jupyter-devbox/releases/tag/v1.0.0
