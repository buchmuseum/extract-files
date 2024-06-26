# Read an excel file and save column B to a list:
import pandas as pd
import os

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
excel_file = "~/wz/extract-files/find_files/fehlende_Digitalisate_liste.xlsx"
path = "/mnt/b/Projekte/_Wasserzeichen/WZIS_Bilder/"

file_names = import_file_names(excel_file)

find_files(file_names, path)
