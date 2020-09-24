def create_matrix(rows):
    matrix = []
    for r in range(rows):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


def get_matrix_sum(matrix):
    matrix_sum = 0
    for row in matrix:
        for col in row:
            matrix_sum += col
    print(matrix_sum)


rows_count, cols_count = [int(x) for x in input().split(', ')]
matrix = create_matrix(rows_count)
get_matrix_sum(matrix)
print(matrix)
