number_1 = float(input("Введіть число: "))
user = input("Введіть математичний символ (+, -, *, /): ")
number_2 = float(input("Введіть число: "))

if user == "+":
    result = number_1 + number_2
elif user == "-":
    result = number_1 - number_2
elif user == "*":
    result = number_1 * number_2
elif user == "/":
    if number_2 == 0:
        result = "Помилка ділення на 0"
    else:
        result = number_1 / number_2

print(result)
