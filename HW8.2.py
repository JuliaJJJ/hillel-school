import string

def is_palindrome(text):
    special_chars = string.punctuation + " "
    new_text = ''.join([char for char in text if char not in special_chars]).lower()

    return new_text == new_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
