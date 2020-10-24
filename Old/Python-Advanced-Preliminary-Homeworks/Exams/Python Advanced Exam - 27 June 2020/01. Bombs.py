from collections import deque

bombs = {'Datura Bombs': 40, 'Cherry Bombs': 60, 'Smoke Decoy Bombs': 120}
bombs_created = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]
is_pouch_filled = False

while True:
    if bombs_created['Datura Bombs'] >= 3 and bombs_created['Cherry Bombs'] >= 3 and bombs_created[
        'Smoke Decoy Bombs'] >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        is_pouch_filled = True
        break
    if len(bomb_casings) == 0 or len(bomb_effects) == 0:
        break
    is_created = False
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()
    for bomb in bombs:
        if current_casing + current_effect == bombs[bomb]:
            bombs_created[bomb] += 1
            is_created = True
            break
    if not is_created:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)

if not is_pouch_filled:
    print("You don't have enough materials to fill the bomb pouch.")

if len(bomb_effects) == 0:
    print("Bomb Effects: empty")
else:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')

if len(bomb_casings) == 0:
    print("Bomb Casings: empty")
else:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')

bombs_created = dict(sorted(bombs_created.items()))
for bomb, count in bombs_created.items():
    print(f'{bomb}: {count}')
