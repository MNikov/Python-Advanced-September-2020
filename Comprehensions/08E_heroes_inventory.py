heroes_dict = {h: {"Items": [], "Cost": 0} for h in input().split(', ')}

while True:
    line = input()
    if line == 'End':
        break
    hero, item, cost = line.split('-')
    cost = int(cost)
    if item not in heroes_dict[hero]['Items']:
        heroes_dict[hero]['Items'].append(item)
        heroes_dict[hero]['Cost'] += cost

for h, h_dict in heroes_dict.items():
    print(f'{h} -> Items: {len(h_dict["Items"])}, Cost: {h_dict["Cost"]}')
