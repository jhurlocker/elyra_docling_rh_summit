import boto3
import os

def download_file_from_s3(bucket_name, object_name, local_file_path, endpoint_url, access_key, secret_key, secure=False):
    """
    Downloads a file from an S3 bucket and saves it to a local directory.

    Args:
        bucket_name (str): The name of the S3 bucket.
        object_name (str): The name of the object (file) in the S3 bucket.
        local_file_path (str): The local path where the file will be saved.
        endpoint_url (str): The MinIO endpoint URL.
        access_key (str): The MinIO access key.
        secret_key (str): The MinIO secret key.
        secure (bool, optional): Whether to use HTTPS (default is False).

    Returns:
        bool: True if the file was downloaded successfully, False otherwise.
    """
    try:
        s3 = boto3.client(
            "s3",
            endpoint_url=endpoint_url,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
        )

        # Create the local directory if it doesn't exist
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)

        # Download the file
        s3.download_file(bucket_name, object_name, local_file_path)

        print(f"File '{object_name}' downloaded successfully to '{local_file_path}'.")
        return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:

local_directory = "../../instruct-generate/sourcedocs" #local directory to save to.
local_file_path1 = os.path.join(local_directory, '2304.14953v2-part1.pdf')
local_file_path2 = os.path.join(local_directory, '2304.14953v2-part2.docx')
bucket_name = "upload-files"
endpoint_url = "http://minio.summit-project-user10.svc.cluster.local:9000"  # Replace with your MinIO endpoint
access_key = "minio"             # Replace with your MinIO access key
secret_key = "minio123"             # Replace with your MinIO secret key

if download_file_from_s3(bucket_name, '2304.14953v2-part1.pdf', local_file_path1, endpoint_url, access_key, secret_key):
    print("Download complete.")
else:
    print("Download failed.")
if download_file_from_s3(bucket_name, '2304.14953v2-part2.docx', local_file_path2, endpoint_url, access_key, secret_key):
    print("Download complete.")
else:
    print("Download failed.")