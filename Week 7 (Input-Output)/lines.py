"""
Task:
In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file, and outputs the number of lines of code in that file, 
excluding comments and blank lines. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, 
the program should instead exit via sys.exit. Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a comment.) Assume that 
any line that only contains whitespace is blank.
"""

import sys

def main():
    check_args()
    print(read_and_count())


def check_args():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    try:
        name, suffix = sys.argv[1].split(".")
        if suffix != "py":
            sys.exit("Not a Python file")
    except ValueError:
        sys.exit("Not a Python file")


def read_and_count():
    lines_count = 0
    try:
        with open(f"{sys.argv[1]}", "r") as code:
            lines = code.readlines()
        for line in lines:
            if line.lstrip().startswith("#"):
                pass
            elif line.strip() == "":
                pass
            else:
                lines_count +=1
        return lines_count
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
