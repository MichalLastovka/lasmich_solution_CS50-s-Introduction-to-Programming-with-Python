from numb3rs import validate


def main():
    test_validate_st()
    test_validate_nd()

def test_validate_st():
    assert validate("") == False
    assert validate("...") == False
    assert validate("+.+.+.+") == False
    assert validate("cat") == False
    assert validate(r"\.\.\.") == False

def test_validate_nd():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.0.1") == True
    assert validate("256.255.255.255") == False
    assert validate("0.0.0.0.") == False
    assert validate("0.0.0.0.0") == False
    assert validate("0.0.0.256") == False


if __name__ == "__main__":
    main()
