from src.string_calculator.string_calculator import add


def test_blank_input():
    assert add("") == 0


def test_input_is_four():
    assert add("4") == 4


def test_values_csv():
    assert add("1,2") == 3


def test_values_csv_for_unknown_numbers():
    assert add("1,2,3,4,5,6,7,8,9") == 45


def test_multiple_deli():
    assert add("1\n2,3") == 6


def test_negative_number_and_bigger_than_1000():
    assert add("1,-2,-3,1000,4") == 5


def test_deli_inside_square_bracket():
    assert add("[***]\n1***2***3") == 6


def test_multiple_single_length_seperators():
    assert add("//[*][%]\n1*2%3") == 6


def test_multiple_longer_length_seperators():
    assert add("//[foo][bar]\n1foo2bar3") == 6
