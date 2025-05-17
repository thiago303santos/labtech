import pytest
from src.roman_numerals import RomanNumerals

@pytest.mark.parametrize("input,expected", [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (40, "XL"),
    (50, "L"),
    (90, "XC"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (900, "CM"),
    (1000, "M"),
    (1987, "MCMLXXXVII"),
    (3999, "MMMCMXCIX")
])
def test_int_to_roman(input, expected):
    assert RomanNumerals.converter(input) == expected