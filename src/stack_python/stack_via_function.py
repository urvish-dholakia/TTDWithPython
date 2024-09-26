def stack_program_push(input_value: str):
    stack = []
    values = [v.strip() for v in input_value.split(',')]
    if len([v for v in values if v]) < 1:
        stack.append(input_value)
        return stack[-1]
    else:
        input_value_list = input_value.split(",")
        stack.append(input_value_list)
        return stack[-1]
