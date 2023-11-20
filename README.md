# Moderne Client

[![CI](https://github.com/JLLeitschuh/moderne-client/actions/workflows/ci.yml/badge.svg)](https://github.com/JLLeitschuh/moderne-client/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/JLLeitschuh/moderne-client/branch/main/graph/badge.svg?token=C05nBupDo7)](https://codecov.io/gh/JLLeitschuh/moderne-client)

This is a client for the [Moderne](https://moderne.io) API.
It is how Jonathan Leitschuh generates automated pull requests to fix vulnerabilities, at-scale, across the entire open source ecosystem.

## Why?

Running a Moderne recipe once via their UI is easy, but what if you want to run a recipe on a scheduled basis across
all of your repositories? Moderne doesn't, currently, support campaigns. This fills that gap.

## Usage

This client can either be used as a standalone script, or as a library.

### Secrets

All environment variables are either read directly from the environment or a `.env` file in the execution directory.

The client requires a few secrets to be set in the environment:

#### Moderne API Token
Can either be read from:
 - `~/.moderne/token.txt` file
 - `MODERNE_API_TOKEN` environment variable

This is required for all moderne API calls.

#### GitHub API Token
Can either be read from:
 - `~/.config/hub` file
 - `GITHUB_TOKEN_FOR_MODERNE` environment variable

This is required only when attempting to create pull requests.

#### GPG Key
In order to support GPG signing commits, there are two options:

1. Set the following environment variables:
   - `GPG_KEY_PUBLIC_KEY`
   - `GPG_KEY_PRIVATE_KEY`
   - `GPG_KEY_PASSPHRASE`

2. Set the following environment variables and the rest of the data will be loaded from your local gpg install:
 - `GPG_KEY_ID`
 - `GPG_KEY_PASSPHRASE`

This is required only when attempting to create pull requests.

### CLI Usage

To install the CLI dependencies use the following command:

```bash
pip install .[cli]
```

For live development, you can use the following command to install the CLI in editable mode:
```bash
pip install -e .[cli]
```
To see more information about developing the CLI, see the [CONTRIBUTING](CONTRIBUTING.md) guide.

To use it as a script, you can run it like this:

```bash
moderne-client --help
```

### Library Usage
TODO
