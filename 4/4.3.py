import random

lst = [random.randint(0, 20) for _ in range(random.randint(3, 10))]

new_lst = [lst[0], lst[2], lst[-2]]

print("Original list:", lst)
print("Final list:", new_lst)
