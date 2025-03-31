import boto3
from botocore.exceptions import ClientError
import os

def download_file_from_minio(bucket_name, object_name, local_file_path, endpoint_url='https://minio-api-minio.apps.cluster-w8qmq.w8qmq.sandbox219.opentlc.com', access_key='minio', secret_key='minio123'):
    """Download a file from an S3 bucket.

    Args:
        bucket_name: Bucket to download from.
        object_name: S3 object name.
        local_file_path: Local path to save the downloaded file.
        endpoint_url: MinIO endpoint URL.
        access_key: MinIO access key.
        secret_key: MinIO secret key.

    Returns:
        True if file was downloaded, else False.
    """

    s3_client = boto3.client('s3',
                              endpoint_url=endpoint_url,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)
    try:
        s3_client.download_file(bucket_name, object_name, local_file_path)
        print(f"File '{object_name}' downloaded to '{local_file_path}'")
        return True
    except ClientError as e:
        print(f"Error downloading file: {e}")
        return False
    except Exception as e: #Catching any other potential error.
        print(f"An unexpected error occurred: {e}")
        return False

bucket_name = 'data-files-bucket' 
object_name = 'my-file3.txt' 
local_file_path = 'docling-markdown-review.md' 

if download_file_from_minio(bucket_name, object_name, local_file_path):
    print("Download successful!")
else:
    print("Download failed.")