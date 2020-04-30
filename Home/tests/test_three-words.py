import Home

def test_basic1():
    assert Home.three_words("Hello World hello") == True, "Hello"

def test_basic2():
    assert Home.three_words("He is 123 man") == False, "123 man"

def test_basic3():
    assert Home.three_words("1 2 3 4") == False, "Digits"

def test_basic4():
    assert Home.three_words("bla bla bla bla") == True, "Bla Bla"

def test_basic5():
    assert Home.three_words("Hi") == False, "Hi"