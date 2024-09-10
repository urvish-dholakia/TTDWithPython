def fizzbuzz_str_to_int(input_value: str):
    if input_value == str("2"):
        input_value = int(input_value)
    elif input_value == str("4"):
        input_value = int(input_value)
    else:
        input_value = 1


def fizzbuzz_int_to_specific_str(input_value: str):
    if input_value == int(2):
        output_value = "Fizz"
    elif input_value == int(4):
        output_value = "Buzz"
