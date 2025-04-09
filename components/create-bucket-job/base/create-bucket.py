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
    
# Upload model to bucket

def upload_file_to_minio(file_path, bucket_name, object_name=None, endpoint_url=s3_endpoint, access_key='minio', secret_key='minio123'):
    """Upload a file to an S3 bucket.

    Args:
        file_path: File to upload.
        bucket_name: Bucket to upload to.
        object_name: S3 object name. If not specified then file_path is used.
        endpoint_url: MinIO endpoint URL.
        access_key: MinIO access key.
        secret_key: MinIO secret key.

    Returns:
        True if file was uploaded, else False.
    """

    # If S3 object_name was not specified, use file_path
    if object_name is None:
        object_name = 'a-model/' + os.path.basename(file_path)

    # Create an S3 client
    s3_client = boto3.client('s3',
                              endpoint_url=endpoint_url,
                              aws_access_key_id=access_key,
                              aws_secret_access_key=secret_key)
    try:
        response = s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' uploaded to '{bucket_name}/{object_name}'")
        return True
    except ClientError as e:
        print(f"Error uploading file: {e}")
        return False
    except FileNotFoundError:
      print(f"Error: File '{file_path}' not found.")
      return False

# Example usage (replace with your actual values):
file_path = '/models/IntroToML_Cert.pdf'  # Replace with the path to your file
bucket_name = 'model-bucket' # Replace with your bucket name

#create example file if it doesn't exist.
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is an example file.")

if upload_file_to_minio(file_path, bucket_name):
    print("Upload of PDF file successful! Data Science Pipeline should be starting.")
else:
    print("Upload failed.")


