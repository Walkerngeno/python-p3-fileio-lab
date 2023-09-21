# In lib/file_io.py

def write_file(file_name, file_content):
    # Append .txt extension to the file_name
    file_name_with_extension = f"{file_name}.txt"
    
    # Open the file for writing and write the content
    with open(file_name_with_extension, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Append .txt extension to the file_name
    file_name_with_extension = f"{file_name}.txt"
    
    # Open the file for appending and append the content
    with open(file_name_with_extension, 'a') as file:
        file.write("\n" + append_content)

def read_file(file_name):
    # Append .txt extension to the file_name
    file_name_with_extension = f"{file_name}.txt"
    
    # Open the file for reading and return its content
    with open(file_name_with_extension, 'r') as file:
        return file.read()
