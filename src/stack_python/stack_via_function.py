class StackOverflowError(Exception):
    """Exception raised when stack overflow occurs."""
    pass


class StackUnderflowError(Exception):
    """Exception raised when stack underflow occurs."""
    pass


MAX_STACK_SIZE = 100  # Maximum size of the stack


def stack_program_push(input_value: str):
    if not hasattr(stack_program_push, 'stack'):
        stack_program_push.stack = []

    values = [v.strip() for v in input_value.split(',') if v.strip()]

    if values:
        for value in values:
            if len(stack_program_push.stack) >= MAX_STACK_SIZE:
                raise StackOverflowError("Cannot push to a full stack")
            stack_program_push.stack.append(value)
    else:
        if len(stack_program_push.stack) >= MAX_STACK_SIZE:
            raise StackOverflowError("Cannot push to a full stack")
        stack_program_push.stack.append(input_value)

    return ','.join(stack_program_push.stack)


def stack_program_pop():
    if not hasattr(stack_program_push, 'stack') or len(stack_program_push.stack) == 0:
        raise StackUnderflowError("Cannot pop from an empty stack")
    return stack_program_push.stack.pop()
