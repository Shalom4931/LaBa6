import os

def analyze_path(path):
   
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

   
    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print(f"Filename: {filename}")
    print(f"Directory: {directory}")

if __name__ == "__main__":
    path = input("Enter the path to analyze: ")
    analyze_path(path)