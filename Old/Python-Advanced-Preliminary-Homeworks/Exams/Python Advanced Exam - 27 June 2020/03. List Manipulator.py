def list_manipulator(numbers, *args):
    if args[0] == "add":
        if args[1] == "beginning":
            numbers = [i for i in args[2:]] + numbers
        elif args[1] == "end":
            numbers = numbers + [i for i in args[2:]]

    elif args[0] == "remove" and len(args) == 3:
        if args[1] == "end":
            numbers = numbers[:-args[2]]
        elif args[1] == "beginning":
            numbers = numbers[args[2]:]

    elif args[0] == "remove" and len(args) == 2:
        if args[1] == "end":
            numbers = numbers[:-1]
        elif args[1] == "beginning":
            numbers = numbers[1:]

    return numbers


# -- 83/100 --
# def list_manipulator(numbers, *args):
#     parameter_1, parameter_2 = args[0], args[1]
#     nums_to_manipulate = [int(x) for x in args[2:]]
#     to_return = []
#     n = len(nums_to_manipulate)
#     if parameter_1 == 'add' and parameter_2 == 'beginning':
#         to_return = nums_to_manipulate + numbers
#     elif parameter_1 == 'add' and parameter_2 == 'end':
#         to_return = numbers + nums_to_manipulate
#     elif parameter_1 == 'remove' and parameter_2 == 'beginning':
#         if n > 0:
#             to_return = numbers[n + 1:]
#         else:
#             to_return = numbers[1:]
#     elif parameter_1 == 'remove' and parameter_2 == 'end':
#         if n > 0:
#             to_return = numbers[:n]
#         else:
#             to_return = numbers[:-1]
#     return to_return
print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
