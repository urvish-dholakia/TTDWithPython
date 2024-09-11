def fizzbuzz_int_string(input_value: str):
    if input_value == "":
        print("Give Input Value")
    elif input_value == "2":
        return int(input_value)
    elif input_value == "4":
        return int(input_value)
    str_to_list = input_value.split(",")
    for iterator in str_to_list:
        if iterator == "2":
            output_value = "Fizz"
            print(output_value)
        elif iterator == "4":
            output_value = "Buzz"
            print(output_value)
    return str(output_value)
