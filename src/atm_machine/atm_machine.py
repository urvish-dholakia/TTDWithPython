from _ast import Add


def main():
    # Get input from the user
    user_input = input("Enter a list of numbers separated by commas: ")

    try:
        # Call the Add function with the user's input
        result = Add(user_input)
        print(f"The sum is: {result}")
    except ValueError as e:
        # Handle the ValueError by printing the exception message
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
