# test_calulator.py

from calculator.calculations import add, subtract, multiply, divide


def test_addition():
    assert add(2, 4) == 6.


def test_subtraction():
    assert subtract(4, 2) == 2.


def test_multiplication():
    assert multiply(2, 4) == 8.


def test_division():
    assert divide(2, 4) == .5        