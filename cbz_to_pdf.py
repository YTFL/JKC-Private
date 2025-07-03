import os
import unzip_cbz_bulk
import pdf_bulk
import renamer

directory = input("Enter the Directory for Conversion: ")
prefix = f"{os.path.basename(directory)}, "
renamer.rename_files(directory, prefix)
unzip_cbz_bulk.main(directory)
pdf_bulk.process_directories(directory)