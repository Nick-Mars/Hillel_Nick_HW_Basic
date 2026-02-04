lst = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]

if len(lst) == 0:
    result = [[], []]
else:
    mid = (len(lst) + 1) // 2
    result = [lst[:mid], lst[mid:]]

print(result)
