def add_filter_phonebook():
    phonebook = {}
    while True:
        line = input().split('-')
        if len(line) != 2:
            number = int(line[0])
            for _ in range(number):
                name = input()
                if name in phonebook:
                    print(f'{name} -> {phonebook[name]}')
                else:
                    print(f'Contact {name} does not exist.')
            break
        name, phone_number = line
        phonebook[name] = phone_number


add_filter_phonebook()
