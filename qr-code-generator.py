# installing required packages
# pip install pyqrcode
# pip install pypng

# importing required packages
import pyqrcode
from PIL import Image

# getting user input
ip = input("Enter anything/link to generate a QR Code: ")

# generating the QR code and saving it as a PNG file
qr_code = pyqrcode.create(ip)
qr_code.png("QRCode_output.png", scale=9)

# displaying the QR code image in a new window
output = Image.open("QRCode_output.png")
output.show()

