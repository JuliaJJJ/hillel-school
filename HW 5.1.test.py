import string
import keyword

punctuation = string.punctuation.replace('_', '')
keywords = keyword.kwlist

def check_rule(value):
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

    return is_valid_result

assert check_rule('_') == True, 'Test1'
assert check_rule('__') == False, 'Test2'
assert check_rule('___') == False, 'Test3'
assert check_rule('x') == True, 'Test4'
assert check_rule('get_value') == True, 'Test5'
assert check_rule('get value') == False, 'Test6'
assert check_rule('get!value') == False, 'Test7'
assert check_rule('some_super_puper_value') == True, 'Test8'
assert check_rule('Get_value') == False, 'Test9'
assert check_rule('get_Value') == False, 'Test10'
assert check_rule('getValue') == False, 'Test11'
assert check_rule('3m') == False, 'Test12'
assert check_rule('m3') == True, 'Test13'
assert check_rule('assert') == False, 'Test14'
assert check_rule('assert_exception') == True, 'Test15'
print('ok')
