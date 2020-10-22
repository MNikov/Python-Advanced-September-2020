from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()
    if current_male <= 0:
        females.appendleft(current_female)
        continue
    if current_female <= 0:
        males.append(current_male)
        continue
    if current_male % 25 == 0:
        if males:
            males.pop()
        females.appendleft(current_female)
        continue
    if current_female % 25 == 0:
        if females:
            females.popleft()
        males.append(current_male)
        continue
    if current_male == current_female:
        matches += 1
    else:
        males.append(current_male - 2)

print(f'Matches: {matches}')
print(f'Males left: {", ".join(map(str, reversed(males)))}') if males else print("Males left: none")
print(f'Females left: {", ".join(map(str, females))}') if females else print("Females left: none")
