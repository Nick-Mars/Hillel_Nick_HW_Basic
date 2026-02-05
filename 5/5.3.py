import string

text = input()

for symbol in string.punctuation:
    text = text.replace(symbol, '')

words = text.split()

hashtag = '#'

for word in words:
    hashtag += word.capitalize()

hashtag = hashtag[:140]

print(hashtag)