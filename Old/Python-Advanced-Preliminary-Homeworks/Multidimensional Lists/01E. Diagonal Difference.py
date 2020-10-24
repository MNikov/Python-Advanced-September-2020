def read_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def find_primary_diagonal_sum(matrix, size):
    primary_diagonal_sum = 0
    for i in range(size):
        primary_diagonal_sum += matrix[i][i]
    return primary_diagonal_sum


def find_secondary_diagonal_sum(matrix, size):
    secondary_diagonal_sum = 0
    for r in range(size):
        for c in range(size):
            if r + c == size - 1:
                secondary_diagonal_sum += matrix[r][c]
        # for i in range(size):
        #     secondary_diagonal_sum += matrix[i][size - i - 1]
        #                                             [- i - 1] <- would work the same way
    return secondary_diagonal_sum


size = int(input())
matrix = read_matrix(size)
pd_sum = find_primary_diagonal_sum(matrix, size)
sd_sum = find_secondary_diagonal_sum(matrix, size)
print(abs(pd_sum - sd_sum))
