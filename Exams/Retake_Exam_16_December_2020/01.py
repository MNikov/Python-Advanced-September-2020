from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
successful_matches = 0

while males and females:
    male = males.pop()
    female = females.popleft()
    if male <= 0 and female <= 0:
        continue
    if male <= 0:
        females.appendleft(female)
        continue
    if female <= 0:
        males.append(male)
        continue
    if male % 25 == 0:
        females.appendleft(female)
        if males:
            males.pop()
        continue
    if female % 25 == 0:
        males.append(male)
        if females:
            females.popleft()
        continue
    if male == female:
        successful_matches += 1
    else:
        males.append(male - 2)

print(f"Matches: {successful_matches}")
print(f'Males left: {", ".join(map(str, reversed(males))) if males else "none"}')
print(f'Females left: {", ".join(map(str, females)) if females else "none"}')
