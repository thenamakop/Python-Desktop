import file_operations

# Writing to a file
file_operations.write_file('example.txt', 'Hello, world!')

# Appending to a file
file_operations.append_file('example.txt', '\nThis is an appended line.')

# Reading from a file
content = file_operations.read_file('example.txt')
print(content)