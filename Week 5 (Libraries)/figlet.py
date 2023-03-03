"""
Task:
In a file called figlet.py, implement a program that:

    Expects zero or two command-line arguments:
        Zero if the user would like to output text in a random font.
        Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, 
        and the second of the two should be the name of the font.
    Prompts the user for a str of text.
    Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should 
exit via sys.exit with an error message.
"""


from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

def main():
    if len(sys.argv) == 1:
        font = random_font(fonts)
        text = get_text()
        figlet.setFont(font=font)
        print(figlet.renderText(text))
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        font = sys.argv[2]
        text = get_text()
        figlet.setFont(font=font)
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")


def random_font(fonts):
    pick = random.choice(fonts)
    return pick

def get_text():
    text = input("Input: ")
    return text


if __name__ == "__main__":
    main()
