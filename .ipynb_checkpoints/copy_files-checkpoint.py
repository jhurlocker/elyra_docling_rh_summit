def create_and_save_file(filename, content):
  try:
    with open(filename, 'w') as file:
      file.write(content)
    print(f"File '{filename}' created and saved successfully.")
  except Exception as e:
    print(f"An error occurred: {e}")

filename = "copy_files_log.txt"
text_content = """This contains the logs for copy_files.py"""

create_and_save_file(filename, text_content)