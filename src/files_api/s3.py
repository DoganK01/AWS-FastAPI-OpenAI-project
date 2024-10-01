import boto3
import os

try:
    from mypy_boto3_s3 import S3Client
    from mypy_boto3_s3.type_defs import (
        PutObjectOutputTypeDef,
        ResponseMetadataTypeDef,
    )
except ImportError:
    print("boto3-stubs[s3] not installed. Please run `pip install boto3-stubs[s3]`")

os.environ["AWS_PROFILE"] = "cloud-course"

BUCKET_NAME = "cloud-course-bucket-dogan"


session = boto3.Session()
s3_client: "S3Client" = session.client("s3")

# Write a file to the S3 bucket with the key 'folder/hello.txt' and the content 'Hello, World!'
response: "PutObjectOutputTypeDef" = s3_client.put_object(
    Bucket=BUCKET_NAME,
    Key="folder/hello.txt",
    Body="Hello World!",
    ContentType="text/plain")


metadata: "ResponseMetadataTypeDef" = response["ResponseMetadata"]