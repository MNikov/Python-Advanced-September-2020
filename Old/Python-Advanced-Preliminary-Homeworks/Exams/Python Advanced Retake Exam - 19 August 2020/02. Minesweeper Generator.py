def create_field(size):
    return [[0] * size for _ in range(size)]


def check_cell(size, row, col):
    return 0 <= row < size and 0 <= col < size


def increase_neighbouring_cells(matrix, size):
    rows = [-1, -1, -1, 0, 1, 1, 1, 0]
    cols = [-1, 0, 1, 1, 1, 0, -1, -1]
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == '*':
                for i in range(8):
                    current_row = row + rows[i]
                    current_col = col + cols[i]
                    if check_cell(size, current_row, current_col):
                        if matrix[current_row][current_col] != '*':
                            matrix[current_row][current_col] += 1


def print_matrix(matrix):
    [print(' '.join([str(x) for x in row])) for row in matrix]


size = int(input())
bombs_count = int(input())
field = create_field(size)

for _ in range(bombs_count):
    line = input()
    coordinates = []
    i = 0
    while True:
        if len(coordinates) == 2:
            break
        char = line[i]
        if char.isdigit():
            coordinates.append(char)
            if i + 1 <= len(line):
                if line[i + 1].isdigit():
                    coordinates.remove(char)
                    coordinates.append(char + line[i + 1])
                    i += 2
                else:
                    i += 1
        else:
            i += 1

    bomb_row, bomb_col = [int(x) for x in coordinates]
    if check_cell(size, bomb_row, bomb_col):
        field[bomb_row][bomb_col] = '*'

increase_neighbouring_cells(field, size)
print_matrix(field)