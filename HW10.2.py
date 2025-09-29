import string
from functools import reduce


def first_word(text: str) -> str:
    """ Search for the first word

    :param text: Input string.
    :return: The first word in the string.
    """
    punctuation = list(string.punctuation.replace("'", '',))

    text_with_spaces = reduce(lambda acc, current: acc.replace(current, ' '), punctuation, text)

    return text_with_spaces.split()[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')