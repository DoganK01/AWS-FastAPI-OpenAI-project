# FastAPI OpenAPI Schema Generation & Validation

This project provides a set of tools for generating and validating OpenAPI schemas for a FastAPI-based application. It ensures that the OpenAPI schema remains up-to-date with your FastAPI application, and helps you detect differences between the existing schema and the newly generated schema.

## Features

- **Generate OpenAPI Schema**: Automatically generates an OpenAPI schema from the FastAPI application.
- **Validate Schema Changes**: Compares an existing OpenAPI schema with the newly generated one to detect any changes.
- **Command-Line Interface (CLI)**: A simple CLI tool to generate and validate OpenAPI schemas.
- **Integration with CI/CD**: Ensures that the OpenAPI schema in your repository is always up-to-date with the FastAPI application, preventing mismatches between your code and API documentation.


## Quick start

```bash
pip install AWS-FastAPI-OpenAI-project
```

```python
from files_api import ...
```

## Developing/Contributing

### System requirements

You will need the following installed on your machine to develop on this codebase

- `make` AKA `cmake`, e.g. `sudo apt-get update -y; sudo apt-get install cmake -y`
- Python 3.7+, ideally using `pyenv` to easily change between Python versions
- `git`

###

```bash
# clone the repo
git clone https://github.com/DoganK01/AWS-FastAPI-OpenAI-project.git

# install the dev dependencies
make install

# run the tests
make test
```

## Contribution Guidelines
We welcome contributions to this project! Please follow these steps:

1. Fork the repository and create your branch.
2. Install dependencies and run tests.
3. Make your changes, ensuring the code is well-documented.
4. Commit your changes and create a pull request.
