def add(input_value:str):
    if input_value == "":
        input_value = str(0)
    str_to_list = input_value.split(",")
    sum = 0
    for iterator in str_to_list:
        sum = sum + int(iterator)
    return int(sum)
