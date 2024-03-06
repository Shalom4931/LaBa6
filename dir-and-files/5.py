def write_list_to_file(file_path, my_list):
    try:
        
        with open(file_path, 'w') as file:
           
            for item in my_list:
                file.write(str(item) + '\n')
        print(f"List has been written to '{file_path}' successfully.")
    except IOError:
        print(f"Error: Unable to write to the file '{file_path}'.")

if __name__ == "__main__":
    my_list = ["apple", "banana", "cherry", "date"]
    file_path = input("Enter the path of the file to write the list: ")
    write_list_to_file(file_path, my_list)