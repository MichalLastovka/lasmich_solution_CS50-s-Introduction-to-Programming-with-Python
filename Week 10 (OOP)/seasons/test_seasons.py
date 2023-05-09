from seasons import get_date, get_minutes, num_to_words
from datetime import date
import pytest as p

def main():
    test_get_date()
    test_get_minutes()
    test_num_to_words()

def test_get_date():
    assert get_date("1991-01-04") == date(1991, 1, 4)
    with p.raises(SystemExit):
        get_date("cat")
    with p.raises(SystemExit):
        get_date("1991, 01, 04")
    with p.raises(SystemExit):
        get_date("1991-13-04")
    with p.raises(SystemExit):
        get_date("")


def test_get_minutes():
    assert get_minutes(date(1991, 1, 4)) == 16917120
    assert get_minutes(date(2023, 3, 4)) == 1440
    assert get_minutes(date(2022, 3, 5)) == 525600
    assert get_minutes(date(2021, 3, 5)) == 1051200



def test_num_to_words():
    assert num_to_words(16917120) == "Sixteen million, nine hundred seventeen thousand, one hundred twenty"
    assert num_to_words(1440) == "One thousand, four hundred forty"
    assert num_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
    assert num_to_words(1051200) == "One million, fifty-one thousand, two hundred"


if __name__ == "__main__":
    main()
