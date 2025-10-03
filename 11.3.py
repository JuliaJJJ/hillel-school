def is_even(number: int) -> bool:
    """
    Determines whether a given integer is even, using bitwise operations.

    :param int: The integer to check.
    :return bool: True if the number is even, False otherwise.
    """
    return (number & 1) == 0

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'