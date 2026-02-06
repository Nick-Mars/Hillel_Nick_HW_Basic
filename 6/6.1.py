import string

letters = string.ascii_lowercase + string.ascii_uppercase

user_input = input("Введіть дві букви через дефіс (наприклад a-c): ")

start, end = user_input.split('-')

print(letters[letters.index(start):letters.index(end)+1])

