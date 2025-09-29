def is_even(digit: int) -> bool:
    """
    Check if a number is even.

    :param digit: Integer to check.
    :return: True if the number is even, False otherwise.
    """
    return digit % 2 == 0


assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')
