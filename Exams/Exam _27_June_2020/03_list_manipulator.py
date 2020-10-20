from collections import deque


def list_manipulator(numbers, command, side, *args):
    new_list = deque(numbers)
    if command == 'add':
        new_nums = list(args)
        if side == 'beginning':
            new_list = new_nums + numbers
        elif side == 'end':
            new_list = numbers + new_nums

    elif command == 'remove':
        if side == 'beginning':
            if len(args) >= 1:
                n = args[0]
                while n > 0:
                    new_list.popleft()
                    n -= 1
            else:
                new_list.popleft()
        elif side == 'end':
            if len(args) >= 1:
                n = args[0]
                while n > 0:
                    new_list.pop()
                    n -= 1
            else:
                new_list.pop()
    return list(new_list)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
