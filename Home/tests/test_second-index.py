import Home

def test_second_index1():
    assert Home.second_index("sims", "s") == 3, "First"

def test_second_index2():
    assert Home.second_index("find the river", "e") == 12, "Second"

def test_second_index3():
    assert Home.second_index("hi", " ") is None, "Third"

def test_second_index4():
    assert Home.second_index("hi mayor", " ") is None, "Fourth"

def test_second_index5():
    assert Home.second_index("hi mr Mayor", " ") == 5, "Fifth"

def test_second_index6():
    assert Home.second_index("three occurrences","r") == 10, "Sixth"
