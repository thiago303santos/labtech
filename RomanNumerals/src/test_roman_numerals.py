import pytest
from src.roman_numerals import RomanNumerals

@pytest.mark.parametrize("entrada, esperado",[
    (1,"I"),
    (2,"II"),
    (3,"III"),
    (4,"IV"),
    (5,"V"),
    (6,"VI"),
    (7,"VII"),
    (8,"VIII"),
    (9,"IX"),
    (10,"X"),
    (14,"XIV"),
    (44,"XLIV"),
    (99,"XCIX"),
    (3999,"MMMCMXCIX")
])
def test_converter(entrada, esperado):
    assert RomanNumerals.converter(entrada) == esperado