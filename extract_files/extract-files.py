import os
import sys
import shutil
import logging

def copy_jpg_png_to_destination(source_dir, destination_dir):
    logging.basicConfig(filename='copy_log.txt', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s: %(message)s')

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.png')):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_dir, file)

                try:
                    os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)
                    shutil.copyfile(source_file_path, destination_file_path)
                    print(f"Copied '{source_file_path}' to '{destination_file_path}'")
                except Exception as e:
                    error_msg = f"Error copying '{source_file_path}': {str(e)}"
                    logging.error(error_msg)
                    print(error_msg)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py source_directory_path destination_directory_path")
        sys.exit(1)

    source_directory_path = sys.argv[1]
    destination_directory_path = sys.argv[2]

    copy_jpg_png_to_destination(source_directory_path, destination_directory_path)
