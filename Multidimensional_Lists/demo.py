def create_matrix(rows_count):
    matrix = []
    for _ in range(rows_count):
        line = input()
        row = [char for char in line]
        matrix.append(row)
    return matrix


def find_player(rows_count, columns_count, matrix):
    for row in range(rows_count):
        for col in range(columns_count):
            if matrix[row][col] == 'P':
                return [row, col]


def check_cell_validity(coordinates, rows_count, columns_count):
    row = coordinates[0]
    col = coordinates[1]
    return 0 <= row < rows_count and 0 <= col < columns_count


def find_bunnies(rows_count, columns_count, matrix):
    bunny_coordinates = []
    for r in range(rows_count):
        for c in range(columns_count):
            if matrix[r][c] == 'B':
                bunny_coordinates.append([r, c])
    return bunny_coordinates


def multiply_bunnies(bunny_coordinates, rows_count, columns_count, matrix):
    rows = [-1, 0, 1, 0]
    cols = [0, 1, 0, -1]
    is_dead = False
    for i in range(4):
        for b_coord in bunny_coordinates:
            b_r, b_c = b_coord
            coordinates = [b_r + rows[i], b_c + cols[i]]
            if check_cell_validity(coordinates, rows_count, columns_count):
                if matrix[coordinates[0]][coordinates[1]] == '.':
                    matrix[coordinates[0]][coordinates[1]] = 'B'
                elif matrix[coordinates[0]][coordinates[1]] == 'P':
                    matrix[coordinates[0]][coordinates[1]] = 'B'
                    is_dead = True
    if is_dead:
        print_matrix(lair)
        print(f'dead: {coordinates[0]} {coordinates[1]}')
        exit()


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


rows_count, columns_count = [int(x) for x in input().split()]
lair = create_matrix(rows_count)
commands = input()
player_row, player_col = find_player(rows_count, columns_count, lair)

for command in commands:
    if command == 'U':
        next_cell_coordinates = [player_row - 1, player_col]
    elif command == 'D':
        next_cell_coordinates = [player_row + 1, player_col]
    elif command == 'L':
        next_cell_coordinates = [player_row, player_col - 1]
    else:
        next_cell_coordinates = [player_row, player_col + 1]
    if check_cell_validity(next_cell_coordinates, rows_count, columns_count):
        lair[player_row][player_col] = '.'
        if lair[next_cell_coordinates[0]][next_cell_coordinates[1]] == 'B':
            lair[player_row][player_col] = '.'
            player_row, player_col = next_cell_coordinates
            lair[player_row][player_col] = 'P'
            bunny_coordinates = find_bunnies(rows_count, columns_count, lair)
            multiply_bunnies(bunny_coordinates, rows_count, columns_count, lair)
            print_matrix(lair)
            print(f'dead: {player_row} {player_col}')
            break
        else:
            lair[next_cell_coordinates[0]][next_cell_coordinates[1]] = 'P'
            player_row, player_col = next_cell_coordinates
    else:
        lair[player_row][player_col] = '.'
        bunny_coordinates = find_bunnies(rows_count, columns_count, lair)
        multiply_bunnies(bunny_coordinates, rows_count, columns_count, lair)
        print_matrix(lair)
        print(f'won: {player_row} {player_col}')
        break
    bunny_coordinates = find_bunnies(rows_count, columns_count, lair)
    multiply_bunnies(bunny_coordinates, rows_count, columns_count, lair)
