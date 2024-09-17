import pytest

from src.atm_machine.atm_machine import Add


def test_add_with_negatives():
    with pytest.raises(ValueError) as exc_info:
        Add("1,-2,-3")

    assert str(exc_info.value) == "Negatives not allowed: -2 -3"


def test_add_no_negatives():
    assert Add("1,2,3") == 6


def test_add_empty_string():
    assert Add("") == 0


def test_add_single_number():
    assert Add("5") == 5


def test_add_mixed_numbers():
    assert Add("10,-1,5,-4,8") == 18  # Raises ValueError for negatives -1, -4
