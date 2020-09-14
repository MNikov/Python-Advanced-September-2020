from collections import deque


def dispense_water(water_quantity):
    people = deque()
    while True:
        person = input()
        if person == 'Start':
            break
        people.append(person)

    while True:
        command = input()
        if command == 'End':
            break
        tokens = command.split()
        if tokens[0] == 'refill':
            water_quantity += int(tokens[1])
        else:
            person = people.popleft()
            liters_to_get = int(tokens[0])
            if liters_to_get <= water_quantity:
                water_quantity -= liters_to_get
                print(f"{person} got water")
            else:
                print(f"{person} must wait")

    print(f"{water_quantity} liters left")


dispense_water(int(input()))
