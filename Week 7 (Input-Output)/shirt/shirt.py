"""
Task:
In a file called shirt.py, implement a program that expects exactly two command-line arguments:

    in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
    in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

The program should then overlay shirt.png (which has a transparent background) on the input after resizing and cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open, resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit, using default values for method, bleed, and centering, overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste, and save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.

The program should instead exit via sys.exit:

    if the user does not specify exactly two command-line arguments,
    if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    if the input’s name does not have the same extension as the output’s name, or
    if the specified input does not exist.

"""


import os
import sys
from PIL import Image, ImageOps

def main():
    inputs = check_inputs()
    modify_inputs(inputs)

def check_inputs():
    valid_ext = [".jpg", ".jpeg", ".png"]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(sys.argv[1])[1].lower() not in valid_ext or os.path.splitext(sys.argv[2])[1].lower() not in valid_ext:
        sys.exit("Ivalid input")
    elif os.path.splitext(sys.argv[1])[1].lower() != os.path.splitext(sys.argv[2])[1].lower():
        sys.exit("Input and output have different extensions")
    else:
        try:
            input = sys.argv[1]
            output = sys.argv[2]
            return input, output
        except FileNotFoundError:
            sys.exit("File does not exist")


def modify_inputs(inputs):
    input = inputs[0]
    output = inputs[1]
    shirt = Image.open("shirt.png")
    size = shirt.size
    print(size)

    with Image.open(input) as im:
        cropped = ImageOps.fit(im, size, bleed=0.0, centering=(0.5, 0.5))
        cropped.paste(shirt, shirt)
        cropped.save(output)


if __name__ == "__main__":
    main()
