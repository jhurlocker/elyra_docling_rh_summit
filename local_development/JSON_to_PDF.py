def create_and_save_file(filename, content):
  try:
    with open(filename, 'w') as file:
      file.write(content)
    print(f"File '{filename}' created and saved successfully.")
  except Exception as e:
    print(f"An error occurred: {e}")

filename = "json_to_pdf_log.txt"


import os

def get_file_type_by_extension(filepath):
    """Get the file extension"""
    name, ext = os.path.splitext(filepath)
    return ext.lower()

# Example usage
file_path = "files/CELEX-CSV.pdf"
file_type = get_file_type_by_extension(file_path)
print(f"The file extension is: {file_type}")

text_content = f"This contains the logs for json_pdf.py. The file extension type is= {file_type}"
if file_type == ".csv":
    create_and_save_file(filename, text_content)
else:
    print("Not a CSV file type.")