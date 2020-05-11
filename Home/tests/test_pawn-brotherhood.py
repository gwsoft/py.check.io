import Home

def test_safe_pawns1():
    assert Home.safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6

def test_safe_pawns2():
    assert Home.safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

def test_safe_pawns3():
    assert Home.safe_pawns({"a1", "a8", "h1", "h8"}) == 0

def test_safe_pawns4():
    assert Home.safe_pawns(["b4","c4","d4","e4","f4","g4","e3"]) == 2

def test_safe_pawns5():
    assert Home.safe_pawns(["e7","e6","d5","f5","c4","e4","g4","e8"]) == 3

def test_safe_pawns6():
    assert Home.safe_pawns(["a2","b4","c6","d8","e1","f3","g5","h8"]) == 0

def test_safe_pawns7():
    assert Home.safe_pawns(["b6","a7","b8","c7","g1","f2","h2","g3"]) == 6
