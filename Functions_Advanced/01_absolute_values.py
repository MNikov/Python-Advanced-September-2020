def get_abs_values_of_nums(nums):
    return [abs(n) for n in nums]


nums = [float(x) for x in input().split()]
print(get_abs_values_of_nums(nums))

# print(list(abs(float(x)) for x in input().split()))
