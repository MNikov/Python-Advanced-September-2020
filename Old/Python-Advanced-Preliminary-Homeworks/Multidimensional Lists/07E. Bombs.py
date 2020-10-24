def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def is_valid_cell(position, size):
    row = position[0]
    col = position[1]
    return 0 <= row < size and 0 <= col < size


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(x) for x in row]))


def count_alive_cells_and_sum_them(matrix, size):
    alive_cells_count = 0
    alive_cells_sum = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] > 0:
                alive_cells_count += 1
                alive_cells_sum += matrix[r][c]
    return alive_cells_count, alive_cells_sum


size = int(input())
matrix = create_matrix(size)
base_matrix = matrix
bomb_coordinates = input().split()

target_rows = [-1, -1, -1, 0, 1, 1, 1, 0]
target_cols = [-1, 0, 1, 1, 1, 0, -1, -1]

for row_col in bomb_coordinates:
    tokens = row_col.split(',')
    row, col = int(tokens[0]), int(tokens[1])
    current_bomb = base_matrix[row][col]
    if base_matrix[row][col] > 0:
        for i in range(8):
            bombed_cell_position = [row + target_rows[i], col + target_cols[i]]
            if is_valid_cell(bombed_cell_position, size):
                cell_row = bombed_cell_position[0]
                cell_col = bombed_cell_position[1]
                if matrix[cell_row][cell_col] > 0:
                    matrix[cell_row][cell_col] -= current_bomb
                matrix[row][col] = 0
                base_matrix[row][col] = 0

alive_cells_count, alive_cells_sum = count_alive_cells_and_sum_them(matrix, size)
print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
print_matrix(matrix)
