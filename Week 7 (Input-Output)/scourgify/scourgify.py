"""
Task:
In a file called scourgify.py, implement a program that:

    Expects the user to provide two command-line arguments:
        the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
        the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
    Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

"""

from csv import DictReader, DictWriter
import sys

def main():
    get_files()
    read_st_file()

def get_files():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            name_st, suffix_st = sys.argv[1].split(".")
            name_nd, suffix_nd = sys.argv[2].split(".")
            if suffix_st != "csv" or suffix_nd != "csv":
                sys.exit("One or both of the file(s) is/are not CSV")
        except FileNotFoundError:
            sys.exit("File does not exist")

def read_st_file():
    st_file = sys.argv[1]
    nd_file = sys.argv[2]
    with open(st_file, "r") as read_file:
        reader = DictReader(read_file)
        with open(nd_file, "w", newline="") as write_file:
            writer = DictWriter(write_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                writer.writerow({"first": f"{first.strip()}", "last": f"{last.strip()}" , "house": f"{row['house']}"})




if __name__ == "__main__":
    main()
