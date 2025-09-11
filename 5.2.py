while True:
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
            result = "Помилка: ділення на нуль"
        else:
            result = number_1 / number_2
    else:
        result = "Невідома операція"

    print("Результат:", result)

    continue_calc = input("Бажаєте продовжити? (y/yes для так, будь-що інше — ні): ").lower()
    if continue_calc != "y" and continue_calc != "yes":
        print("Роботу завершено.")
        break
