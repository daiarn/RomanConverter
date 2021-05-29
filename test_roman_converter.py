import pytest

from main import RomanConverter


@pytest.fixture
def roman_converter():
    return RomanConverter()


@pytest.mark.parametrize("expected,test_input",
                         [("IV", 4), ("XXXIX", 39), ("CCXLVI", 246), ("DCCLXXXIX", 789), ("MMCDXXI", 2421),
                          ("MIX", 1009)])
def test_encoding(test_input, expected, roman_converter):
    assert expected == roman_converter.encode(test_input)


@pytest.mark.parametrize("test_input,expected",
                         [("IV", 4), ("XXXIX", 39), ("CCXLVI", 246), ("DCCLXXXIX", 789), ("MMCDXXI", 2421),
                          ("MIX", 1009)])
def test_decoding(test_input, expected, roman_converter):
    assert expected == roman_converter.decode(test_input)
