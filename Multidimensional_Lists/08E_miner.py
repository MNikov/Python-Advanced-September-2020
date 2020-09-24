def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix


def find_start(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 's':
                return r, c


def get_coals_count(matrix, size):
    coals_count = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'c':
                coals_count += 1
    return coals_count


def check_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
commands = input().split()
field = create_matrix(size)
miner_r, miner_c = find_start(field, size)
coals_count = get_coals_count(field, size)
coals_collected = 0
is_done = True

for command in commands:
    if command == 'up':
        next_r, next_c = miner_r - 1, miner_c
    elif command == 'down':
        next_r, next_c = miner_r + 1, miner_c
    elif command == 'left':
        next_r, next_c = miner_r, miner_c - 1
    else:
        next_r, next_c = miner_r, miner_c + 1
    if check_valid_cell(next_r, next_c, size):
        field[miner_r][miner_c] = '*'
        if field[next_r][next_c] == 'c':
            coals_collected += 1
            if coals_collected == coals_count:
                print(f"You collected all coals! ({next_r}, {next_c})")
                is_done = False
                break
        elif field[next_r][next_c] == 'e':
            print(f"Game over! ({next_r}, {next_c})")
            is_done = False
            break
        miner_r, miner_c = next_r, next_c

if is_done:
    print(f"{coals_count - coals_collected} coals left. ({miner_r}, {miner_c})")
