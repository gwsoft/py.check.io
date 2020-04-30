import Elementary

def test_nearest_val1():
    assert Elementary.nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10

def test_nearest_val2():
    assert Elementary.nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7

def test_nearest_val3():
    assert Elementary.nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8

def test_nearest_val4():
    assert Elementary.nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9

def test_nearest_val5():
    assert Elementary.nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4

def test_nearest_val6():
    assert Elementary.nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17

def test_nearest_val7():
    assert Elementary.nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8

def test_nearest_val8():
    assert Elementary.nearest_value({-1, 2, 3}, 0) == -1
