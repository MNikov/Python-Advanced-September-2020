from collections import deque

string = deque(input().split())
main = ('red', 'yellow', 'blue')
secondary = ('orange', 'purple', 'green')
all = main + secondary
colors_made = []

while string:
    mid = len(string) // 2 - 1
    front = string.popleft()
    if not string:
        if front in all:
            colors_made.append(front)
        break
    back = string.pop()
    if (front + back) in all:
        colors_made.append((front + back))
    elif (back + front) in all:
        colors_made.append((back + front))
    else:
        new_front = front[:-1]
        if len(new_front) >= 1:
            string.insert(mid, front[:-1])
        new_back = back[:-1]
        if len(new_back) >= 1:
            string.insert(mid, back[:-1])

for color in colors_made:
    if color in secondary:
        if color == 'orange':
            if 'red' not in colors_made or 'yellow' not in colors_made:
                colors_made.remove(color)
        elif color == 'purple':
            if 'red' not in colors_made or 'blue' not in colors_made:
                colors_made.remove(color)
        elif color == 'green':
            if 'yellow' not in colors_made or 'blue' not in colors_made:
                colors_made.remove(color)

print(colors_made)
