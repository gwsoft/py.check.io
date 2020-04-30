import Home

def test_first_word1():
    assert Home.first_word("Hello world") == "Hello"

def test_first_word2():
    assert Home.first_word(" a word ") == "a"

def test_first_word3():
    assert Home.first_word("don't touch it") == "don't"

def test_first_word4():
    assert Home.first_word("greetings, friends") == "greetings"

def test_first_word5():
    assert Home.first_word("... and so on ...") == "and"

def test_first_word6():
    assert Home.first_word("hi") == "hi"

def test_first_word7():
    assert Home.first_word("Hello.World") == "Hello"
