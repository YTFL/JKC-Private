import zipfile
import os
import shutil

def create_cbz(images_dir, output_file):
    with zipfile.ZipFile(output_file, 'w') as output_zip:
        for root, _, files in os.walk(images_dir):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    file_path = os.path.join(root, file)
                    output_zip.write(file_path, arcname=os.path.relpath(file_path, images_dir))


def main(images_dir, output_filename, output_path):

    if not images_dir.endswith(os.path.sep):
        images_dir += os.path.sep

    if not output_path.endswith(os.path.sep):
        output_path += os.path.sep

    output_file = os.path.join(output_path, output_filename)

    if not os.path.exists(images_dir):
        print("Directory does not exist.")
    else:
        create_cbz(images_dir, output_file)
        print("CBZ file created successfully!")

        shutil.rmtree(images_dir)
        print("Images directory deleted.")

if __name__ == "__main__":
    images_dir = input("Enter the directory containing the images: ").strip()
    output_filename = input("Enter the name of the CBZ file (including extension): ").strip()
    output_path = input("Enter the directory where you want to save the CBZ file: ").strip()
    main(images_dir, output_filename, output_path)