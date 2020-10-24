def find_even_len_words():
    return [x for x in input().split() if len(x) % 2 == 0]


word_list = find_even_len_words()
[print(x) for x in word_list]