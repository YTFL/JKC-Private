import os
from PIL import Image


def images_to_pdf(image_folder, output_pdf):
    image_files = [f for f in os.listdir(image_folder) if
                   f.endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp'))]

    image_files.sort()

    images = []

    for image_file in image_files:
        img_path = os.path.join(image_folder, image_file)
        img = Image.open(img_path).convert('RGB')
        images.append(img)

    if images:
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"PDF created successfully: {output_pdf}")
    else:
        print("No images found in the folder.")

image_folder = input("Enter the Location of the Images: ")
output_pdf = f'{os.path.basename(image_folder)}.pdf'

images_to_pdf(image_folder, output_pdf)
