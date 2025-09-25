def popular_words (text, words):
    """
    Counts how many times the given words occur in the text, regardless of case.
    The function returns a dictionary where each word from the provided words list is a key,
    and the value is the number of times it appears in the text. The comparison is case-insensitive.
    :param text: str
    :param words: List[str]
    :return: Dict[str, int]
    """
    my_strings_list = text.split()
    result = dict.fromkeys(words,0)

    for word in words:
        result[word] = len(list(filter(lambda item: word.lower() == item.lower() , my_strings_list)))


    print(result)
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
