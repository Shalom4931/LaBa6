import string

def generate_text_files():
    
    for letter in string.ascii_uppercase:
        file_name = letter + ".txt"
        try:
            
            with open(file_name, 'w') as file:
                file.write("This is the content of " + file_name)
            print(f"File '{file_name}' has been created successfully.")
        except IOError:
            print(f"Error: Unable to create the file '{file_name}'.")

if __name__ == "__main__":
    generate_text_files()