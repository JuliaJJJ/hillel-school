def difference(*numbers):
    """
    Calculates the difference between the maximum and minimum numbers in the passed arguments.
    If no arguments are passed, returns 0. The result is rounded to two decimal places.

    :param numbers:
    :return: number
    """

    if len(numbers) == 0:
        return 0

    return round(max(numbers) - min(numbers), 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
