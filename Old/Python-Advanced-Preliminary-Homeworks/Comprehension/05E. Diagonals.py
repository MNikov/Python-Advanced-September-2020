def create_matrix(size):
    matrix = [[int(x) for x in input().split(', ')] for _ in range(size)]
    return matrix


def print_first_diagonal(matrix, size):
    first_diagonal = [matrix[i][i] for i in range(size)]
    print(f'First diagonal: {", ".join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}')


def print_second_diagonal(matrix, size):
    second_diagonal = [matrix[i][size - i - 1] for i in range(size)]
    print(f'Second diagonal: {", ".join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}')


size = int(input())
matrix = create_matrix(size)
print_first_diagonal(matrix, size)
print_second_diagonal(matrix, size)
