import TwilioSendGrid

def test_stressful1():
    assert TwilioSendGrid.is_stressful("Hi") == False, "First"

def test_stressful2():
    assert TwilioSendGrid.is_stressful("I neeed HELP") == True, "Second"

def test_stressful3():
    assert TwilioSendGrid.is_stressful("We need you A.S.A.P.!!") == True, "Third"

def test_stressful4():
    assert TwilioSendGrid.is_stressful("I NEED YOU NOW!") == True, "4th"

def test_stressful5():
    assert TwilioSendGrid.is_stressful("What do I need to do???!!!!") == True, "5th"
