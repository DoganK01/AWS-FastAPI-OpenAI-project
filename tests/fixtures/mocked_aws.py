# tests/fixtures/mocked_aws.py

"""Pytest fixture to mock AWS services."""

import os

import boto3
import pytest
from moto import mock_aws
from pytest import fixture

from tests.consts import TEST_BUCKET_NAME


# Set the environment variables to point away from AWS
def point_away_from_aws():
    os.environ["AWS_ACCESS_KEY_ID"] = "testtest"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testtest"
    os.environ["AWS_SECURITY_TOKEN"] = "testtest"
    os.environ["AWS_SESSION_TOKEN"] = "testtest"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


# Our fixture is a function and we have named it as a noun instead
# of verb, because it is a resource that'll be provided to our tests
# as arguments.


@pytest.fixture(scope="function")
def mocked_aws():
    with mock_aws():
        # Set the environment variables to point away from AWS
        point_away_from_aws()

        # 1. Create an S3 bucket
        s3_client = boto3.client("s3")
        # aws_region = os.environ.get("AWS_REGION", "us-east-1")
        s3_client.create_bucket(Bucket=TEST_BUCKET_NAME)

        yield

        # 4. Clean up/Teardown by deleting the bucket
        response = s3_client.list_objects_v2(Bucket=TEST_BUCKET_NAME)
        for obj in response.get("Contents", []):
            s3_client.delete_object(Bucket=TEST_BUCKET_NAME, Key=obj["Key"])

        s3_client.delete_bucket(Bucket=TEST_BUCKET_NAME)
        print("Hello from cleanup")
