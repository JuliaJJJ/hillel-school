from typing import Callable, Generator

def pow(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func: Callable[[int], int]) -> Generator[int, None, None]:
    """
    А generator function that produces values of a sequence

    begin: the first element of the sequence
    end: the number of elements in the sequence
    func: a function that generates values for the sequence
    """
    current = begin
    count = 0
    while count < end:
        yield current
        current = func(current)
        count +=1

from inspect import isgenerator

gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
