def is_even(digit):
    return digit % 2 == 0

assert is_even(2) == True, 'Test_1'
assert is_even(5) == False, 'Test_2'
assert is_even(0) == True, 'Test_3'
print('OK')