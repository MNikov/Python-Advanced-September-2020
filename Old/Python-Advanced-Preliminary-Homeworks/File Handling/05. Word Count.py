import re

text_path = './08-File-Handling-Lab-Resources/Words Count/text.txt'
searched_words_path = './08-File-Handling-Lab-Resources/Words Count/words.txt'
text_file = open(text_path, 'r')
searched_words_file = open(searched_words_path, 'r')

searched_words_dict = {word: 0 for word in searched_words_file.read().split()}

for word in text_file:
    words = re.findall(r'[A-Za-z0-9]+', word.lower())
    for filtered_word in words:
        if filtered_word in searched_words_dict:
            searched_words_dict[filtered_word] += 1

searched_words_dict = dict(sorted(searched_words_dict.items(), key=lambda x: x[1], reverse=True))
[print(f'{word} - {count}') for word, count in searched_words_dict.items()]
