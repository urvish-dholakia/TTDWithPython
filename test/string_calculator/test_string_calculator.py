from src.string_calculator.string_calculator import add


def test_blank_input():
        assert add("") == 0


def test_input_is_four():
        assert add("4") == 4


def test_values_csv():
        assert add("1,2") == 3
