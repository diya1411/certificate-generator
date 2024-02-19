import os
from PIL import Image, ImageFont, ImageDraw

# Global Variables
FONT_FILE = ImageFont.truetype(r'./GreatVibes-Regular.ttf', 80)

FONT_COLOR = "#28282B"

template = Image.open(r'template.png')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'template.png')
    draw = ImageDraw.Draw(image_source)

    # Calculate the width and height of the text dynamically
    name_width, name_height = 450, 15

    # Placing it in the center, then making some adjustments.
    # Adjust the y-coordinate by subtracting a fraction of the text's height
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - name_height * 0.1), name, fill=FONT_COLOR, font=FONT_FILE)

    # Define the directory path, cause can't let the certificates be in the same directory as the script, it's like not petting a cat, it's just wrong.
    meow_dir_path = "./out/"

    # Check if the directory exists, if not, create it
    if not os.path.exists(meow_dir_path):
        os.makedirs(meow_dir_path)

    # Saving the certificates in a different directory.
    image_source.save(meow_dir_path + name + ".png")
    print('Saving Certificate of:', name)


if __name__ == "__main__":

    names = []
    with open('name.txt') as f:
        content = f.readlines()
        for item in content:
            names.append(item[:-1].title())

    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")