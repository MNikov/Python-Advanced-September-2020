def count_chars(text):
    chars = {}
    for char in text:
        if char not in chars:
            chars[char] = 0
        chars[char] += 1
    return chars


def print_chars(char_dict):
    for char, count in sorted(char_dict.items()):
        print(f'{char}: {count} time/s')


print_chars(count_chars(input()))