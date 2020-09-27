def get_words_with_even_len(words):
    return [w for w in words if len(w) % 2 == 0]


print('\n'.join(get_words_with_even_len(input().split())))
