import Elementary

def test_maxdigit1():
    assert Elementary.max_digit(0) == 0

def test_maxdigit2():
    assert Elementary.max_digit(0) == 0

def test_maxdigit3():
    assert Elementary.max_digit(52) == 5

def test_maxdigit4():
    assert Elementary.max_digit(634) == 6

def test_maxdigit5():
    assert Elementary.max_digit(1) == 1

def test_maxdigit6():
    assert Elementary.max_digit(10000) == 1
