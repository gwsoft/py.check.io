import ElectronicStation

def test_digits_mul1():
    assert ElectronicStation.digits_multiplication(123405) == 120

def test_digits_mul2():
    assert ElectronicStation.digits_multiplication(999) == 729

def test_digits_mul3():
    assert ElectronicStation.digits_multiplication(1000) == 1

def test_digits_mul4():
    assert ElectronicStation.digits_multiplication(1111) == 1
