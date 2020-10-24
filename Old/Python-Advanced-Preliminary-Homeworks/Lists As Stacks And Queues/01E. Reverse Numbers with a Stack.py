def stack_reverse(number_list):
    stack = []
    for number in number_list:
        stack.append(number)
    while stack:
        print(stack.pop(), end=' ')


stack_reverse(input().split())