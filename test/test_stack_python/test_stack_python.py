import pytest

from src.stack_python.stack_via_function import stack_program_push, stack_program_pop, StackOverflowError, \
    StackUnderflowError, MAX_STACK_SIZE


def test_stack_python_push():
    # Reset the stack before running tests
    if hasattr(stack_program_push, 'stack'):
        del stack_program_push.stack

    assert stack_program_push("1") == "1"
    assert stack_program_push("2,3,4") == "1,2,3,4"
    assert stack_program_push("") == "1,2,3,4,"
    assert stack_program_push("5, 6") == "1,2,3,4,,5,6"


def test_stack_python_pop():
    # Reset the stack before running tests
    if hasattr(stack_program_push, 'stack'):
        del stack_program_push.stack

    stack_program_push("1,2,3")
    assert stack_program_pop() == "3"
    assert stack_program_pop() == "2"
    assert stack_program_pop() == "1"

    with pytest.raises(StackUnderflowError):
        stack_program_pop()


def test_stack_overflow():
    # Reset the stack before running tests
    if hasattr(stack_program_push, 'stack'):
        del stack_program_push.stack

    # Push MAX_STACK_SIZE elements
    for i in range(MAX_STACK_SIZE):
        stack_program_push(str(i))

    # Trying to push one more element should raise StackOverflowError
    with pytest.raises(StackOverflowError):
        stack_program_push("overflow")


def test_stack_underflow():
    # Reset the stack before running tests
    if hasattr(stack_program_push, 'stack'):
        del stack_program_push.stack

    # Trying to pop from an empty stack should raise StackUnderflowError
    with pytest.raises(StackUnderflowError):
        stack_program_pop()
