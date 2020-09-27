def classify_numbers(numbers):
    pos = [n for n in numbers if n >= 0]
    neg = [n for n in numbers if n < 0]
    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]
    return pos, neg, even, odd


pos, neg, even, odd = classify_numbers([int(x) for x in input().split(', ')])
print(f'Positive: {", ".join([str(x) for x in pos])}')
print(f'Negative: {", ".join([str(x) for x in neg])}')
print(f'Even: {", ".join([str(x) for x in even])}')
print(f'Odd: {", ".join([str(x) for x in odd])}')
