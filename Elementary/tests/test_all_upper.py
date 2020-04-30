import Elementary

def test_basic1():
    assert Elementary.is_all_upper('ALL UPPER') == True

def test_basic2():
    assert Elementary.is_all_upper('all lower') == False

def test_basic3():
    assert Elementary.is_all_upper('mixed UPPER and lower') == False

def test_basic4():
    assert Elementary.is_all_upper('') == True

def test_digits():
	assert Elementary.is_all_upper("123") == True

def test_threespaces():
	assert Elementary.is_all_upper("     ") == True
