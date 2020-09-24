def create_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append([x for x in input().split()])
    return matrix


def check_valid_cell(row, col, rows_count, cols_count):
    return 0 <= row < rows_count and 0 <= col < cols_count


def print_matrix(matrix):
    for row in matrix:
        print(' '.join([str(x) for x in row]))


rows_count, cols_count = [int(x) for x in input().split()]
matrix = create_matrix(rows_count)

while True:
    line = input()
    is_invalid = False
    if line == 'END':
        break
    tokens = line.split()
    if len(tokens) == 5 and tokens[0] == 'swap':
        command, r1, c1, r2, c2 = tokens
        r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)
        if check_valid_cell(r1, c1, rows_count, cols_count) and check_valid_cell(r2, c2, rows_count, cols_count):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
            print_matrix(matrix)
        else:
            is_invalid = True
    else:
        is_invalid = True
    if is_invalid:
        print('Invalid input!')
