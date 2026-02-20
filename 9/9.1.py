def popular_words(text, words):
    text_lower = text.lower()
    text_words = text_lower.split()

    result = {}

    for word in words:
        result[word] = text_words.count(word)

    return result


text = '''When I was One I had just begun When I was Two I was nearly'''
words_to_find = ['one', 'two', 'three']
print(popular_words(text, words_to_find))