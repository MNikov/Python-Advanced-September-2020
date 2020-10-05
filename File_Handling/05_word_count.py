import re

words_file = open('08-File-Handling-Lab-Resources\\Words Count\\words.txt')
text_file = open('08-File-Handling-Lab-Resources\\Words Count\\text.txt')

word_dict = {w: 0 for w in words_file.read().split()}

for line in text_file:
    words = re.findall(r'[A-Za-z0-9]+', line.lower())
    for word in words:
        if word in word_dict:
            word_dict[word] += 1

with open('output.txt', 'w') as output_file:
    for word, count in sorted(word_dict.items(), key=lambda x: -x[1]):
        output_file.write(f'{word} - {count}\n')

words_file.close()
text_file.close()
