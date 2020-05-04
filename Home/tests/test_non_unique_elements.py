import Home

def test_non_unique_elements1():
    assert list(Home.non_unique_elements([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"

def test_non_unique_elements2():
    assert list(Home.non_unique_elements([1, 2, 3, 4, 5])) == [], "2nd example"

def test_non_unique_elements3():
    assert list(Home.non_unique_elements([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"

def test_non_unique_elements4():
    assert list(Home.non_unique_elements([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
