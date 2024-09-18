import re


def add(input_value: str):
    if input_value == "":
        input_value = str(0)
    comma_separated = process_seperators(input_value)
    int_str_to_list = str_list_to_int_list(comma_separated)
    negatives = [num for num in int_str_to_list if num < 0]
    check_negatives(negatives)
    return sum_values(int_str_to_list)


def sum_values(int_str_to_list):
    sum = 0
    for iterator in int_str_to_list:
        if 0 < iterator < 1000:
            sum = sum + iterator
    return sum


def process_seperators(input_value):
    predefined_seperators = [',', ';', ':', '|', '\n', '/']
    bracket_seperators = re.findall(r'\[(.*?)\]', str(input_value))
    joined_all_seperators = set(''.join(bracket_seperators) + ''.join(predefined_seperators))
    cleaned_text = re.sub(r'\[.*?\]', '', input_value)
    separator_pattern = '|'.join(map(re.escape, joined_all_seperators))
    parts = [part.strip() for part in re.split(separator_pattern, cleaned_text) if part.strip()]
    comma_separated = ','.join(parts)
    return comma_separated


def str_list_to_int_list(comma_separated):
    str_to_list = comma_separated.split(',')
    int_str_to_list = list(map(int, str_to_list))
    return int_str_to_list


def check_negatives(negatives):
    if negatives:
        raise ValueError(f"Negatives not allowed: {' '.join(map(str, negatives))}")
