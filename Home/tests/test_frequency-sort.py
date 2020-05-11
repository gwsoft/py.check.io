import Home

def test_frequency_sort1():
    assert list(Home.frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]

def test_frequency_sort2():
    assert list(Home.frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']

def test_frequency_sort3():
    assert list(Home.frequency_sort([17, 99, 42])) == [17, 99, 42]

def test_frequency_sort4():
    assert list(Home.frequency_sort([])) == []

def test_frequency_sort5():
    assert list(Home.frequency_sort([1])) == [1]
