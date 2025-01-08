# installing required packages
# pip install rembg
# pip install pillow

# importing required packages
from rembg import remove
from PIL import Image

# setting input and output path
input_path = input("Enter the image path: ")
output_path = "output_removed_bg.png"

# main logic
ip = Image.open(input_path)
op = remove(ip)
op.save(output_path)

