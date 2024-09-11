from src.fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_input_for_3():
    assert fizzbuzz(3) == "Fizz"


def test_fizzbuzz_input_for_5():
    assert fizzbuzz(5) == "Buzz"


def test_fizzbuzz_input_for_6():
    assert fizzbuzz(6) == "Fizz"


def test_fizzbuzz_input_for_25():
    assert fizzbuzz(25) == "Buzz"


def test_fizzbuzz_input_for_1():
    assert fizzbuzz(1) == "1"


def test_fizzbuzz_input_for_15():
    assert fizzbuzz(15) == "FizzBuzz"
