def create_sequence(count):
    sequence = [0, 1, 1]
    for n in range(3, count):
        next_n = sequence[n - 1] + sequence[n - 2]
        sequence.append(next_n)
    print(' '.join([str(x) for x in sequence]))


def locate_number(number):
    x, y = 0, 1
    index = 0

    while x < number:
        x, y = y, x + y
        index += 1
    if number == x:
        print(f"The number - {number} is at index {index}")
    else:
        print(f"The number {number} is not in the sequence")

# Python Advanced September 2020 - Jordan`s solution: https://pastebin.com/uQwzF9tB
