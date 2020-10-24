nums = [int(x) for x in input().split()]
nums = list(filter(lambda x: x % 2 == 0, nums))
print(nums)