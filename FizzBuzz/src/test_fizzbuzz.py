import pytest
from .fizz_buzz import FizzBuzz

@pytest.mark.parametrize("input,expected", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz")
])
def test_FizzBuzz(input, expected):
    assert FizzBuzz.run(input) == expected
