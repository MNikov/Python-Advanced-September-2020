def numbers_searching(*args):
    nums = args
    duplicates = []
    missing_num = ''
    sorted_nums = sorted(list((set(nums))))
    for i, num in enumerate(sorted_nums):
        if num - sorted_nums[i - 1] > 1 and min(nums) <= num - 1 <= max(nums):
            missing_num = num - 1
            break

    for num in set(nums):
        if nums.count(num) > 1 and min(nums) <= num <= max(nums):
            duplicates.append(num)
    return [missing_num, sorted(duplicates)]


# def numbers_searching(*args):
#     duplicates = set()
#     missing_number = 0
#     nums = [int(x) for x in args]
#     for num in range(min(nums), max(nums) + 1):
#         if num not in nums:
#             missing_number = num
#         if nums.count(num) > 1:
#             duplicates.add(num)
#     return [missing_number, list(sorted(duplicates))]

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
