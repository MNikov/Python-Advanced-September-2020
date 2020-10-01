def print_combinations(text, idx):
    if idx >= len(text):
        print("".join(text))
        return
    print_combinations(text, idx + 1)
    for i in range(idx + 1, len(text)):
        text[idx], text[i] = text[i], text[idx]
        print_combinations(text, idx + 1)
        text[idx], text[i] = text[i], text[idx]


text = list(input())
print_combinations(text, 0)
