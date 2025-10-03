from typing import Generator
from inspect import isgenerator

def prime_generator(end: int) -> Generator[int, None, None]:
    """
    A generator of prime numbers from 2 up to the specified value.

    :param end: The upper bound of the range up to which prime numbers are generated
    :return Generator: A generator that yields prime numbers one by one.

    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for num in range(2, end + 1):
        if is_prime(num):
            yield num

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')