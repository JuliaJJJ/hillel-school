import string
import keyword

punctuation = string.punctuation.replace('_', '')
keywords = keyword.kwlist

value = input('Add value: ')
lst = list(value)
under_line_list = [item for item in lst if item == "_"]
is_valid_result = True

if value[0].isdigit() or value != value.lower():
    is_valid_result = False
elif value in keywords:
    is_valid_result = False
elif any(ch in punctuation or ch == " " for ch in lst):
    is_valid_result = False
elif len(under_line_list) == len(value) and len(under_line_list) != 1:
    is_valid_result = False

print(is_valid_result)
