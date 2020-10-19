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
