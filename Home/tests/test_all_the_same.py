from Home import all_the_same

def test_all_the_same1():
    assert all_the_same([1, 1, 1]) == True

def test_all_the_same2():
    assert all_the_same([1, 2, 1]) == False

def test_all_the_same3():
    assert all_the_same(['a', 'a', 'a']) == True

def test_all_the_same4():
    assert all_the_same([]) == True

def test_all_the_same5():
    assert all_the_same([1]) == True

def test_all_the_same6():
    assert all_the_same([1,"a",1]) == False

def test_all_the_same7():
    assert all_the_same([600000]) == True

def test_all_the_same8():
    assert all_the_same([10000,99999]) == False
