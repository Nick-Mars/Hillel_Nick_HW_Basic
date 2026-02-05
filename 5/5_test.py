while True:
    num_1 = float(input("Введіть перше число:"))
    num_2 = float(input("Введіть перше число:"))

    operation = input("Введіть операцію (+, -, *, /):")

    if operation == '+':
        result = num_1 + num_2
    elif operation == '-':
        result = num_1 - num_2
    elif operation == '*':
        result = num_1 * num_2
    elif operation == '/':
        if num_2 != 0:
            result = num_1 / num_2
        else:
            print("Ділення на нуль неможливе!")
            continue
    else:
        print("Невідома операція!")
        continue

    print("Результат:", result)
