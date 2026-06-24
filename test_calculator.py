from calculator import *

def test_add():
    assert add(2, 3) == 5

def test_substract():
    assert substract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(20, 5) == 4

def test_divide_by_zero():
    try:
        divide(5, 0)
        assert False
    except ValueError:
        assert True