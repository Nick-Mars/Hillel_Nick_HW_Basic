lst = [0, 1, 0, 12, 3]

non_zero = []

zero_count = 0

for num in lst:
    if num != 0:
        non_zero.append(num)
    else:
        zero_count += 1

lst = non_zero + [0] * zero_count

print(lst)

