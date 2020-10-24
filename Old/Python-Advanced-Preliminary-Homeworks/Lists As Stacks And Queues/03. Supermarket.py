from _collections import deque


def solution():
    people = deque()
    while True:
        name = input()
        if name == 'End':
            print(f'{len(people)} people remaining.')
            break
        elif name == 'Paid':
            while people:
                popped_person = people.popleft()
                print(popped_person)
        else:
            people.append(name)


solution()
