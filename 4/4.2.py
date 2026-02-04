lst = [0, 1, 7, 2, 4, 8]

if len(lst) == 0:
    result = 0
else:
    sum_even_index = sum(lst[0::2])
    result = sum_even_index * lst[-1]

print(result)

