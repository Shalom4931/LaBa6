from docx import Document

def count_lines_in_docx(file_path):
    try:
        
        doc = Document(file_path)
        
        line_count = len(doc.paragraphs)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1
    except Exception as e:
        print(f"Error: Unable to read the file '{file_path}'. {e}")
        return -1

if __name__ == "__main__":
    file_path = input("Enter the path of the .docx file: ").strip('"')
    lines_count = count_lines_in_docx(file_path)
    if lines_count != -1:
        print(f"The number of lines in the file '{file_path}' is: {lines_count}")