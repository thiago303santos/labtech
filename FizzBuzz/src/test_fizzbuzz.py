import pytest

from .fizz_buzz import FizzBuzz

@pytest.mark.parametrize("input_number, expected_output", [
    (1, '1'),
    (2, '2'),
    (7, '7'),
    (11, '11')
])
def test_print_number(input_number: int, expected_output: str):
    assert FizzBuzz.run(input_number) == expected_output

@pytest.mark.parametrize("input_number", [
    (3),
    (6),
    (9),
    (12),
    (18)
])
def test_print_Fizz(input_number):
    assert FizzBuzz.run(3) == "Fizz"

@pytest.mark.parametrize("input_number", [
    (5),
    (10),
    (20),
    (25),
    (35)
])
def test_print_Buzz(input_number):
    assert FizzBuzz.run(5) == "Buzz"

@pytest.mark.parametrize("input_number", [
    (15),
    (30),
    (60),
    (90)
])
def test_print_FizzBuzz(input_number):
    assert FizzBuzz.run(15) == "FizzBuzz"