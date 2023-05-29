import pytest

@pytest.fixture
def input_value():
    input = 39
    return input

def test_divisible_by_three(input_value):
    assert input_value % 3 == 0

def test_divisible_by_seven(input_value):
    assert input_value % 7 == 0

def test_divisible_by_eight(input_value):
    assert input_value % 8 == 0
