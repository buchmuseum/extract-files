# Read an excel file with mssing files and find the files in the given path


import pandas as pd
import os
import sys

def import_file_names(excel_file):
    # read excel file and save the second column to a list
    df = pd.read_excel(excel_file)
    file_names = df.iloc[:, 1].tolist()
    return file_names

def find_files(file_names, path):
    # Iterate over the list of file names and check if the file exists in the given path and subdirectories
    for file_name in file_names:
        print(f"Looking for: {file_name}")
        # Iterate over the subdirectories
        for root, dirs, files in os.walk(path):
            for file in files:
                # If file_name is part of the file name, print the full path
                # and break out of the loop
                if file_name in file:
                    print(f"Found file: {os.path.join(root, file)}")
                    # Write the full path of the file to a text file
                    with open("found_files.txt", "a") as f:
                        f.write(os.path.join(root, file) + "\n")
                    break
                else:
                    continue

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py excel_file path")
        sys.exit(1)

    excel_file = sys.argv[1]
    path = sys.argv[2] 

    # Read the excel file and save the second column to a list
    file_names = import_file_names(excel_file)
    # Iterate over the list of file names and check if the file exists in the given path and subdirectories
    find_files(file_names, path)
