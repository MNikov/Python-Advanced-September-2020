from collections import deque


def best_list_pureness(*args):
    nums, rotations = args
    best_value = -99999999
    nums = deque(nums)
    best_rot = 0
    for rotation in range(rotations + 1):
        value = 0
        for i, n in enumerate(nums):
            value += (i * n)
        if value > best_value:
            best_value = value
            best_rot = rotation
        nums.appendleft(nums.pop())
    return f"Best pureness {best_value} after {best_rot} rotations"


test = ([4, 3, 2, 6], 0)
result = best_list_pureness(*test)
print(result)
test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
