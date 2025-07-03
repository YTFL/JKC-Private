import unzip_cbz
import create_cbz
import os

vol_main_dir = input("Enter the Main Directory of the Volumes: ").strip()
output_path = input("Enter the directory where you want to save the CBZ file: ").strip()
cmc_name = os.path.basename(vol_main_dir)

for root, dirs, files in os.walk(vol_main_dir):
    dirs.sort()
    files.sort()
    if files:
        vol_name = os.path.basename(root)
        cbz_directory = root
        print(root)
        output_filename = f"{cmc_name}, {vol_name}.cbz"
        print(output_filename)
        '''for filename in files:
            output_filename = f"{cmc_name}, {vol_name}.cbz"
            print(output_filename)'''

        unzip_cbz.main(cbz_directory)
        create_cbz.main(cbz_directory, output_filename, output_path)