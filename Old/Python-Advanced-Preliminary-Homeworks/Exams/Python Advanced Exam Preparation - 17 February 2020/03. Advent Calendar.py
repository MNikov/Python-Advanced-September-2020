def fix_calendar(numbers):
    numbers = [int(x) for x in numbers]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


numbers = [3, 2, 1]
fixed = fix_calendar(numbers)
print(fixed)


# data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
# new_list = []
#
# while data_list:
#     minimum = data_list[0]  # arbitrary number in list
#     for x in data_list:
#         if x < minimum:
#             minimum = x
#     new_list.append(minimum)
#     data_list.remove(minimum)
#
# print(new_list)