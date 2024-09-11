from src.fizzbuzz.fizzbuzz import fizzbuzz_int_string


def test_str_to_int():
    assert fizzbuzz_int_string("2") == 2
    assert fizzbuzz_int_string("4") == 4


def test_int_to_specific_str():
    assert fizzbuzz_int_string("2,4")
