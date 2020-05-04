import Elementary

def test_is_even1():
    assert Elementary.is_even(2) == True

def test_is_even2():
    assert Elementary.is_even(5) == False

def test_is_even3():
    assert Elementary.is_even(0) == True
