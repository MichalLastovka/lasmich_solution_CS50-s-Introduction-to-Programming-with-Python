"""
Task:
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, 
but main is only called if the value of __name__ is "__main__".

Then, in a file called test_plates.py, implement four or more functions that collectively test your implementation of is_valid thoroughly, each of whose names should begin with test_ so that you can execute your tests.
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
