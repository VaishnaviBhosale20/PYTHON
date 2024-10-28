def delete_file(python_demo):
    try:
        os.remove(python_demo)
        print(f"File '{python_demo}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting file: {e}")