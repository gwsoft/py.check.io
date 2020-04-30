import Home
import pytest

def test_basic1():
    assert Home.even_last([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"

def test_basic2():
    assert Home.even_last([1, 3, 5]) == 30, "(1+5)*5=30"

def test_basic3():
    assert Home.even_last([6]) == 36, "(6)*6=36"

def test_basic4():
    assert Home.even_last([]) == 0, "An empty array = 0"
	
def test_new1():
	assert Home.even_last([1, 5, 2, 6, 7]) == 70, "Oops. (1+2+7)*7=70"
	
def test_new2():
	assert Home.even_last([27, 96, 70, 87]) == 8439
	
def test_compare_solutions():
	a = [0, 1, 2, 3, 4, 5]
	assert Home.even_last(a) == Home.even_last_slice(a)
	
def test_compare_solutions2():
	a = [12, 32, 6, 12, 5, 11, 21, 5]
	assert Home.even_last(a) == Home.even_last_slice(a)