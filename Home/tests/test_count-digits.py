import Home

def test_count_digits_regex1():
    assert Home.count_digits_regex('hi') == 0

def test_count_digits_regex2():
    assert Home.count_digits_regex('who is 1st here') == 1

def test_count_digits_regex3():
    assert Home.count_digits_regex('my numbers is 2') == 1

def test_count_digits_regex4():
    assert Home.count_digits_regex('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8

def test_count_digits_regex5():
    assert Home.count_digits_regex('5 plus 6 is') == 2

def test_count_digits_regex6():
    assert Home.count_digits_regex('') == 0

####
def test_count_digits_iter1():
    assert Home.count_digits_iter('hi') == 0

def test_count_digits_iter2():
    assert Home.count_digits_iter('who is 1st here') == 1

def test_count_digits_iter3():
    assert Home.count_digits_iter('my numbers is 2') == 1

def test_count_digits_iter4():
    assert Home.count_digits_iter('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8

def test_count_digits_iter5():
    assert Home.count_digits_iter('5 plus 6 is') == 2

def test_count_digits_iter6():
    assert Home.count_digits_iter('') == 0

