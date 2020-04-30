import Home

def test_days_diff1():
    assert Home.days_diff((1982, 4, 19), (1982, 4, 22)) == 3

def test_days_diff2():
    assert Home.days_diff((2014, 1, 1), (2014, 8, 27)) == 238

def test_days_diff3():
    assert Home.days_diff((2014, 8, 27), (2014, 1, 1)) == 238
