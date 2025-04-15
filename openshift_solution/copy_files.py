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
local_file_path1 = os.path.join('sourcedocs/2304.14953v2-part1.pdf')
local_file_path2 = os.path.join('sourcedocs/2304.14953v2-part2.docx')
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

import pathlib # Import the pathlib module for path manipulation

# --- Configuration ---
# Define the directory name
directory_name = "resultdocs"
# Define the filename
file_name = "note.txt"

# --- Create Path Objects ---
# Create a Path object for the current directory
current_directory = pathlib.Path('.') # '.' represents the current directory
# Create a Path object for the target directory
target_directory = current_directory / directory_name # Use '/' to join paths

# --- Ensure Directory Exists ---
try:
    # Create the target directory if it doesn't exist.
    # parents=True: Creates any necessary parent directories.
    # exist_ok=True: Doesn't raise an error if the directory already exists.
    target_directory.mkdir(parents=True, exist_ok=True)
    print(f"Directory '{target_directory}' ensured.")
except OSError as e:
    print(f"Error creating directory '{target_directory}': {e}")
    # Decide if you want to exit or handle the error differently
    exit() # Exit if directory creation fails

# --- Construct Full File Path ---
# Combine the target directory path and the filename
full_file_path = target_directory / file_name
# Alternative using os.path.join:
# full_file_path_os = os.path.join(directory_name, file_name)
# print(f"Full file path: {full_file_path_os}") # Using os module

print(f"Full file path: {full_file_path}") # Using pathlib

# Define the content to write to the file
content_to_write = "Hello, this file is saved in a specific directory.\nThis is the second line."

# --- Create and Write to the File ---
try:
    # Open the file using the full path in write mode ('w')
    with open(full_file_path, 'w') as file:
        file.write(content_to_write)
        print(f"Successfully wrote to '{full_file_path}'")

except IOError as e:
    print(f"Error writing to file '{full_file_path}': {e}")


# --- Read from the File ---
try:
    # Open the same file using the full path in read mode ('r')
    with open(full_file_path, 'r') as file:
        read_content = file.read()
        print(f"\n--- Content read from '{full_file_path}' ---")
        print(read_content)
        print("------------------------------------")

except FileNotFoundError:
    print(f"Error: File '{full_file_path}' not found.")
except IOError as e:
    print(f"Error reading from file '{full_file_path}': {e}")



# Specify the directory path
directory_path = '.' # '.' represents the current directory
# Or use an absolute path like:
# directory_path = '/path/to/your/directory' # Linux/macOS
# directory_path = r'C:\path\to\your\directory' # Windows (raw string)

try:
  entries = os.listdir(directory_path)
  print(f"Entries in '{directory_path}':")
  for entry in entries:
    print(entry)

  # --- If you want only files ---
  print("\n--- Files Only ---")
  files_only = [f for f in entries if os.path.isfile(os.path.join(directory_path, f))]
  for file_name in files_only:
    print(file_name)

  # --- If you want only directories ---
  print("\n--- Directories Only ---")
  dirs_only = [d for d in entries if os.path.isdir(os.path.join(directory_path, d))]
  for dir_name in dirs_only:
    print(dir_name)

except FileNotFoundError:
  print(f"Error: The directory '{directory_path}' was not found.")
except PermissionError:
  print(f"Error: Permission denied to access '{directory_path}'.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")