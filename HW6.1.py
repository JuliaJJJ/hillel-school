import string

value = input('Please enter value: ')
value_list = value.split('-')

string_list = string.ascii_letters

indexA = string_list.index(value_list[0])
indexB = string_list.index(value_list[1]) + 1

final = ''.join(string_list[indexA:indexB])

print(final)
