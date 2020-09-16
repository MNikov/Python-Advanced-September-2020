def collect_guests(n):
    all_guests = [input() for _ in range(n)]
    return all_guests


def get_not_arrived_guests(guests: list):
    while True:
        guest = input()
        if guest == 'END':
            break
        guests.remove(guest)
    print(len(guests))
    [print(g) for g in sorted(guests)]


guests_count = int(input())
all_guests = collect_guests(guests_count)
get_not_arrived_guests(all_guests)