from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0

while True:
    bottle = bottles.pop()
    cup = cups.popleft()
    if bottle > cup:
        wasted_water += bottle - cup
    cup -= bottle
    if cup > 0:
        cups.appendleft(cup)

    if not cups:
        result = 'Bottles: '
        while bottles:
            result += f'{str(bottles.pop())} '
        break
    if not bottles:
        result = 'Cups: '
        while cups:
            result += f'{str(cups.popleft())} '
        break

print(result)
print(f"Wasted litters of water: {wasted_water}")
