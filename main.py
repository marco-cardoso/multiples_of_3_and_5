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


def get_message(number: int, multiple_of_three : bool, multiple_of_five : bool) -> str:
    """
    Get the message for the given number

    Possible results :
    For multiples of three return “Three”
    For multiples of five return “Five”
    For numbers which are multiples of both three and five return “ThreeFive”
    For none of the cases above return the number itself


    :param number: An integer with the number to analyse
    :param multiple_of_five: A boolean with whether the result is multiple of five or not
    :param multiple_of_three: A boolean with whether the result is multiple of three or not
    :return: The message with one of the above results
    """

    result_message = None
    if multiple_of_three and multiple_of_five:
        result_message = "ThreeFive"
    elif multiple_of_three:
        result_message = "Three"
    elif multiple_of_five:
        result_message = "Five"
    else:
        result_message = str(number)

    return result_message


def main():
    for number in range(1, 101):
        is_multiple_of_three = is_multiple_of(number, 3)
        is_multiple_of_five = is_multiple_of(number, 5)
        message = get_message(number, is_multiple_of_three, is_multiple_of_five)
        show_result(message)


if __name__ == "__main__":
    main()
