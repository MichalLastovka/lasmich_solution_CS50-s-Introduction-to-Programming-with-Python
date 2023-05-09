from jar import Jar
import pytest as p

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    with p.raises(ValueError):
        jar = Jar(5, 12)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar = Jar(10, 5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    jar = Jar(10, 0)
    with p.raises(ValueError):
        jar.deposit(11)

def test_withdraw():
    jar = Jar()
    with p.raises(ValueError):
        jar.withdraw(5)
    jar = Jar(10, 0)
    jar.deposit(5)
    jar.withdraw(3)
    assert str(jar) == "🍪🍪"


if __name__ == "__main__":
    main()
