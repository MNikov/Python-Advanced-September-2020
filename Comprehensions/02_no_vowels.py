def remove_vowels(text):
    fixed_text = [c for c in text if c not in ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']]
    return ''.join(fixed_text)


print(remove_vowels(input()))
