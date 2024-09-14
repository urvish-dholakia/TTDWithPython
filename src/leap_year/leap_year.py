def leap_year(input_value: str):
    if int(input_value) % 400 == 0 and int(input_value) % 100 == 0:
        return "Y"
    elif int(input_value) % 4 == 0 and int(input_value) % 100 != 0:
        return "Y"
    else:
        return "N"
