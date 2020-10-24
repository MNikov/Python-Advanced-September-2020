from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches_count = 0

while males and females:
    male = males.pop()
    female = females.popleft()
    if male <= 0:
        females.appendleft(female)
        continue
    if female <= 0:
        males.append(male)
        continue

    if male % 25 == 0:
        if males:
            males.pop()
        females.appendleft(female)
        continue
    if female % 25 == 0:
        if females:
            females.popleft()
        males.append(male)
        continue

    if male == female:
        matches_count += 1
    else:
        males.append(male - 2)

print(f'Matches: {matches_count}')
print(f"Males left: {', '.join([str(x) for x in reversed(males)]) if males else 'none'}")
print(f"Females left: {', '.join([str(x) for x in females]) if females else 'none'}")
