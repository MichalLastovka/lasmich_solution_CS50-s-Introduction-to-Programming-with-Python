from bank import value

def main():
    test_value_st()

def test_value_st():
    assert value("Hello") == 0
    assert value("Hi") == 20
    assert value("0") == 100
    assert value("Hakunamatata") == 20
    assert value("100") == 100
    assert value("!?:") == 100
    assert value("HI") == 20
    assert value("HELLO") == 0


if __name__ == "__main__":
    main()
