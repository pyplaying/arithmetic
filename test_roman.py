#!/usr/bin/python3

import pytest

from roman import Roman

known_numerals = (
    ('I', 1),
    ('II', 2),
    ('III', 3),
    ('IV', 4),
    ('V', 5),
    ('VI', 6),
    ('IX', 9),
    ('X', 10),
    ('XI', 11),
    ('XVIII', 18),
    ('XCIV', 94),
    ('MMMDCCCLXXXVIII', 3888),
    ('MMMCMXCIX', 3999),
    ('MIX', 1009),
)
correct_numerals = [r for r, d in known_numerals]
incorrect_numerals = ['', 'IIII', 'IIX', 'VIV', 'IVI', 'B', 'MMMM', '0', '1', 'IM', 'CIVIL', 'DIM', 'VIXI', 'XIVI', 'VLIV', 'CIL', 'MIC']
incorrect_integers = [0, -1, -10, 4000, 4001, 10000, 1000000]


def test_correct_numerals():
    """is_roman_numeral should return True for correct roman numerals."""
    for numeral in correct_numerals:
        assert numeral == str(Roman(numeral))

def test_incorrect_numerals():
    """is_roman_numeral should return False for strings that are not roman numerals."""
    for numeral in incorrect_numerals:
        assert Roman.is_roman_numeral(numeral) == False

        with pytest.raises(ValueError):
            Roman(numeral)

def test_incorrect_integers():
    """Zero and negative integers are not supported."""
    for number in incorrect_integers:
        with pytest.raises(ValueError):
            Roman(number)

def test_bad_type():
    """is_roman_numeral should raise TypeError for non-string arguments"""
    for numeral in (None, 0, 1, 1.0):
        with pytest.raises(TypeError):
            Roman.is_roman_numeral(numeral)
    for obj in (None, 1.0):
        with pytest.raises(TypeError):
            Roman(numeral)

def test_from_integer():
    """Roman(integer) makes a correct numeral."""
    for numeral, value in known_numerals:
        assert str(Roman(value)) == numeral

def test_to_integer():
    """Roman(numeral) converts to the right integer."""
    for numeral, value in known_numerals:
        assert int(Roman(numeral)) == value

def test_inversion():
    for i in range(1, 4000):
        assert int(Roman(i)) == i

def test_eq():
    for i in range(1, 4000):
        assert Roman(i) == Roman(i)

def test_not_eq():
    assert Roman(1) != Roman(2)

def test_add():
    assert Roman(3987) + Roman(12) == Roman(3999)

def test_sub():
    assert Roman(3987) - Roman(18) == Roman(3969)

def test_mul():
    assert Roman(19) * Roman(12) == Roman(228)
