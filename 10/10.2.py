import re

def first_word(text):
    match = re.search(r"[A-Za-z']+", text)
    if match:
        return match.group(0)
    return ""
assert first_word("Hello world") == "Hello", 'Test_1'
assert first_word("greetings, friends") == "greetings", 'Test_2'
assert first_word("don't touch it") == "don't", 'Test_3'
assert first_word(".., and so on ...") == "and", 'Test_4'
assert first_word("hi") == "hi", 'Test_5'
assert first_word("Hello.World") == "Hello", 'Test_6'
print('OK')