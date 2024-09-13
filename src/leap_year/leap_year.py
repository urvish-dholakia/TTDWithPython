def leap_year(input_value: str):
    if int(input_value) % 4 or int(input_value) % 100 == 0:
        return str("Y")
