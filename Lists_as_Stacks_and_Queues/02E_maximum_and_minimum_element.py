def max_min(n):
    stack = []
    for _ in range(n):
        tokens = input().split()
        query = tokens[0]
        if query == '1':
            el = int(tokens[1])
            stack.append(el)
        elif query == '2':
            if stack:
                stack.pop()
        elif query == '3':
            if stack:
                print(max(stack))
        else:
            if stack:
                print(min(stack))
    print(', '.join([str(x) for x in stack[::-1]]))


max_min(int(input()))
