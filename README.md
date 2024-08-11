# Navttc-Task-14-Content-searching-from-multiple-files

# Directory Search Script

## Description

This Python script allows you to search for a specific keyword or phrase within all `.txt` files in a specified directory. It will return the line number and content of the line where the search term is found.

## Code

```python
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
```

## Steps

1. **Import Required Module:**
   - Import the `os` module, which is used for interacting with the operating system and traversing directories.

2. **Define the `search_in_file` Function:**
   - This function reads a file line by line and checks if the search term is present in any of the lines. 
   - If found, it prints the line number and content.

3. **Define the `search_in_directory` Function:**
   - This function traverses through the specified directory and subdirectories to find all `.txt` files.
   - It then calls `search_in_file` for each `.txt` file found.

4. **Main Program:**
   - The user is prompted to enter a directory path and a search term.
   - The script verifies if the directory exists and then searches for the term in all `.txt` files within the directory.

## How to Run

1. **Ensure Python is Installed:**
   - Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Save the Script:**
   - Save the provided Python code into a file named `14- Content searching from multiple files (Nasir Sharif).py`.

3. **Execute the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where `14- Content searching from multiple files (Nasir Sharif).py` is saved.
   - Run the script using the following command:
     ```bash
     python 14- Content searching from multiple files (Nasir Sharif).py
     ```

4. **Provide Input:**
   - When prompted, enter the directory path where you want to search.
   - Enter the keyword or phrase you want to search for.

## Example

- **Directory:** If you input `C:/Users/YourUsername/Documents`, the script will search in all `.txt` files within this directory.
- **Search Term:** If you input `"example"`, the script will look for this word in each `.txt` file and display the matching lines with their line numbers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Nasir Sharif at nasirsharifqasoori786@gmail.com
