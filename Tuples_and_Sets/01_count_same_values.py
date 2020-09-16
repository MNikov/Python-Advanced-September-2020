def count_num_occurrences(nums):
    num_dict = {n: 0 for n in nums}
    for n in nums:
        num_dict[n] += 1
    [print(f'{float(n)} - {t} times') for n, t in num_dict.items()]


count_num_occurrences(input().split())
