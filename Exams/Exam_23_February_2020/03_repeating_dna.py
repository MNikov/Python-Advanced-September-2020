def get_repeating_DNA(sequence):
    all_sequences = []
    for i in range(len(sequence) - 9):
        current_sequence = sequence[i:i + 10]
        all_sequences.append(current_sequence)
    result = []
    for s in all_sequences:
        if s not in result and all_sequences.count(s) >= 2:
            result.append(s)
    return result


# def get_repeating_DNA(sequence):
#     subsequences = []
#     for i in range(len(sequence) - 10):
#         current_subsequence = sequence[i: i + 10]
#         chopped_sequence = sequence[i + 1:]
#         if current_subsequence not in subsequences and current_subsequence in chopped_sequence:
#             subsequences.append(current_subsequence)
#     return subsequences
test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)
test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)
test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
