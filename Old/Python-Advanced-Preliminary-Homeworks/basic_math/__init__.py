def calculate(string):
    a, operator, b = string.split()
    a, b = float(a), float(b)
    result = ''

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b
    elif operator == '^':
        result = a ** b

    print(f'{result:.2f}')
