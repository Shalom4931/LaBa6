def copy_file(source_file, destination_file):
    try:
        # Open the source file in read mode
        with open(source_file, 'r') as source:
            # Read the contents of the source file
            content = source.read()

        # Open the destination file in write mode
        with open(destination_file, 'w') as destination:
            # Write the contents to the destination file
            destination.write(content)
        
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print(f"Error: One of the files '{source_file}' or '{destination_file}' not found.")
    except IOError:
        print(f"Error: Unable to copy contents from '{source_file}' to '{destination_file}'.")

if __name__ == "__main__":
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the path of the destination file: ")
    copy_file(source_file, destination_file)