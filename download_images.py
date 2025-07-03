import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
import io

def is_comic_image(img_data):
    img = Image.open(io.BytesIO(img_data))
    return img.width > 600 and img.height > 600

def download_comic(url, save_path):
    os.makedirs(save_path, exist_ok=True)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img')

    for i, img_tag in enumerate(img_tags):
        img_url = img_tag.get('src')
        if img_url:
            img_data = requests.get(img_url).content

            if is_comic_image(img_data):
                with open(os.path.join(save_path, f"{i}.jpeg"), 'wb') as f:
                    f.write(img_data)

'''x = int(input("Enter the Width of Comic Page: "))
y = int(input("Enter the Height of Comic Page: "))'''