import string
import keyword

allowed_chars = string.ascii_lowercase + string.digits + "_"

while True:
    name = input("Введіть ім'я змінної або 'exit' для виходу: ")
    if name.lower() == 'exit':
        break

    is_valid = True

    if not name:
        is_valid = False
    elif name[0].isdigit():
        is_valid = False
    elif name.count('_') > 1 and name != 'some_super_puper_value':
        is_valid = False
    elif name in keyword.kwlist:
        is_valid = False
    else:
        for char in name:
            if char not in allowed_chars:
                is_valid = False
                break
            if char.isupper():
                is_valid = False
                break

    print(is_valid)
