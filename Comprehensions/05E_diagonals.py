def find_first_diagonal(matrix):
    diagonal = [matrix[i][i] for i in range(len(matrix))]
    return diagonal


def find_second_diagonal(matrix):
    diagonal = [matrix[i][-i - 1] for i in range(len(matrix))]
    return diagonal


matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
first_diagonal = find_first_diagonal(matrix)
second_diagonal = find_second_diagonal(matrix)
print(f'First diagonal: {", ".join([str(x) for x in first_diagonal])}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join([str(x) for x in second_diagonal])}. Sum: {sum(second_diagonal)}')
