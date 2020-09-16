def reverse_numbers(numbers):
    reversed_numbers = []
    while numbers:
        reversed_numbers.append(numbers.pop())
    print(' '.join(reversed_numbers))


reverse_numbers(input().split())