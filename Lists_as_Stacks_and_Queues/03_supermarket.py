from collections import deque


def main():
    names = deque()
    while True:
        name = input()
        if name == 'End':
            break
        elif name == 'Paid':
            while names:
                print(names.popleft())
        else:
            names.append(name)
    print(f'{len(names)} people remaining.')


main()
