def say_hi(name, age):
    return f"Hi. My name is {name} and I'm {age} years old"

# Тести
assert say_hi("Nick", 32) == "Hi. My name is Nick and I'm 32 years old", 'Test1'
assert say_hi("Robert", 68) == "Hi. My name is Robert and I'm 68 years old", 'Test2'
print('ОК')
