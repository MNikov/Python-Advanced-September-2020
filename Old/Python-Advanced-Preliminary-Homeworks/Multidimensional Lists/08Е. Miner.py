# -- 90/100 --

def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix


def find_start_position(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 's':
                start = [r, c]
                return start


def find_all_coals(matrix, size):
    all_coals = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'c':
                all_coals += 1
    return all_coals


def check_cell_validity(coordinates, size):
    row = coordinates[0]
    col = coordinates[1]
    return 0 <= row < size and 0 <= col < size


size = int(input())
commands = input().split()
field = create_matrix(size)
start_row, start_col = find_start_position(field, size)
total_coals = find_all_coals(field, size)
is_not_over_or_collected_coals = True

for command in commands:
    if command == 'up':
        next_cell_coordinates = [start_row - 1, start_col]
    elif command == 'down':
        next_cell_coordinates = [start_row + 1, start_col]
    elif command == 'left':
        next_cell_coordinates = [start_row, start_col - 1]
    else:
        next_cell_coordinates = [start_row, start_col + 1]
    if check_cell_validity(next_cell_coordinates, size):
        next_cell = field[next_cell_coordinates[0]][next_cell_coordinates[1]]
        if next_cell == '*':
            start_row, start_col = next_cell_coordinates
        elif next_cell == 'e':
            print(f"Game over! ({next_cell_coordinates[0]}, {next_cell_coordinates[1]})")
            is_not_over_or_collected_coals = False
            break
        elif next_cell == 'c':
            total_coals -= 1
            field[next_cell_coordinates[0]][next_cell_coordinates[1]] = '*'
            start_row, start_col = next_cell_coordinates
            if total_coals == 0:
                print(f"You collected all coals! ({start_row}, {start_col})")
                is_not_over_or_collected_coals = False
                break

if is_not_over_or_collected_coals:
    print(f"{total_coals} coals left. ({start_row}, {start_col})")
