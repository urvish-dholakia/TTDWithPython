from src.stack_python.stack_via_function import stack_program_push


def test_stack_python():
    assert stack_program_push("1") == "1"
    assert stack_program_push("2,3,4") == "2,3,4"
