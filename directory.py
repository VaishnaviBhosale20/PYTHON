import os
import shutil

def create_directory(path):
    """Creates a new directory at the specified path."""
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")

def list_directory(path):
    """Lists files and directories in the specified path."""
    try:
        items = os.listdir(path)
        print(f"Contents of '{path}':")
        for item in items:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")

def delete_directory(path):
    """Deletes a directory at the specified path."""
    try:
        shutil.rmtree(path)
        print(f"Directory '{path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")

def rename_directory(path, new_name):
    """Renames a directory at the specified path."""
    try:
        new_path = os.path.join(os.path.dirname(path), new_name)
        os.rename(path, new_path)
        print(f"Directory '{path}' renamed to '{new_path}'.")
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")

if __name__ == "__main__":
    while True:
        print("\nDirectory Management Menu:")
        print("1. Create directory")
        print("2. List directory contents")
        print("3. Delete directory")
        print("4. Rename directory")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter the path for the new directory: ")
            create_directory(path)
        elif choice == "2":
            path = input("Enter the path to list: ")
            list_directory(path)
        elif choice == "3":
            path = input("Enter the path to delete: ")
            delete_directory(path)
        elif choice == "4":
            path = input("Enter the path to rename: ")
            new_name = input("Enter the new name: ")
            rename_directory(path, new_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")