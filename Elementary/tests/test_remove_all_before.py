import Elementary
import pytest

def test_basic1():
    assert list(Elementary.remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]

def test_basic2():
    assert list(Elementary.remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]

def test_basic3():
    assert list(Elementary.remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]

def test_basic4():
    assert list(Elementary.remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]

def test_basic5():
    assert list(Elementary.remove_all_before([], 0)) == []

def test_basic6():
    assert list(Elementary.remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]