import os

def search_in_file(file_path, search_term):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.readlines()
            for line_number, line in enumerate(contents, start=1):
                if search_term.lower() in line.lower():
                    print(f"Found in {file_path} on line {line_number}: {line.strip()}")
    except UnicodeDecodeError:
        print(f"Could not read file {file_path} due to encoding issues.")
    except Exception as e:
        print(f"Could not read file {file_path}. Error: {e}")

def search_in_directory(directory, search_term):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):  # Ensuring we're only reading text files
                file_path = os.path.join(root, file)
                search_in_file(file_path, search_term)

# Main Program
directory = input("Enter the directory path to search in: ")
search_term = input("Enter the keyword or phrase to search for: ")

if os.path.isdir(directory):
    search_in_directory(directory, search_term)
else:
    print("The directory does not exist.")
