def is_palindrome(text):
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test_1'
assert is_palindrome('0P') == False, 'Test_2'
assert is_palindrome('a.') == True, 'Test_3'
assert is_palindrome('aurora') == False, 'Test_4'
print('ОК')
