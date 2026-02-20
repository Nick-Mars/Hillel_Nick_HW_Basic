def difference(*args):
    if not args:
        return 0
    diff = max(args) - min(args)
    return round(diff, 2)

assert difference(1, 2, 3) == 2, 'Test_1'
assert difference(5, -5) == 10, 'Test_2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test_3'
assert difference() == 0, 'Test_4'
print('OK')