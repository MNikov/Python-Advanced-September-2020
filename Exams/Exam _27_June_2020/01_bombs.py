from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]

bombs = {
    'Datura Bombs': 40,
    'Cherry Bombs': 60,
    'Smoke Decoy Bombs': 120
}

pouch = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}


def check_if_pouch_full(pouch: dict):
    return all([count >= 3 for count in pouch.values()])


while bomb_effects and bomb_casings and not check_if_pouch_full(pouch):
    is_produced = False
    curr_effect = bomb_effects.popleft()
    curr_casing = bomb_casings.pop()
    curr_sum = curr_casing + curr_effect
    for bomb_name, price in bombs.items():
        if curr_sum == price:
            pouch[bomb_name] += 1
            is_produced = True
            break
    if not is_produced:
        curr_casing -= 5
        bomb_effects.appendleft(curr_effect)
        bomb_casings.append(curr_casing)

if check_if_pouch_full(pouch):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects]) if bomb_effects else "empty"}')
print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings]) if bomb_casings else "empty"}')

for b, c in sorted(pouch.items()):
    print(f'{b}: {c}')
