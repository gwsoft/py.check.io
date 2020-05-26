from Home import split_list

def test_split_list1():
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]

def test_split_list2():
    assert split_list([1, 2, 3]) == [[1, 2], [3]]

def test_split_list3():
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]

def test_split_list4():
    assert split_list([1]) == [[1], []]

def test_split_list5():
    assert split_list([]) == [[], []]

def test_split_list6():
    assert split_list([1,1,1,1,1]) == [[1,1,1],[1,1]]

def test_split_list7():
    assert split_list([6,7,8,9]) == [[6,7],[8,9]]
