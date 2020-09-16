def give_nums_in_parking_lot(n):
    parking_lot = set()
    for _ in range(n):
        command, number = input().split(', ')
        if command == 'IN':
            parking_lot.add(number)
        else:
            parking_lot.remove(number)
    if not parking_lot:
        print('Parking Lot is Empty')
    else:
        [print(n) for n in parking_lot]


give_nums_in_parking_lot(int(input()))
