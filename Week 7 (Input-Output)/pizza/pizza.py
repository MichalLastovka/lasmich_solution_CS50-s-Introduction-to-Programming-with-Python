"""
Task:
In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a 
package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.
"""

import sys
import csv
from tabulate import tabulate

def main():
    get_file()
    file_name = sys.argv[1]
    print(get_table(file_name))


def get_file():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        try:
            name, suffix = sys.argv[1].split(".")
            if suffix != "csv":
                sys.exit("Not a CSV file")

        except FileNotFoundError:
            sys.exit("File does not exist")

def get_table(file_name):
    with open(file_name, "r") as price_list:
        reader = csv.DictReader(price_list)
        table = tabulate(reader, headers="keys", tablefmt="grid")
        return table


if __name__ == "__main__":
    main()
