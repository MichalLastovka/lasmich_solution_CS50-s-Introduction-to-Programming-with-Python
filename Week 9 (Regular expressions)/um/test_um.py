from um import count

def mian():
    test_count_st()
    test_count_nd()
    test_count_rd()

def test_count_st():
    assert count("123") == 0
    assert count("?!.") == 0
    assert count("ABC") == 0
    assert count("") == 0

def test_count_nd():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count(", um") == 1
    assert count("um, ") == 1
    assert count("um um um, um, um?, um!") == 6

def test_count_rd():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2
    assert count("sum, mum, gum, rum, cum, bum") == 0
    assert count("documentation, circumference, argumentative") == 0
    assert count("bioluminescence, counterargument, humorlessnesses") == 0


if __name__ == "__main__":
    main()
