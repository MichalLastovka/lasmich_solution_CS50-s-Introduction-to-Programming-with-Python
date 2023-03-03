"""
Task:
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels 
(A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""


def main():
    original = input("Input: ")
    translate = ""
    for c in original:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            translate += c
    print(f"Output: {translate}")






if __name__ == "__main__":
    main()
