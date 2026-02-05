def calculator():
    num_1 = float(input("Введіть перше число: "))
    num_2 = float(input("Введіть друге число: "))
    op = input("Введіть операцію (+, -, *, /): ")

    if op == '+':
        return num_1 + num_2
    elif op == '-':
        return num_1 - num_2
    elif op == '*':
        return num_1 * num_2
    elif op == '/':
        if num_2 != 0:
            return num_1 / num_2
        else:
            print("Ділення на нуль неможливе!")
            return None
    else:
        print("Невідома операція!")
        return None

while True:
    result = calculator()
    if result is not None:
        print("Результат:", result)

    cont = input("Бажаєте ще обчислити? (y/yes для продовження): ").lower()
    if cont != 'y' and cont != 'yes':
        print("Калькулятор завершив роботу.")
        break
