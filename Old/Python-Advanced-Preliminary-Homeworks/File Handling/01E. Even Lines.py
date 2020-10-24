chars_to_remove = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as text_file:
    for i, line in enumerate(text_file):
        if i % 2 == 0:
            for char in line:
                if char in chars_to_remove:
                    line = line.replace(char, '@')
            line = line.split()
            print(' '.join(reversed(line)))
