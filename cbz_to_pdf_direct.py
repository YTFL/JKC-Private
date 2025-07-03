import os
import zipfile
import img2pdf
import shutil
from PIL import Image


def resize_image(image, min_size, max_size):
    # Ensure image meets minimum size
    if image.size[0] < min_size[0] or image.size[1] < min_size[1]:
        ratio = max(min_size[0] / image.size[0], min_size[1] / image.size[1])
        new_size = (int(image.size[0] * ratio), int(image.size[1] * ratio))
        image = image.resize(new_size, Image.LANCZOS)

    # Ensure image does not exceed maximum size
    if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
        image.thumbnail(max_size, Image.LANCZOS)

    return image


def cbz_to_pdf(input_dir, min_size=(3, 3), max_size=(14400, 14400)):
    for filename in os.listdir(input_dir):
        if filename.endswith(".cbz"):
            filepath = os.path.join(input_dir, filename)
            temp_dir = os.path.join(input_dir, "_temp")
            os.makedirs(temp_dir, exist_ok=True)

            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(temp_dir)

            images = []
            for root, _, files in os.walk(temp_dir):
                for img in files:
                    img_path = os.path.join(root, img)
                    if img.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')):
                        try:
                            with Image.open(img_path) as image:
                                image = resize_image(image, min_size, max_size)
                                image.save(img_path)
                                images.append(img_path)
                        except Exception as e:
                            print(f"Error processing image {img_path}: {e}")

            if images:
                try:
                    pdf_bytes = img2pdf.convert(images)
                    pdf_path = os.path.join(input_dir, os.path.splitext(filename)[0] + ".pdf")
                    with open(pdf_path, "wb") as pdf_file:
                        pdf_file.write(pdf_bytes)
                except Exception as e:
                    print(f"Error converting images to PDF for file {filename}: {e}")
            else:
                print(f"No valid images found in {filename}")

            shutil.rmtree(temp_dir)

            os.remove(filepath)

    print("Conversion complete.")


if __name__ == "__main__":
    directory = input("Enter the Directory: ")
    cbz_to_pdf(directory)