def operate(operator, *nums):
    result = nums[0]
    if operator == '+':
        for n in nums[1:]:
            result += n
    elif operator == '-':
        for n in nums[1:]:
            result -= n
    elif operator == '*':
        for n in nums[1:]:
            result *= n
    elif operator == '/':
        for n in nums[1:]:
            result /= n
    return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 20, 4))
print(operate("-", 54, 43))
