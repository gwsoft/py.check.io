from Home import morse_decoder

def test_morse_decoder1():
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"

def test_morse_decoder2():
    assert morse_decoder("..--- ----- .---- ---..") == "2018"

def test_morse_decoder3():
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"

def test_morse_decoder4():
    assert morse_decoder(".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --..") == "Abcdefghijklmnopqrstuvwxyz"

def test_morse_decoder5():
    assert morse_decoder("----- .---- ..--- ...-- ....- ..... -.... --... ---.. ----.   .- .-. .   -.. .. --. .. - ...") == "0123456789 are digits"

def test_morse_decoder6():
    assert morse_decoder("...- ...-- .-. -.--   .---- ----- -. --.   ... - .-. .---- -. --.   .-- .---- - ....   ... ----- -- ...--   -. ..- -- -... ...-- .-. .....") == "V3ry 10ng str1ng w1th s0m3 numb3r5"
