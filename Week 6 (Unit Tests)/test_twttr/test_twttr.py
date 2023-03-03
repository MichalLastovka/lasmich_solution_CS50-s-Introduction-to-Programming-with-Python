"""
Task:
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects
a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""
from twttr import shorten

def main():
    test_shorten()
    test_shorten_nd()

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("aeiou") == ""
    assert shorten("AEIOU") == ""
    assert shorten("Strč prst skrz krk") == "Strč prst skrz krk"

def test_shorten_nd():
    assert shorten("A4E3I1") == "431"
    assert shorten("A:E!I&0O") == ":!&0"


if __name__ == "__main__":
    main()
