def subexpression_printer(expression):
    stack = []
    for index, char in enumerate(expression):
        if char == '(':
            stack.append(index)
        elif char == ')':
            end_index = index
            start_index = stack.pop()
            print(expression[start_index:end_index + 1])


subexpression_printer(input())