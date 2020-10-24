def collect_numbers(n):
    all_plates = set()
    for _ in range(n):
        command, number = input().split(', ')
        if command == 'IN':
            all_plates.add(number)
        elif command == 'OUT':
            if number in all_plates:
                all_plates.remove(number)
    return all_plates


def print_plates(plates):
    if len(plates) == 0:
        print('Parking Lot is Empty')
    else:
        [print(p) for p in plates]


print_plates(collect_numbers(int(input())))