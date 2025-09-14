value = input('ввести число: ')
n = int(value)

while n >= 10:
    i = 1
    while n > 0:
        last_number = n % 10
        i *= last_number
        n //= 10
    n = i

print(n)
