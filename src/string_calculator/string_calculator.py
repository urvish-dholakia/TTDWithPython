import re


def add(input_value: str):
    if input_value == "":
        input_value = str(0)
    predefined_seperators = [',', ';', ':', '|', '\n', '/']
    bracket_seperators = re.findall(r'\[(.*?)\]', str(input_value))
    joined_all_seperators = set(''.join(bracket_seperators) + ''.join(predefined_seperators))
    print(joined_all_seperators)
    cleaned_text = re.sub(r'\[.*?\]', '', input_value)
    separator_pattern = '|'.join(map(re.escape, joined_all_seperators))
    parts = [part.strip() for part in re.split(separator_pattern, cleaned_text) if part.strip()]
    comma_separated = ','.join(parts)
    str_to_list = comma_separated.split(',')
    print(str_to_list)
    sum = 0
    for iterator in str_to_list:
        if 0 < int(iterator) < 1000:
            sum = sum + int(iterator)
    return int(sum)
