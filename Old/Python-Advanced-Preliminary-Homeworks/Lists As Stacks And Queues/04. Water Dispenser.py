from collections import deque


def dispense():
    water_quantity = int(input())
    people = deque()
    while True:
        person = input()
        if person == 'Start':
            break
        people.append(person)

    while True:
        command = input()
        if command == 'End':
            print(f"{water_quantity} liters left")
            break
        tokens = command.split()
        if tokens[0] == 'refill':
            liters = int(tokens[1])
            water_quantity += liters
        else:
            liters = int(tokens[0])
            person = people.popleft()
            if liters <= water_quantity:
                print(f"{person} got water")
                water_quantity -= liters
            else:
                print(f'{person} must wait')


dispense()