def get_string_lengths(strings):
    return {s: len(s) for s in strings}


print(', '.join(f'{k} -> {v}' for k, v in get_string_lengths(input().split(', ')).items()))
