import Elementary

def test_between_markers1():
    assert Elementary.between_markers('What is >apple<', '>', '<') == "apple"

def test_between_markers2():
    assert Elementary.between_markers('What is [apple]', '[', ']') == "apple"

def test_between_markers3():
    assert Elementary.between_markers('What is ><', '>', '<') == ""

def test_between_markers4():
    assert Elementary.between_markers('>apple<', '>', '<') == "apple"

# Using regex

def test_between_markers_regex1():
    assert Elementary.between_markers_regex('What is >apple<', '>', '<') == "apple"

def test_between_markers_regex2():
    assert Elementary.between_markers_regex('What is [apple]', '[', ']') == "apple"

def test_between_markers_regex3():
    assert Elementary.between_markers_regex('What is ><', '>', '<') == ""

def test_between_markers_regex4():
    assert Elementary.between_markers_regex('>apple<', '>', '<') == "apple"
