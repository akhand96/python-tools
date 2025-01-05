# install required libraries
# pip install webcolors

#importing required libraries
from webcolors import name_to_hex

# function to convert color name to hex code using webcolors library
def color2hex(color_name):
    try:
        color_code = name_to_hex(color_name)
        return color_code
    except ValueError:
        return None

# get user input for color name and convert it to hex code
color = input("Enter the Color Name for getting Hex Code: ")
result = color2hex(color)

print("The Hex Code for {0} Color is: {1}".format(color, result))