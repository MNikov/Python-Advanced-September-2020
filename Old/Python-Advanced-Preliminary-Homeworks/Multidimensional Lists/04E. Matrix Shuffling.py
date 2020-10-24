def create_matrix(rows_count):
    matrix = []
    for _ in range(rows_count):
        matrix.append([x for x in input().split()])
    return matrix


def validate_position(position, rows_count, cols_count):
    current_row = position[0]
    current_col = position[1]
    return 0 <= current_row < rows_count and 0 <= current_col < cols_count


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


rows_count, cols_count = [int(x) for x in input().split()]
matrix = create_matrix(rows_count)

while True:
    line = input().split()
    if line[0] == 'END':
        break
    is_valid = True
    if line[0] == 'swap' and len(line) == 5:
        pos_1 = [int(line[1]), int(line[2])]
        pos_2 = [int(line[3]), int(line[4])]
        if validate_position(pos_1, rows_count, cols_count) and validate_position(pos_2, rows_count, cols_count):
            r1, c1 = pos_1
            r2, c2 = pos_2
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            print_matrix(matrix)
        else:
            is_valid = False
    else:
        is_valid = False
    if not is_valid:
        print('Invalid input!')
