def func_executor(*args):
    result = []
    for t in args:
        fn, nums = t
        result.append(fn(*nums))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4)),
    (sum_numbers, (5, 6)),
    (multiply_numbers, (5, 6))
))
