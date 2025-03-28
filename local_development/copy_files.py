import shutil
import os

def copy_files(source_dir, destination_dir):
  """
  Copies files from the source directory to the destination directory,
  organizing them into subdirectories based on their file extensions.
  Also writes the names of the created subdirectories to a text file.

  Args:
    source_dir: The path to the directory containing the files to copy.
    destination_dir: The path to the base destination directory.
  """
    
  if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)

  subdir_list = []  # List to store subdirectory names

  for filename in os.listdir(source_dir):
    source_path = os.path.join(source_dir, filename)
        
    if os.path.isfile(source_path):
      base, extension = os.path.splitext(filename)
      extension = extension[1:]
      subdir_list.append(extension)  # Add subdir name to the list

      subdir = os.path.join(destination_dir, extension)
      if not os.path.exists(subdir):
        os.makedirs(subdir)

      destination_path = os.path.join(subdir, filename)
      shutil.copy2(source_path, destination_path)

  # Write subdirectory names to a text file
  with open(os.path.join('.', "subdirectories.txt"), "w") as f:
    print(subdir_list)
    for subdir_name in subdir_list:
      f.write(subdir_name + "\n")

if __name__ == "__main__":
  # Set an environment variable
  os.environ['CSV_FILE_TYPE'] = 'TRUE'
  source_directory = "files"
  destination_directory = "docling_files_by_type"
  copy_files(source_directory, destination_directory)