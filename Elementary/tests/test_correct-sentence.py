import Elementary

def test_correct_sentence1():
    assert Elementary.correct_sentence("greetings, friends") == "Greetings, friends."

def test_correct_sentence2():
    assert Elementary.correct_sentence("Greetings, friends") == "Greetings, friends."

def test_correct_sentence3():
    assert Elementary.correct_sentence("Greetings, friends.") == "Greetings, friends."

def test_correct_sentence4():
    assert Elementary.correct_sentence("hi") == "Hi."

def test_correct_sentence5():
    assert Elementary.correct_sentence("welcome to New York") == "Welcome to New York."
