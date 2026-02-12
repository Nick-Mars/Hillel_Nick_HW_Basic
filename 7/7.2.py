def correct_sentence(text):
    text = text[0].upper() + text[1:] if text else ''
    if not text.endswith('.'):
        text += '.'
    return text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test_1'
assert correct_sentence("hello") == "Hello.", 'Test_2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test_3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test_4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test_5'
print('ОК')
