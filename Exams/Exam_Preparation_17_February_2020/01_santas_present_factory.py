from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

presents_magic = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

presents_made = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while materials and magic_levels:
    current_material = materials.pop()
    current_magic = magic_levels.popleft()

    if current_material == 0 and current_magic == 0:
        continue
    if current_material == 0:
        magic_levels.appendleft(current_magic)
        continue
    if current_magic == 0:
        materials.append(current_material)
        continue

    total_magic = current_magic * current_material
    if total_magic in presents_magic:
        present = presents_magic[total_magic]
        presents_made[present] += 1
    elif total_magic < 0:
        new_sum = current_magic + current_material
        materials.append(new_sum)
    elif total_magic not in presents_magic and total_magic > 0:
        current_material += 15
        materials.append(current_material)

condition_one = presents_made['Doll'] >= 1 and presents_made['Wooden train'] >= 1
condition_two = presents_made['Teddy bear'] >= 1 and presents_made['Bicycle'] >= 1

if condition_one or condition_two:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f'Materials left: {", ".join(str(x) for x in reversed(materials))}')
if magic_levels:
    print(f'Magic left: {", ".join(str(x) for x in magic_levels)}')

[print(f'{present}: {count}') for present, count in sorted(presents_made.items()) if count > 0]
