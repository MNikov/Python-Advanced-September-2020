def odd_even_equation(numbers, command):
    if command == 'Odd':
        print(sum([x for x in numbers if x % 2 != 0]) * len(numbers))
    else:
        print(sum([x for x in numbers if x % 2 == 0]) * len(numbers))


command = input()
nums = [int(x) for x in input().split()]
odd_even_equation(nums, command)