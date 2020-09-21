def count_symbols(string):
    occurrences = {}
    for char in string:
        if char not in occurrences:
            occurrences[char] = 0
        occurrences[char] += 1
    return occurrences


def print_result(collection: dict):
    for k, v in sorted(collection.items()):
        print(f'{k}: {v} time/s')


char_occurrences = count_symbols(input())
print_result(char_occurrences)
