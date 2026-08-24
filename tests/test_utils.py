import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from utils import square, is_even, celsius_to_fahrenheit


def test_square():
    assert square(5) == 25


def test_is_even():
    assert is_even(10) is True
    assert is_even(5) is False


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
