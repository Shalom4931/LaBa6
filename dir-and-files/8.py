import os

def delete_file(file_path):
    try:
        # Check if the path exists
        if not os.path.exists(file_path):
            print(f"The path '{file_path}' does not exist.")
            return

        # Check if the file is accessible
        if not os.access(file_path, os.F_OK):
            print(f"Error: File '{file_path}' is not accessible.")
            return

        # Delete the file
        os.remove(file_path)
        print(f"File '{file_path}' has been deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to delete file '{file_path}'.")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to delete: ")
    delete_file(file_path)