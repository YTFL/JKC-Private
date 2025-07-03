import os
import re
from natsort import natsorted

def extract_numeric_part(filename):
    numeric_part = re.search(r'(\d+(\.\d+)?)', filename)
    if numeric_part:
        return float(numeric_part.group(1))
    else:
        return -1

def rename_files(directory, prefix):
    files = os.listdir(directory)

    files = natsorted(files, key=extract_numeric_part)

    for filename in files:
        name, extension = os.path.splitext(filename)
        new_name = f"{prefix}{filename}"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    directory_path = input("Enter the Directory of the Files: ")
    prefix = f"{os.path.basename(directory_path)}, "
    rename_files(directory_path, prefix)