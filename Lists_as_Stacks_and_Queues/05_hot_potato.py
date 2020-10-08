from collections import deque


def play_hot_potato(names, toss_count):
    names = deque(names)
    while len(names) > 1:
        names.rotate(-toss_count)
        kid = names.pop()
        print(f'Removed {kid}')

    print(f'Last is {names[0]}')


play_hot_potato(input().split(), int(input()))

