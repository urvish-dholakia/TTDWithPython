import re


def add(input_value: str):
    if input_value == "":
        input_value = str(0)
    str_del = re.findall(r'\[(.*?)\]', str(input_value))
    print(str_del)
    str_to_list = re.split("str_del|,|\n|;", input_value)
    sum = 0
    for iterator in str_to_list:
        if 0 < int(iterator) < 1000:
            sum = sum + int(iterator)
    return int(sum)
