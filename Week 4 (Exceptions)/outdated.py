"""
Task:
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, 
formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. 
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date = get_date()
    print(date)

def get_date():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month, day, year = date.split("/")
                if month.strip().isdigit() and day.strip().isdigit() and year.strip().isdigit():
                    month = int(month.strip())
                    day = int(day.strip())
                    year = int(year.strip())
                    if day < 1 or day > 31 or month < 1 or month > 12:
                        pass
                    else:
                        date = f"{year}-{month:02}-{day:02}"
                        return date
                else:
                    pass
            elif "," in date:
                month_day, year = date.split(",")
                month, day = month_day.split(" ")
                year = year.strip()
                if day.isdigit() and year.isdigit() and month.isalpha():
                    if month in months:
                        day = int(day)
                        year = int(year)
                        month = months.index(month) + 1
                        if day < 1 or day > 31 or month < 1 or month > 12:
                            pass
                        else:
                            date = f"{year}-{month:02}-{day:02}"
                            return date
                    else:
                        pass
                else:
                        pass
            else:
                pass

        except ValueError:
            pass


if __name__ == "__main__":
    main()
