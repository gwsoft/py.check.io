import Home

def test_between_markers1():
    assert Home.between_markers('What is >apple<', '>', '<') == "apple", "One sym"

def test_between_markers2():
    assert Home.between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"

def test_between_markers3():
    assert Home.between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'

def test_between_markers4():
    assert Home.between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'

def test_between_markers5():
    assert Home.between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'

def test_between_markers6():
    assert Home.between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
