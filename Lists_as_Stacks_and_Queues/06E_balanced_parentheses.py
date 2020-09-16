def check_balanced_parentheses(expression):
    stack = []
    is_valid = True
    opening_parentheses = ['(', '[', '{']
    closing_parentheses = [')', ']', '}']
    for char in expression:
        if char in opening_parentheses:
            stack.append(char)
        elif char in closing_parentheses:
            if len(stack) == 0:
                is_valid = False
            else:
                last = stack.pop()
                if last == '(' and char == ')':
                    continue
                elif last == '[' and char == ']':
                    continue
                elif last == '{' and char == '}':
                    continue
                else:
                    is_valid = False
                    break

    if is_valid:
        print('YES')
    else:
        print('NO')


check_balanced_parentheses(input())
