import Home

def test_lj1():
    assert Home.left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"

def test_lj2():
    assert Home.left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"

def test_lj3():
    assert Home.left_join(("brightness wright",)) == "bleftness wleft", "One phrase"

def test_lj4():
    assert Home.left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
