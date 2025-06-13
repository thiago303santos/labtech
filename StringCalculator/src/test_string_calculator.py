import pytest
from src.string_calculator import StringCalculator

import pytest
from src.string_calculator import StringCalculator

@pytest.fixture
def calc():
    return StringCalculator()

@pytest.mark.parametrize("input_str, expected", [
    ("", 0),
    ("1", 1),
    ("1,2", 3),
    ("1,2,3,4,5", 15),
    ("1\n2,3", 6),
])
def test_add_variados(calc, input_str, expected):
    assert calc.add(input_str) == expected

def test_delimitador_customizado(calc):
    assert calc.add("//;\n1;2") == 3


