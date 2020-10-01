def round_nums(nums):
    return [round(x) for x in nums]


nums = [float(x) for x in input().split()]
print(round_nums(nums))

# print(list(round(float(x)) for x in input().split()))
