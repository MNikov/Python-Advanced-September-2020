chars_to_remove = ["-", ",", ".", "!", "?"]

with open('text.txt') as text_file:
    for i, line in enumerate(text_file):
        if i % 2 == 0:
            for char in line:
                if char in chars_to_remove:
                    line = line.replace(char, '@')
            print(' '.join(reversed(line.split())))
