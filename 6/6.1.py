number = input()

while len(number) > 1:
    result = 1

    for digit in number:
        result *= int(digit)

    number = str(result)

print(number)
