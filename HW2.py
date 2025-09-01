number = int(input("Введіть число: "))
a = (number // 10000) % 10
b = (number // 1000) % 10
c = (number // 100) % 10
d = (number //10) % 10
e = number % 10
reversed_number = e*10000 + d*1000 + c*100 + b*10 + a
print(reversed_number)

