def fill_and_filter_phonebook():
    phonebook = {}
    while True:
        line = input().split('-')
        if len(line) != 2:
            n = int(line[0])
            for _ in range(n):
                name = input()
                if name in phonebook:
                    print(f'{name} -> {phonebook[name]}')
                else:
                    print(f'Contact {name} does not exist.')
            break
        name, number = line
        phonebook[name] = number


fill_and_filter_phonebook()
