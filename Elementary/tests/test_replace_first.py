import Elementary

def test_rf1():
    assert list(Elementary.replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]

def test_rf2():
    assert list(Elementary.replace_first([1])) == [1]

def test_rf3():
    assert list(Elementary.replace_first([])) == []
