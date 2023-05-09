"""
Task:

In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer, 
using English words instead of numerals, just like the song from Rent, without any and between words. Since a user might not know the time at which they were born, assume, for simplicity, that the user was born 
at midnight (i.e., 00:00:00) on that date. And assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. 
Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.

Structure your program per the below, not only with a main function but also with one or more other functions as well:
"""

import sys
import inflect
from datetime import date


def main():
    dob = get_date(input("Date of Birth: "))
    minutes = get_minutes(dob)
    min_words = num_to_words(minutes)
    return print(min_words, "minutes")

def get_date(dob):
    try:
        year, month, day = dob.split("-")
        dob_format = date(int(year), int(month), int(day))
        return dob_format
    except ValueError:
        sys.exit("Invalid format")

def get_minutes(dob):
    days = (date.today() - dob)
    minutes = days.days * 24 * 60
    return minutes

def num_to_words(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return words.capitalize()

if __name__ == "__main__":
    main()
