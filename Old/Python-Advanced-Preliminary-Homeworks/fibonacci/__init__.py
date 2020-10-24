def create_fib(n):
    if n == 0:
        return 0
    fib_list = [0, 1]
    for i in range(2, n):
        current_number = fib_list[i - 2] + fib_list[i - 1]
        fib_list.append(current_number)
    print(' '.join([str(x) for x in fib_list]))


def locate(number):
    x, y = 0, 1
    index = 0

    while x < number:
        x, y = y, x + y
        index += 1
    if number == x:
        print(f"The number - {number} is at index {index}")
    else:
        print(f"The number {number} is not in the sequence")
