import zipfile
import os

def unzip_cbz(cbz_file):
    with zipfile.ZipFile(cbz_file, 'r') as zip_ref:
        cbz_basename = os.path.splitext(os.path.basename(cbz_file))[0]
        extract_dir = os.path.join(os.path.dirname(cbz_file), cbz_basename)
        os.makedirs(extract_dir, exist_ok=True)

        zip_ref.extractall(extract_dir)

        for filename in zip_ref.namelist():
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                new_filename = f"{cbz_basename}_p{filename}"
                os.rename(os.path.join(extract_dir, filename),
                          os.path.join(extract_dir, new_filename))

def main(cbz_directory):
    files = os.listdir(cbz_directory)
    cbz_files = [f for f in files if f.lower().endswith('.cbz')]

    if not cbz_files:
        print("No CBZ files found in the directory.")
        return

    for cbz_file in cbz_files:
        cbz_path = os.path.join(cbz_directory, cbz_file)
        print(f"Extracting {cbz_file}...")
        unzip_cbz(cbz_path)

    for cbz_file in cbz_files:
        cbz_path = os.path.join(cbz_directory, cbz_file)
        try:
            os.remove(cbz_path)
            print(f"Deleted {cbz_file}")
        except OSError as e:
            print(f"Error deleting {cbz_file}: {e.strerror}")

    print("Extraction and deletion complete.")

if __name__ == "__main__":
    cbz_directory = input("Enter the directory containing the CBZ files: ")
    main(cbz_directory)