# FastAPI OpenAPI Schema Generation & Validation

This project provides a set of tools for generating and validating OpenAPI schemas for a FastAPI-based application. It ensures that the OpenAPI schema remains up-to-date with your FastAPI application, and helps you detect differences between the existing schema and the newly generated schema.

## Features

### **File Upload and Retrieval**

The core functionality of the **Files API** revolves around file management. The API supports:

- **File Upload**: Uploading files to the server is straightforward and simple. The files can be uploaded using the `/files/upload` endpoint. This allows users to send a file as part of their HTTP request and store it in the server (or cloud storage like AWS S3).

- **File Retrieval**: The `/files/{file_id}` endpoint allows users to retrieve previously uploaded files by their unique identifier (`file_id`). This allows for quick access to files using a RESTful approach.

  **How It Works:**
  - **Upload**: When a file is uploaded, the system generates a unique identifier for the file (e.g., a UUID) which is used for future retrievals.
  - **Retrieve**: The file can be retrieved using the unique identifier, ensuring that there is no confusion with similarly named files.

### **Custom Exception Handling**

The **Files API** provides a sophisticated error-handling mechanism to manage validation errors and unexpected exceptions.

- **Pydantic Validation Errors**: The application uses **Pydantic** models for data validation. When the incoming request data is invalid (e.g., incorrect file format, missing parameters), the application catches these validation errors and returns structured error responses to the client.
  
- **Broad Exception Handling**: In addition to Pydantic errors, the application includes custom middleware to handle all other unexpected exceptions. This ensures that even when things go wrong, the API can provide meaningful error messages instead of generic server errors.

- **Error Responses**: Whenever an exception occurs, the API returns a structured error response, which includes an error code, a human-readable message, and detailed information for debugging. This helps users and developers easily identify and resolve issues.

### **Lambda Context Middleware**

For serverless environments (like AWS Lambda), the **Files API** includes middleware to inject the **Lambda context** into the HTTP request. This allows you to access runtime-specific information (e.g., request ID, function memory limits, timeouts) directly within the API request handling.

- **Serverless Compatibility**: The Lambda context middleware is a powerful feature for cloud deployments, allowing the API to behave like a fully serverless application. This integration is ideal for platforms like AWS Lambda, where resource limits and request contexts are crucial for managing scalability and performance.

- **Request Context**: In environments where the request context is critical (such as in cloud-based platforms), the middleware makes the Lambda-specific metadata available within the request. This can be used for logging, debugging, or performance monitoring.


### **Flexible Configuration Management**

The **Files API** provides a flexible configuration system powered by **Pydantic**. The configuration is easily customizable via environment variables or configuration files, ensuring that the application can be adapted to different environments and needs.

- **Configuration Settings**: Key settings such as **S3 bucket name** for file storage, **root path** for the API, and **logging levels** can all be customized.
  
- **Environment Variable Support**: The application reads configuration values from environment variables, allowing you to change settings without modifying the code. This makes the application easy to deploy across different environments (e.g., local development, staging, production).

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

### **Output Customization**
   - The generated OpenAPI schema can be saved to a specified location, ensuring that you have control over where the schema file is stored.
   - The schema is saved in **formatted JSON**, making it easy to read and verify manually, if needed.
   - You can also specify the file path for the output using the `--output-spec` argument.

### **Comprehensive Diffing Between Schemas**
   - The `get_diff_between_openapi_schemas` function allows you to compare the newly generated OpenAPI schema with any existing schema stored in your repository.
   - The comparison identifies and lists all the differences between the two schemas, helping developers spot API changes before they cause issues.
   - The diffing works at a very granular level, detecting even small changes that could affect API consumers.

### **Documentation**
   - The project includes detailed docstrings and comments, making the code easy to understand and extend.
   - The diff output and error messages are clear and informative, providing developers with sufficient context to understand what changed and where.

### **Logging and Monitoring**

While not directly tied to a specific endpoint, the **Files API** integrates comprehensive **logging and monitoring** features to track the performance and health of the application.

- **Lambda Context Integration**: Logs are enhanced with metadata from the Lambda context, providing better visibility into the request lifecycle.
  
- **Custom Logging**: The API uses a custom logging setup that captures key application events and exceptions, ensuring that administrators and developers can monitor the system effectively.

### **Support for FastAPI Applications**
   - The script is tailored for FastAPI applications and integrates seamlessly with them.
   - It supports FastAPI features such as custom routes, description, versioning, metadata, and more, ensuring that the generated OpenAPI schema is accurate and complete.

### **Docker Support**

For containerized environments, the **Files API** comes with a Docker configuration, allowing you to run the application in a containerized environment with minimal setup.

- **Dockerfile**: The included Dockerfile enables you to build and run the application in Docker, ensuring that it runs in a consistent environment across different machines and cloud platforms.

- **Cloud Deployments**: The Docker configuration can be easily adapted for deployments to cloud platforms like AWS ECS, Google Kubernetes Engine (GKE), or Azure Kubernetes Service (AKS), enabling automated and scalable deployments.


---

# API Endpoints

The **Files API** provides the following endpoints:

## 1. File Upload
**POST** `/files/upload`

Uploads a file to the server.

### Request Body:
- `file`: The file to upload.

### Response:
- `200 OK`: If the file upload is successful.
- `400 Bad Request`: If the file is missing or invalid.

---

## 2. File Retrieval
**GET** `/files/{file_id}`

Retrieves a file using its unique identifier.

### Path Parameters:
- `file_id`: The ID of the file to retrieve.

### Response:
- `200 OK`: If the file is found, the file content will be returned.
- `404 Not Found`: If the file with the given `file_id` does not exist.

---

## 3. OpenAPI Schema Generation
**GET** `/openapi.json`

Generates and returns the OpenAPI schema for the application.

### Response:
- `200 OK`: Returns the OpenAPI schema in JSON format.

---

## 4. OpenAPI Diff Generation
**POST** `/openapi-diff`

Generates an OpenAPI schema and compares it to an existing schema.

### Request Body:
- `existing_spec`: The existing OpenAPI specification in JSON format.

### Response:
- `200 OK`: If the diff operation was successful, with the differences in schema.
- `500 Internal Server Error`: If an error occurs during the diff process.

---

# Configuration

The app can be configured via environment variables or a configuration file. The following settings are available:

- `S3_BUCKET_NAME`: The name of the AWS S3 bucket for file storage.
- `ROOT_PATH`: The base path for the app (e.g., `/prod` for production).
- `LOGGING_LEVEL`: Controls the logging level for the application (default is `INFO`).

## Middleware & Error Handling

### 1. Custom Exception Handling

The project uses custom exception handlers for clean and predictable error management. It leverages FastAPI’s `exception_handler` to catch validation and unexpected errors. This approach provides both developers and users with informative error messages, improving the reliability of the application.

- **Pydantic Validation Errors**: Handles validation errors by catching them and providing a structured response. This ensures that users receive clear feedback when input is invalid.
- **Broad Exception Handling**: Catches unexpected exceptions globally and logs them for further analysis. This helps identify and troubleshoot issues that may arise during runtime.

This middleware ensures that the application continues to run smoothly, even in the event of an error, and provides helpful logs and error details for easier debugging.

### 2. Lambda Context Middleware

In serverless environments like AWS Lambda, it is often important to inject the Lambda context into every request to access runtime information (e.g., request ID, memory limits). This application includes a middleware function called `inject_lambda_context__middleware` to seamlessly integrate this feature.

This middleware can also be used in other cloud environments where the application is designed to run in a serverless context, such as AWS, Google Cloud, or Azure.

---

## OpenAPI Schema and Diffing

The project automatically generates the OpenAPI schema using FastAPI’s built-in OpenAPI tools. This schema can be used to describe and document the API's endpoints, request/response formats, and more.

Additionally, the project includes a feature for comparing the generated OpenAPI schema to an existing one. This is useful for tracking changes in the API over time, ensuring backward compatibility, and maintaining clear version control of the API specification.

By leveraging this diffing feature, developers can easily spot changes, review updates, and ensure that modifications to the API do not break existing functionality.


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

Built in mlops course: https://mlops-club.org/
