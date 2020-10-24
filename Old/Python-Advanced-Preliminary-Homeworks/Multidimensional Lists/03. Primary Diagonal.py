def read_matrix(rows_count):
    matrix = []
    for _ in range(rows_count):
        matrix.append([int(x) for x in input().split()])
    return matrix


def primary_diagonal_sum(matrix):
    pd_sum = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if row == col:
                pd_sum += matrix[row][col]
    # for i in range(len(matrix)):
    #     pd_sum += matrix[i][i]
    return pd_sum


print(primary_diagonal_sum(read_matrix(int(input()))))
