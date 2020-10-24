def create_inventory():
    inventory = {name: {} for name in input().split(', ')}
    return inventory


def fill_inventory(inventory):
    while True:
        line = input()
        if line == 'End':
            break
        name, item, price = line.split('-')
        price = int(price)
        if item not in inventory[name]:
            inventory[name][item] = price
    return inventory


inventory = create_inventory()
fill_inventory(inventory)
[print(f'{name} -> Items: {len(inventory[name])}, Cost: {sum(inventory[name].values())}') for name in inventory]
