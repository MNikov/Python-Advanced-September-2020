def split_sums(number):
    odd_set = set()
    even_set = set()
    for i in range(1, number + 1):
        name = input()
        name_sum = 0
        name_sum = sum([ord(c) for c in name]) // i
        if name_sum % 2 == 0:
            even_set.add(name_sum)
        else:
            odd_set.add(name_sum)
    return odd_set, even_set


def print_result(odd_set, even_set):
    if sum(odd_set) == sum(even_set):
        to_print = odd_set.union(even_set)
    if sum(odd_set) > sum(even_set):
        to_print = odd_set.difference(even_set)
    else:
        to_print = odd_set.symmetric_difference(even_set)
    print(', '.join([str(x) for x in to_print]))


odd_set, even_set = split_sums(int(input()))
print_result(odd_set, even_set)