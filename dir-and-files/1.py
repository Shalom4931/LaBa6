import os

def list_directories_and_files(path):
    try:
        print("Directories:")
        for item in os.listdir(path):
            if os.path.isdir(os.path.join(path, item)):
                print(item)

        print("\nFiles:")
        for item in os.listdir(path):
            if os.path.isfile(os.path.join(path, item)):
                print(item)

        print("\nAll directories and files:")
        for root, dirs, files in os.walk(path):
            for dir in dirs:
                print(os.path.join(root, dir))
            for file in files:
                print(os.path.join(root, file))

    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    path = input("Enter the path: ")
    list_directories_and_files(path)