def leap_year(input_value: str):
    if int(input_value) % 4 and int(input_value) % 100 != 0:
        return str("Y")
    if int(input_value) % 400 == 0:
        return str("Y")
    else:
        return str("N")
