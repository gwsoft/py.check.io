import Elementary
import pytest

def test_basic1():
	res = Elementary.backward_string('1345')
	assert res == '5431'

def test_basic2():
	assert Elementary.backward_string('val') == 'lav'

def test_basic3():
	assert Elementary.backward_string('') == ''

def test_basic4():
	assert Elementary.backward_string('ohho') == 'ohho'

def test_basic5():
	assert Elementary.backward_string('123456789') == '987654321'
