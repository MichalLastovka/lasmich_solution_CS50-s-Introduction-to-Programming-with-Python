"""
Task:
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid 
if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns 
True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for 
is_valid to call (e.g., one function per requirement).

Requirements:
- “All vanity plates must start with at least two letters.”
- “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
- “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
   AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
- “No periods, spaces, or punctuation marks are allowed.”
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lenght_check(s):
        if alphanum_check(s):
            if st_char_check(s):
                if number_check(s):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def lenght_check(s):
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        return True

def alphanum_check(s):
    for c in s:
        if c.isdigit() == False and c.isalpha() == False:
            return False
    return True

def st_char_check(s):
    if s[0].isalpha():
        if s[1].isalpha():
            return True
        else:
            return False
    else:
        return False

def number_check(s):
    for c in s:
        if c.isdigit():
            if c == "0":
                return False
            else:
                pos = s.rfind(c)
                rest = s[pos:len(s)]
                for c in rest:
                    if c.isalpha():
                        return False
                else:
                    return True
    else:
        return True
        

if __name__ == "__main__":
    main()
