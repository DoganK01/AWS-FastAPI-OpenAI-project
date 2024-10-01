# tests/unit_tests/s3/test__write_objects.py

import os
from uuid import uuid4

import boto3
from moto import mock_aws

from files_api.s3.write_objects import upload_s3_object
from tests.consts import TEST_BUCKET_NAME

# TEST_BUCKET_NAME = f"test-bucket-cloud-course-{str(uuid4())[:4]}"


@mock_aws
def test__upload_s3_object(mocked_aws: None):

    # 2. Upload a file to the bucket, with a particular content type
    object_key = "test.txt"
    file_content = b"Hello, world!"
    content_type = "text/plain"

    upload_s3_object(
        bucket_name=TEST_BUCKET_NAME,
        object_key=object_key,
        file_content=file_content,
        content_type=content_type,
    )

    # 3. Assert that the file was uploaded with the correct content type
    s3_client = boto3.client("s3")
    response = s3_client.get_object(Bucket=TEST_BUCKET_NAME, Key=object_key)
    assert response["ContentType"] == content_type
    assert response["Body"].read() == file_content