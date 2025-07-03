from PIL import Image
import img2pdf
import os
import shutil


def to_pdf(image_directory, output_directory, output):
    output_pdf = os.path.join(output_directory, output)

    image_files = []

    min_width_points = 3  # Minimum width for an image in points
    min_height_points = 3  # Minimum height for an image in points

    dpi = 72  # Standard DPI for images

    for filename in sorted(os.listdir(image_directory)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            full_path = os.path.join(image_directory, filename)
            with Image.open(full_path) as img:
                width, height = img.size

                # Convert pixels to points
                width_points = width / dpi
                height_points = height / dpi

                # Calculate new size in pixels to meet minimum requirements in points
                if width_points < min_width_points:
                    new_width = int((min_width_points * dpi))
                    height_ratio = height / width
                    new_height = int(new_width * height_ratio)
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                if height_points < min_height_points:
                    new_height = int((min_height_points * dpi))
                    width_ratio = width / height
                    new_width = int(new_height * width_ratio)
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Save the resized image temporarily
                temp_path = os.path.splitext(full_path)[0] + "_temp.png"
                img.save(temp_path)

                # Add the path of the resized image to the list
                image_files.append(temp_path)

    if not image_files:
        print(f"No images found in {image_directory}. Skipping...")
        return

    with open(output_pdf, 'wb') as f:
        f.write(img2pdf.convert(image_files))

    print(f"Images in {image_directory} converted to {output_pdf}")

    # Delete the temporary files
    for temp_file in image_files:
        os.remove(temp_file)

    # Delete the entire folder after PDF conversion
    try:
        shutil.rmtree(image_directory)
        print(f"Deleted folder {image_directory}")
    except OSError as e:
        print(f"Error deleting folder {image_directory}: {e.strerror}")
    print("Folder has been deleted.")

def process_directories(parent_directory):
    subdirs = [d for d in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, d))]

    if not subdirs:
        print("No subdirectories found in the parent directory.")
        return

    for subdir in subdirs:
        image_directory = os.path.join(parent_directory, subdir)
        output_directory = parent_directory
        output_pdf_name = f"{subdir}.pdf"
        to_pdf(image_directory, output_directory, output_pdf_name)

    print("PDF conversion complete for all directories.")

if __name__ == "__main__":
    parent_directory = input("Enter the parent directory containing the image folders: ")
    process_directories(parent_directory)