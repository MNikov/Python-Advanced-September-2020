def get_repeating_DNA(sequence):
    subsequences = []
    for i in range(len(sequence) - 10):
        current_subsequence = sequence[i: i + 10]
        chopped_sequence = sequence[i + 1:]
        if current_subsequence not in subsequences and current_subsequence in chopped_sequence:
            subsequences.append(current_subsequence)
    return subsequences


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
