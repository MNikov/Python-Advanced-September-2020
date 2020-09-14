def get_sub_expressions(expression):
    sub_expressions = []
    for char in expression:
        if char == '(':
            sub_expressions.append('')

        for i in range(len(sub_expressions)):
            sub_expressions[i] += char

        if char == ')':
            sub_expression = sub_expressions.pop()
            print(sub_expression)


get_sub_expressions(input())
