def flatten_list(nums):
    return ' '.join([y for x in nums.split('|')[::-1] for y in x.split()])


nums = input()
print(flatten_list(nums))
