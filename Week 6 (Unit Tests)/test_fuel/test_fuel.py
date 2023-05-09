from fuel import convert, gauge
import pytest as p

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/10") == 10
    assert convert("1/100") == 1
    with p.raises(ValueError):
        convert("a/c")
    with p.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(69) == "69%"

if __name__ == "__main__":
    main()
