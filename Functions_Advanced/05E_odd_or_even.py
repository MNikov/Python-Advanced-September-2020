command = input()
nums = [int(x) for x in input().split()]

if command == 'Odd':
    odd_sum = sum(filter(lambda x: x % 2 != 0, nums))
    print(odd_sum * len(nums))
else:
    even_sum = sum(filter(lambda x: x % 2 == 0, nums))
    print(even_sum * len(nums))
