def filter_divisible_numbers(start, end):
    filtered_list = {n for n in range(start, end + 1) for d in range(2, 11) if n % d == 0}
    return list(filtered_list)


print(filter_divisible_numbers(int(input()), int(input())))

# print([n for n in range(int(input()), int(input()) + 1) if any([n % m == 0 for m in range(2, 11)])])
