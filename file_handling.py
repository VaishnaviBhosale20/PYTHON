import os

def create_file(python_demo):
    try:
        with open(python_demo, 'w') as file:
            pass
        print(f"File '{python_demo}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")

def write_to_file(python_demo, content):
    try:
        with open(python_demo, 'a') as file:
            file.write(content)
        print(f"Content written to '{python_demo}' successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

def read_from_file(python_demo):
    try:
        with open(python_demo, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading from file: {e}")

def append_to_file(python_demo, content):
    try:
        with open(python_demo, 'a') as file:
            file.write(content)
        print(f"Content appended to '{python_demo}' successfully.")
    except Exception as e:
        print(f"Error appending to file: {e}")

def delete_file(python_demo):
    try:
        os.remove(python_demo)
        print(f"File '{python_demo}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")

python_demo = "python_demo.txt"

create_file(python_demo)

write_to_file(python_demo, "This is the first line.\n")
write_to_file(python_demo, "This is the second line.\n")

content = read_from_file(python_demo)
print("File contents:")
print(content)

append_to_file(python_demo, "This is an additional line.\n")

delete_file(python_demo)