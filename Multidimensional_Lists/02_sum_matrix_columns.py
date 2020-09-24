def create_matrix(rows):
    matrix = []
    for _ in range(rows):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def get_matrix_col_sum(matrix, rows_count, cols_count, cols_sums):
    for row in range(rows_count):
        for col in range(cols_count):
            cols_sums[col] += matrix[row][col]
    print('\n'.join([str(x) for x in col_sums]))


rows_count, cols_count = [int(x) for x in input().split(', ')]
matrix = create_matrix(rows_count)
col_sums = cols_count * [0]
get_matrix_col_sum(matrix, rows_count, cols_count, col_sums)
