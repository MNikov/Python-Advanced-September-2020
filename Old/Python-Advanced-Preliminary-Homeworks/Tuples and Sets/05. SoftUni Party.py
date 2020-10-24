def distribute_guests(n, end_command):
    guests = set()
    for _ in range(n):
        guest = input()
        guests.add(guest)
    while True:
        guest_arrived = input()
        if guest_arrived == end_command:
            break
        guests.remove(guest_arrived)
    return guests


def print_guests(guests):
    guests = sorted(guests)
    print(len(guests))
    [print(g) for g in guests]


print_guests(distribute_guests(int(input()), 'END'))
