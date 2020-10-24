def filter_divisible_numbers(start, end):
    filtered_list = {n for n in range(start, end + 1) for d in range(2, 10) if n % d == 0}
    return list(filtered_list)


print(filter_divisible_numbers(int(input()), int(input())))
