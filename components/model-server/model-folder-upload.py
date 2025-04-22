import boto3
import os
from botocore.exceptions import NoCredentialsError

def upload_folder_to_s3(local_folder, bucket_name, s3_folder='model'):
    """
    Uploads all files within a local folder to an Amazon S3 bucket.

    Args:
        local_folder (str): The path to the local folder containing files to upload.
        bucket_name (str): The name of the S3 bucket.
        s3_folder (str, optional): The destination folder within the S3 bucket.
                                     Defaults to the root of the bucket.
    """
    #s3 = boto3.client('s3')
    s3 = boto3.client('s3',
                    #endpoint_url='https://f{os.environ.get('MINIO_API_URL')}',
                    endpoint_url=f"https://{os.environ.get('MINIO_API_URL')}",
                    aws_access_key_id='minio',
                    aws_secret_access_key='minio123')

    for root, _, files in os.walk(local_folder):
        for filename in files:
            local_path = os.path.join(root, filename)
            relative_path = os.path.relpath(local_path, local_folder)
            s3_key = os.path.join(s3_folder, relative_path)

            # try:
            s3.upload_file(local_path, bucket_name, s3_key)
            print(f"Uploaded {local_path} to s3://{bucket_name}/{s3_key}")
            # except FileNotFoundError:
            #     print(f"Error: File not found at {local_path}")
            # except NoCredentialsError:
            #     print("Error: AWS credentials not found. Please configure your AWS credentials.")
            #     return
            # except Exception as e:
            #     print(f"An error occurred during upload: {e}")
            # return

if __name__ == "__main__":
    local_folder_to_upload = 'model'  # Replace with the actual path to your local folder
    s3_bucket_name = 'model-bucket'  # Replace with your S3 bucket name
    #s3_destination_folder = 'optional/s3/subfolder'  # Optional: Specify a folder in S3

    upload_folder_to_s3(local_folder_to_upload, s3_bucket_name)
    print("Folder upload process completed.")
