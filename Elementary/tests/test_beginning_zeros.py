import Elementary

def test_beginning_zeros1():
    assert Elementary.beginning_zeros('100') == 0

def test_beginning_zeros2():
    assert Elementary.beginning_zeros('001') == 2

def test_beginning_zeros3():
    assert Elementary.beginning_zeros('100100') == 0

def test_beginning_zeros4():
    assert Elementary.beginning_zeros('001001') == 2

def test_beginning_zeros5():
    assert Elementary.beginning_zeros('012345679') == 1

def test_beginning_zeros6():
    assert Elementary.beginning_zeros('0000') == 4
