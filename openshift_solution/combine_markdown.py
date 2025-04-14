# Generated markdown files
file1_name = '../../instruct-generate/resultdocs/2304.14953v2-part1.md'
file2_name = '../../instruct-generate/resultdocs/2304.14953v2-part2.md'

# Combined markdow file
destination_filename = '../../instruct-generate/resultdocs/combined.md'

# Open the first file in read mode ('r')
with open(file1_name, 'r') as file1:
  content1 = file1.read() # Read the entire content

# Open the second file in read mode ('r')
with open(file2_name, 'r') as file2:
  content2 = file2.read() # Read the entire content

# Open the destination file in write mode ('w')
# If the file exists, it will be overwritten. If not, it will be created.
with open(destination_filename, 'w') as destination_file:
  # Write the content of the first file, followed by the content of the second file
  destination_file.write(content1)
  destination_file.write(content2)

print(f"Files '{file1_name}' and '{file2_name}' successfully combined into '{destination_filename}'")