import Home

def test_dt_converter1():
    assert Home.date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"

def test_dt_converter2():
    assert Home.date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"

def test_dt_converter3():
    assert Home.date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"

def test_dt_converter4():
    assert Home.date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute"

def test_dt_converter5():
    assert Home.date_time("09.07.1995 16:50") == "9 July 1995 year 16 hours 50 minutes"

def test_dt_converter6():
    assert Home.date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
