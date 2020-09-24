def create_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def get_primary_diagonal_sum(matrix, size):
    p_d_sum = 0
    for r in range(size):
        p_d_sum += matrix[r][r]
    print(p_d_sum)


n = int(input())
matrix = create_matrix(n)
get_primary_diagonal_sum(matrix, n)