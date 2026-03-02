from inspect import isgenerator

def generate_cube_numbers(end):

    n = 2
    while True:
        cube = n ** 3
        if cube > end:
            return
        yield cube
        n += 1

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test_0'
assert list(generate_cube_numbers(10)) == [8], 'Test1: оскільки 2^3 = 8 < 10'
assert list(generate_cube_numbers(100)) == [8, 27, 64], 'Test_2: 5^3 = 125 > 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], 'Test_3: 10^3 = 1000'
print('OK')