def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def get_primary_diagonal_sum(matrix, size):
    p_d_sum = 0
    for i in range(size):
        p_d_sum += matrix[i][i]
    return p_d_sum


def get_secondary_diagonal_sum(matrix, size):
    s_d_sum = 0
    for i in range(size):
        s_d_sum += matrix[i][size - i - 1]
    return s_d_sum


size = int(input())
matrix = create_matrix(size)
prim_diag_sum = get_primary_diagonal_sum(matrix, size)
sec_diag_sum = get_secondary_diagonal_sum(matrix, size)
print(abs(prim_diag_sum - sec_diag_sum))
