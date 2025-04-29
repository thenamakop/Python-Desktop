def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def append_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)