def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def check_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


def detonate_bomb(bomb_r, bomb_c, matrix, size):
    rows = [-1, -1, -1, 0, 1, 1, 1, 0]
    cols = [-1, 0, 1, 1, 1, 0, -1, -1]
    bomb_value = matrix[bomb_r][bomb_c]
    for i in range(len(rows)):
        bombed_row, bombed_col = bomb_r + rows[i], bomb_c + cols[i]
        if check_valid_cell(bombed_row, bombed_col, size) and matrix[bombed_row][bombed_col] > 0:
            matrix[bombed_row][bombed_col] -= bomb_value
    matrix[bomb_r][bomb_c] = 0


def get_alive_cells_and_their_sum(matrix, size):
    alive_cells = 0
    alive_cells_sum = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] > 0:
                alive_cells += 1
                alive_cells_sum += matrix[r][c]
    return alive_cells, alive_cells_sum


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(x) for x in row]))


size = int(input())
field = create_matrix(size)
bombs = input().split()

for bomb in bombs:
    b_r, b_c = [int(x) for x in bomb.split(',')]
    if field[b_r][b_c] > 0:
        detonate_bomb(b_r, b_c, field, size)

alive_cells, alive_cells_sum = get_alive_cells_and_their_sum(field, size)
print(f'Alive cells: {alive_cells}\nSum: {alive_cells_sum}')
print_matrix(field)
