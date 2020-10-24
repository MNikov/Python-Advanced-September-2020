def classify_nums():
    nums = [int(x) for x in input().split(', ')]
    pos = [x for x in nums if x >= 0]
    print(f'Positive: {", ".join([str(x) for x in pos])}')

    neg = [x for x in nums if x < 0]
    print(f"Negative: {', '.join([str(x) for x in neg])}")

    even = [x for x in nums if x % 2 == 0]
    print(f"Even: {', '.join([str(x) for x in even])}")

    odd = [x for x in nums if x % 2 != 0]
    print(f"Odd: {', '.join([str(x) for x in odd])}")


classify_nums()
