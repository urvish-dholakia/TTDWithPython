from src.fizzbuzz.fizzbuzz import fizzbuzz_str_to_int, fizzbuzz_int_to_specific_str


def test_str_to_int():
    assert fizzbuzz_str_to_int("2") == 2
    assert fizzbuzz_str_to_int("4") == 4


def test_int_to_specific_str():
    assert fizzbuzz_int_to_specific_str("2") == "Fizz"
    assert fizzbuzz_int_to_specific_str("4") == "Buzz"
