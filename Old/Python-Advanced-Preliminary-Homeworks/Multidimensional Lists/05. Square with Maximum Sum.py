def read_matrix(rows_count):
    matrix = []
    for _ in range(rows_count):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def get_square_sum(matrix, row, col):
    square_sum = 0
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            square_sum += matrix[r][c]
    return square_sum


def print_square(matrix, row, col):
    for r in range(row, row + 2):
        for c in range(col, col + 2):
            print(matrix[r][c], end=' ')
        print()


rows_count, columns_count = [int(x) for x in input().split(', ')]
current_matrix = read_matrix(rows_count)

best_position = 0, 0
best_value = get_square_sum(current_matrix, 0, 0)

for row in range(len(current_matrix) - 1):
    for col in range(len(current_matrix[row]) - 1):
        current_value = get_square_sum(current_matrix, row, col)
        if current_value > best_value:
            best_value = current_value
            best_position = row, col

best_row, best_col = best_position
print_square(current_matrix, best_row, best_col)
print(best_value)
