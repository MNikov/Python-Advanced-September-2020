def fact(n):
    if n == 1:
        return 1
    print(n * (n - 1))
    print('---')
    return n * fact(n - 1)


print(fact(5))
