import Elementary

def test_split_pairs1():
    assert list(Elementary.split_pairs('abcd')) == ['ab', 'cd']

def test_split_pairs2():
    assert list(Elementary.split_pairs('abc')) == ['ab', 'c_']

def test_split_pairs3():
    assert list(Elementary.split_pairs('abcdf')) == ['ab', 'cd', 'f_']

def test_split_pairs4():
    assert list(Elementary.split_pairs('a')) == ['a_']

def test_split_pairs5():
    assert list(Elementary.split_pairs('')) == []
