def create_matrix(rows_count):
    matrix = []
    for row in range(rows_count):
        matrix.append([x for x in input().split()])
    return matrix


def count_2x2_equal_char_squares(matrix, rows_count, columns_count):
    squares_count = 0
    for r in range(rows_count - 1):
        for c in range(columns_count - 1):
            condition = matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]
            if condition:
                squares_count += 1
    return squares_count


rows_count, columns_count = [int(x) for x in input().split()]
current_matrix = create_matrix(rows_count)
print(count_2x2_equal_char_squares(current_matrix, rows_count, columns_count))