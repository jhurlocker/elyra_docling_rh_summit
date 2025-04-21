import boto3, os
from botocore.exceptions import ClientError
import subprocess
import requests

print(os.getenv("AWS_S3_ENDPOINT"))
s3_endpoint = os.getenv("AWS_S3_ENDPOINT")
#bucket_name = os.getenv("AWS_S3_BUCKET")

s3 = boto3.client(
    "s3",
    endpoint_url=s3_endpoint,
    aws_access_key_id='minio',
    aws_secret_access_key='minio123',
)
bucket = 'upload-files'
print("creating " + bucket + " bucket in minio")
if bucket not in [bu["Name"] for bu in s3.list_buckets()["Buckets"]]:
    s3.create_bucket(Bucket=bucket)

bucket2 = 'data-files-bucket'
print("creating " + bucket + " bucket in minio")
if bucket2 not in [bu["Name"] for bu in s3.list_buckets()["Buckets"]]:
    s3.create_bucket(Bucket=bucket2)

bucket3 = 'model-bucket'
print("creating " + bucket + " bucket in minio")
if bucket3 not in [bu["Name"] for bu in s3.list_buckets()["Buckets"]]:
    s3.create_bucket(Bucket=bucket3)


