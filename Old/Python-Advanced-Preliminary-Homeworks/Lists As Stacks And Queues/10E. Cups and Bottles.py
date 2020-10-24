from collections import deque

empty_cups = deque([int(c) for c in input().split()])
bottles = [int(b) for b in input().split()]
wasted_water = 0

while empty_cups and bottles:
    current_bottle = bottles.pop()
    current_cup = empty_cups.popleft()
    current_cup -= current_bottle
    if current_cup == 0:
        continue
    elif current_cup > 0:
        empty_cups.appendleft(current_cup)
    elif current_cup < 0:
        wasted_water += -current_cup

if not empty_cups:
    print('Bottles: ', end='')
    while bottles:
        print(bottles.pop(), end=' ')

else:
    print('Cups: ', end='')
    while empty_cups:
        print(empty_cups.popleft(), end=' ')
print()
print(f"Wasted litters of water: {wasted_water}")
