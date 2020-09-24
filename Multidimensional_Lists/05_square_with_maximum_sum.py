def create_matrix(rows_count):
    matrix = []
    for _ in range(rows_count):
        matrix.append([int(x) for x in input().split(', ')])
    return matrix


def get_square_sum(row, col, matrix):
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


rows_count, cols_count = [int(x) for x in input().split(', ')]
matrix = create_matrix(rows_count)
best_pos = 0, 0
best_sum = get_square_sum(0, 0, matrix)

for r in range(rows_count - 1):
    for c in range(cols_count - 1):
        current_pos = r, c
        current_sum = get_square_sum(r, c, matrix)
        if current_sum > best_sum:
            best_pos = current_pos
            best_sum = current_sum

print_square(matrix, best_pos[0], best_pos[1])
print(best_sum)
