# csp matrix adapter

A [csp](https://github.com/point72/csp) adapter for [Matrix](https://matrix.org)

[![Build Status](https://github.com/csp-community/csp-adapter-matrix/actions/workflows/build.yaml/badge.svg?branch=main&event=push)](https://github.com/csp-community/csp-adapter-matrix/actions/workflows/build.yaml)
[![codecov](https://codecov.io/gh/csp-community/csp-adapter-matrix/branch/main/graph/badge.svg)](https://codecov.io/gh/csp-community/csp-adapter-matrix)
[![License](https://img.shields.io/github/license/csp-community/csp-adapter-matrix)](https://github.com/csp-community/csp-adapter-matrix)
[![PyPI](https://img.shields.io/pypi/v/csp-adapter-matrix.svg)](https://pypi.python.org/pypi/csp-adapter-matrix)

## Overview

The Matrix adapter reads and writes Matrix messages in [csp](https://github.com/point72/csp) graphs. It wraps the Matrix backend from [chatom](https://github.com/1kbgz/chatom), which uses [`matrix-nio`](https://pypi.org/project/matrix-nio/), or [`matrix-sdk-python`](https://pypi.org/project/matrix-sdk-python/) for end-to-end encrypted rooms.

## Chat Framework

[`csp-bot`](https://github.com/Point72/csp-bot) is a framework for writing cross-platform, command oriented chat bots.

## Installation

Install with `pip`:

```bash
pip install csp csp-adapter-matrix
```

For end-to-end encrypted rooms, install the `e2ee` extra and create the adapter with `encrypted=True`:

```bash
pip install 'csp-adapter-matrix[e2ee]'
```

## License

This software is licensed under the Apache 2.0 license. See the [LICENSE](https://github.com/csp-community/csp-adapter-matrix/blob/main/LICENSE) file for details.

> [!NOTE]
> This library was generated using [copier](https://copier.readthedocs.io/en/stable/) from the [Base Python Project Template repository](https://github.com/python-project-templates/base).
