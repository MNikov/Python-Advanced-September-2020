def create_field(rows):
    field = []
    for _ in range(rows):
        field.append([x for x in input()])
    return field


def find_player(matrix, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'P':
                return r, c


def check_valid_cell(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


def find_bunnies(matrix, rows_count, cols_count):
    bunnies = []
    for r in range(rows_count):
        for c in range(cols_count):
            if matrix[r][c] == 'B':
                bunnies.append((r, c))
    return bunnies


def multiply_bunnies(matrix, rows_count, cols_count):
    rows = [-1, 0, 1, 0]
    cols = [0, 1, 0, -1]
    is_dead = False
    bunny_coordinates = find_bunnies(matrix, rows_count, cols_count)
    for bunny_coord in bunny_coordinates:
        b_r, b_c = bunny_coord
        for i in range(4):
            next_r, next_c = b_r + rows[i], b_c + cols[i]
            if check_valid_cell(next_r, next_c, rows_count, cols_count):
                if matrix[next_r][next_c] == 'P':
                    is_dead = True
                matrix[next_r][next_c] = 'B'
    if is_dead:
        print_matrix(lair)
        print(f'dead: {player_r} {player_c}')
        exit()


rows_count, cols_count = [int(x) for x in input().split()]
lair = create_field(rows_count)
commands = input()
player_r, player_c = find_player(lair, rows_count, cols_count)

for command in commands:
    if command == 'U':
        next_r, next_c = player_r - 1, player_c
    elif command == 'D':
        next_r, next_c = player_r + 1, player_c
    elif command == 'L':
        next_r, next_c = player_r, player_c - 1
    else:
        next_r, next_c = player_r, player_c + 1

    if check_valid_cell(next_r, next_c, rows_count, cols_count):
        lair[player_r][player_c] = '.'
        if lair[next_r][next_c] == '.':
            player_r, player_c = next_r, next_c
            lair[player_r][player_c] = 'P'
        elif lair[next_r][next_c] == 'B':
            player_r, player_c = next_r, next_c
            multiply_bunnies(lair, rows_count, cols_count)
            print_matrix(lair)
            print(f'dead: {player_r} {player_c}')
            break
    else:
        lair[player_r][player_c] = '.'
        multiply_bunnies(lair, rows_count, cols_count)
        print_matrix(lair)
        print(f'won: {player_r} {player_c}')
        break
    multiply_bunnies(lair, rows_count, cols_count)
