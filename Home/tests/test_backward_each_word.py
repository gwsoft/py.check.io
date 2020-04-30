import Home

def test_backward_each_word1():
    assert Home.backward_string_by_word('') == ''

def test_backward_each_word2():
    assert Home.backward_string_by_word('world') == 'dlrow'

def test_backward_each_word3():
    assert Home.backward_string_by_word('hello world') == 'olleh dlrow'

def test_backward_each_word4():
    assert Home.backward_string_by_word('hello   world') == 'olleh   dlrow'

def test_backward_each_word5():
    assert Home.backward_string_by_word('welcome to a game') == 'emoclew ot a emag'

def test_backward_each_word6():
    assert Home.backward_string_by_word("ha ha ha   this is cool") == 'ah ah ah   siht si looc'
    
