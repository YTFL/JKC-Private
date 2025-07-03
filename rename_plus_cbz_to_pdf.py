import renamer
import os
import cbz_to_pdf_direct

directory = input("Enter the Directory: ")
prefix = f"{os.path.basename(directory)}, "
renamer.rename_files(directory, prefix)
cbz_to_pdf_direct.cbz_to_pdf(directory)