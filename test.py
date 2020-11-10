from main import *


def test_is_multiple_of():
    assert is_multiple_of(1, 1) is True
    assert is_multiple_of(1, 3) is False
    assert is_multiple_of(15, 5) is True
    assert is_multiple_of(15, 3) is True


def test_get_message():
    assert get_message(3, True, False) == "Three"
    assert get_message(5, False, True) == "Five"
    assert get_message(15, True, True) == "ThreeFive"
    assert get_message(1, False, False) == "1"
