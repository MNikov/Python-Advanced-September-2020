def operate(operator, *args):
    if operator in ['+', '-']:
        result = 0
    else:
        result = 1
    for num in args:
        if operator == '+':
            result += num
        elif operator == '-':
            result -= num
        elif operator == '*':
            result *= num
        else:
            result /= num
    return result
