def print_min_max_sum(numbers):
    print(f'The minimum number is {min(numbers)}')
    print(f'The maximum number is {max(numbers)}')
    print(f'The sum number is: {sum(numbers)}')


nums = [int(x) for x in input().split()]
print_min_max_sum(nums)