def is_multiple_of(number: int, multiple: int) -> bool:
    """
    Check if the parameter number is multiple of the variable multiple
    :param number: The number to identify if is multiple or not
    :param multiple: The multiple
    :return: A boolean with the result whether the number is multiple or not
    """
    return number % multiple == 0


def show_result(message: str):
    """
    Responsible to present the result message.
    :param message: A string with the message
    """
    print(message)


def get_message(number: int) -> str:
    """
    Get the message for the given number

    Possible results
    For multiples of three return “Three”
    For multiples of five return “Five”
    For numbers which are multiples of both three and five return “ThreeFive”
    For none of the cases above return the number itself

    :param number: An integer with the number to analyse
    :return: The message with one of the above results
    """
    is_multiple_of_three = is_multiple_of(number, 3)
    is_multiple_of_five = is_multiple_of(number, 5)

    result_message = None
    if is_multiple_of_three and is_multiple_of_five:
        result_message = "ThreeFive"
    elif is_multiple_of_three:
        result_message = "Three"
    elif is_multiple_of_five:
        result_message = "Five"
    else:
        result_message = str(number)

    return result_message


def main():
    for number in range(1, 101):
        message = get_message(number)
        show_result(message)


if __name__ == "__main__":
    main()
