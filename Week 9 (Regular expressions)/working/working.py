"""
Task:

In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00). 
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

    9:00 AM to 5:00 PM
    9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and 
end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

"""

import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        raise ValueError



def convert(s):
    try:
        start, finish = s.split(" to ")
        if re.search(r"(([1-9]|1[0-2]) (AM|PM))|(([1-9]|1[0-2]):[0-5][0-9] (AM|PM))", start).group():
            mod_start = clean(start)
        else:
            raise ValueError
        if re.search(r"(([1-9]|1[0-2]) (AM|PM))|(([1-9]|1[0-2]):[0-5][0-9] (AM|PM))", finish).group():
            mod_finish = clean(finish)
        else:
            raise ValueError

        return f"{mod_start} to {mod_finish}"

    except ValueError:
        raise ValueError
    except AttributeError:
        raise ValueError

def clean(str):
    time, noon = str.split(" ")
    if ":" in time:
        hours, minutes = time.split(":")
        if "AM" in noon and int(hours) == 12:
            return "00:00"
        elif "AM" in noon:
            return f"{(int(hours)):02}:{minutes}"
        elif "PM" in noon and int(hours) == 12:
            return "12:00"
        else:
            return f"{(int(hours) + 12):02}:{minutes}"
    else:
        if "AM" in noon and int(time) == 12:
            return "00:00"
        elif "AM" in noon:
            return f"{(int(time)):02}:00"
        elif "PM" in noon and int(time) == 12:
            return "12:00"
        else:
            return f"{int(time) + 12}:00"


if __name__ == "__main__":
    main()
