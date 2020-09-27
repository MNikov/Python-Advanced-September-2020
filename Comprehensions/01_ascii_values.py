def get_ascii_values(chars_as_string):
    return {char: ord(char) for char in chars_as_string.split(', ')}


print(get_ascii_values(input()))
