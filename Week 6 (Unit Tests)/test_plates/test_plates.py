from plates import is_valid

def main():
    test_plates_st()
    test_plates_nd()
    test_plates_rd()
    test_plates_th()

def test_is_valid_st():
    assert is_valid("PI.14") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False

def test_is_valid_nd():
    assert is_valid("AE43") == True
    assert is_valid("CS50") == True
    assert is_valid("aabbcc") == True

def test_is_valid_rd():
    assert is_valid("aabbccd") == False
    assert is_valid("a123") == False
    assert is_valid("") == False

def test_is_valid_th():
    assert is_valid(".!.") == False
    assert is_valid("H") == False
    assert is_valid("aloha1") == True



if __name__ == "__main__":
    main()

