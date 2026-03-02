def is_even(number):
    return (number & 1) == 0
assert is_even(2494563894038**2) == True, 'Test_1'
assert is_even(1056897**2) == False, 'Test_2'
assert is_even(24945638940387**3) == False, 'Test_3'

print('OK')