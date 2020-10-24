from collections import deque


def solution(kids, tosses):
    kids = deque(kids)
    toss_counter = 0
    while kids:
        toss_counter += 1
        popped_kid = kids.popleft()
        if tosses == toss_counter:
            if kids:
                print(f'Removed {popped_kid}')
                toss_counter = 0
            else:
                print(f'Last is {popped_kid}')
        else:
            kids.append(popped_kid)


solution(input().split(), int(input()))