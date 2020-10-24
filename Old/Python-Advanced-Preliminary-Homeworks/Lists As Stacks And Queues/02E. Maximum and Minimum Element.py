def solution(number):
    stack = []
    for _ in range(number):
        line = input().split()
        command_type = int(line[0])
        if command_type == 1:
            num = int(line[1])
            stack.append(num)
        elif command_type == 2:
            if len(stack) > 0:
                stack.pop()
        elif command_type == 3:
            if len(stack) > 0:
                print(max(stack))
        elif command_type == 4:
            if len(stack) > 0:
                print(min(stack))

    print(', '.join(reversed([str(n) for n in stack])))


solution(int(input()))
