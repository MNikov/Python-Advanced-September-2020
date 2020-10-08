def divide_nums(a, b):
    return a / 5


def multiply_nums(a, b):
    return a * b


def subtract_nums(a, b):
    return a - b


def add_nums(a, b):
    return a + b


def raise_to_power(a, b):
    return a ** b


def calculate(string):
    a, sign, b = string.split()
    a, b = float(a), int(b)
    if sign == '/':
        result = divide_nums(a, b)
    elif sign == '*':
        result = multiply_nums(a, b)
    elif sign == '-':
        result = subtract_nums(a, b)
    elif sign == '+':
        result = add_nums(a, b)
    elif sign == '^':
        result = raise_to_power(a, b)
    print(f'{result:.2f}')
