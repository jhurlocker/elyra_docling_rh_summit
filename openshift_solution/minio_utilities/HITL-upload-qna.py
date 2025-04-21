import boto3
from botocore.exceptions import ClientError
import os

def upload_file_to_minio(file_path, bucket_name, object_name=None, endpoint_url=os.environ.get('minio-url'), access_key='minio', secret_key='minio123'):
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
        object_name = os.path.basename(file_path)

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
file_path = 'qna-approved.yaml'  # Replace with the path to your file
bucket_name = 'data-files-bucket' # Replace with your bucket name

#create example file if it doesn't exist.
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is an example file.")

if upload_file_to_minio(file_path, bucket_name):
    print("Upload of Markdown file successful!")
else:
    print("Upload failed.")