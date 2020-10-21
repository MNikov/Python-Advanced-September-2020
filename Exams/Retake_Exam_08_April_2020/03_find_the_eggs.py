def find_strongest_eggs(*args):
    eggs, n = args
    sub_lists = [[] for _ in range(n)]
    idx = 0
    for egg in eggs:  # distribute in sublists
        if idx == n:
            idx = 0
        sub_lists[idx].append(egg)
        idx += 1

    strongest_eggs = []
    for sl in sub_lists:
        mid_egg = sl[len(sl) // 2]
        left_egg = sl[(len(sl) // 2) - 1]
        right_egg = sl[(len(sl) // 2) + 1]
        condition_1 = left_egg < mid_egg > right_egg
        condition_2 = right_egg > left_egg
        if condition_1 and condition_2:
            strongest_eggs.append(mid_egg)

    return strongest_eggs


# # ПРИМЕРЕН КОД ОТ ЛЕКЦИЯТА НА ТАНЯ СТАНЕВА
# def find_strongest_eggs(eggs, sub_list_count):
#     best_eggs = []
#
#     for i in range(sub_list_count):
#         current = [eggs[idx] for idx in range(i, len(eggs), sub_list_count)]
#         mid_element = current[len(current) // 2]
#         left_element = current[len(current) // 2 - 1]
#         right_element = current[len(current) // 2 + 1]
#         if left_element < mid_element > right_element > left_element:
#             best_eggs.append(mid_element)
#
#     return best_eggs

test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))
test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))
test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
