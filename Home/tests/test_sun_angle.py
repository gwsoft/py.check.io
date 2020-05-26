import Home

def test_sun_angle1():
    assert Home.sun_angle("07:00") == 15

def test_sun_angle2():
    assert Home.sun_angle("01:23") == "I don't see the sun!"

def test_sun_angle3():
    assert Home.sun_angle("12:30") == 97.5

def test_sun_angle4():
    assert Home.sun_angle("05:55") == "I don't see the sun!"

def test_sun_angle5():
    assert Home.sun_angle("18:01") == "I don't see the sun!"

def test_sun_angle6():
    assert Home.sun_angle("18:00") == 180

def test_sun_angle6():
    assert Home.sun_angle("06:00") == 0
