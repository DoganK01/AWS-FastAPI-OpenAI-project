# FastAPI OpenAPI Schema Generation & Validation

This project provides a set of tools for generating and validating OpenAPI schemas for a FastAPI-based application. It ensures that the OpenAPI schema remains up-to-date with your FastAPI application, and helps you detect differences between the existing schema and the newly generated schema.

## Features

### **Automatic OpenAPI Schema Generation**
   - This project allows you to automatically generate an OpenAPI schema from your FastAPI application.
   - The schema reflects all the routes, request parameters, responses, and other relevant API details.
   - The schema generation process is fully customizable, supporting title, version, description, tags, servers, and other OpenAPI features.
   - You can use the `generate` command to create and save the OpenAPI schema in a JSON format.

### **Schema Validation with Diffing**
   - This project provides a mechanism to compare an **existing** OpenAPI schema against a **newly generated** schema.
   - The `generate-and-diff` command generates the OpenAPI schema and checks for any differences compared to an existing schema on disk.
   - Differences are displayed in a user-friendly format, highlighting what has changed between the two schemas, such as:
     - Added or removed endpoints.
     - Modified request/response parameters.
     - Changes in descriptions, titles, or other metadata.
   - This is particularly useful for Continuous Integration (CI) pipelines to ensure that the API documentation is in sync with the code.

### **CLI-Based Interface for Flexibility**
   - The project comes with a simple yet powerful command-line interface (CLI) that allows for easy interaction with the script.
   - The CLI supports two main commands:
     - **`generate`**: Generates the OpenAPI schema and writes it to a specified file.
     - **`generate-and-diff`**: Generates the OpenAPI schema and compares it with an existing schema, optionally failing if there are differences.
   - The CLI uses the `argparse` library, which provides a clean and user-friendly experience for developers.

### **Easy Integration into CI/CD Pipelines**
   - The `generate-and-diff` command is perfect for CI/CD environments, where you can automatically verify that the OpenAPI schema in your repository is up-to-date.
   - If the generated schema differs from the existing one, the script will display a detailed diff and, optionally, cause the build to fail if discrepancies are found.
   - This ensures that API documentation is always aligned with the implementation, reducing the chances of outdated or incorrect API docs being deployed.

### **Detailed Diff Output**
   - The diffing feature is designed to show precise changes at every level of the OpenAPI schema.
   - It compares not only simple values but also nested structures such as:
     - **Dictionaries**: It shows the exact differences in nested properties.
     - **Lists**: It detects changes in list items, including added, removed, or modified entries.
   - Each detected difference is presented in a clear and structured format, indicating:
     - The path to the changed item in the schema.
     - The values before and after the change, displayed in JSON format for easy inspection.
   - The diffing system supports deep comparison, ensuring that even nested objects and lists are thoroughly checked.

### **Flexible Configuration and Settings**
   - The script uses the `Settings` class to configure application parameters. This enables the schema generation to adapt to different environments or configurations.
   - You can pass in various settings like the S3 bucket name (in the `Settings` class) for any specific configurations your FastAPI app might need.
   - The settings also support custom configuration of the FastAPI app, such as title, version, description, and others, which are directly reflected in the OpenAPI schema.

### **Output Customization**
   - The generated OpenAPI schema can be saved to a specified location, ensuring that you have control over where the schema file is stored.
   - The schema is saved in **formatted JSON**, making it easy to read and verify manually, if needed.
   - You can also specify the file path for the output using the `--output-spec` argument.

### **Comprehensive Diffing Between Schemas**
   - The `get_diff_between_openapi_schemas` function allows you to compare the newly generated OpenAPI schema with any existing schema stored in your repository.
   - The comparison identifies and lists all the differences between the two schemas, helping developers spot API changes before they cause issues.
   - The diffing works at a very granular level, detecting even small changes that could affect API consumers.

### **Error Handling and Exit Codes**
   - If differences are found between the existing and generated schemas, the script will print a detailed list of the differences.
   - If the `--fail-on-diff` option is specified, the script will exit with a non-zero status code (`sys.exit(1)`), indicating a failure in the CI pipeline.
   - This prevents inadvertent API schema changes from being merged without review, ensuring API contract consistency.

### **Documentation and Logging**
   - The project includes detailed docstrings and comments, making the code easy to understand and extend.
   - The diff output and error messages are clear and informative, providing developers with sufficient context to understand what changed and where.

### **Support for FastAPI Applications**
   - The script is tailored for FastAPI applications and integrates seamlessly with them.
   - It supports FastAPI features such as custom routes, description, versioning, metadata, and more, ensuring that the generated OpenAPI schema is accurate and complete.


---



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
