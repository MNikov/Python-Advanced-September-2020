def create_matrix(rows):
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    return matrix


def valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


def print_matrix(matrix):
    [print(' '.join([str(x) for x in row])) for row in matrix]  # did this for the sake of using comprehension


rows = int(input())
matrix = create_matrix(rows)

while True:
    line = input()
    if line == 'END':
        print_matrix(matrix)
        break
    command, *rest = line.split()
    row, col, value = map(int, rest)
    if valid_cell(row, col, rows):
        if command == 'Add':
            matrix[row][col] += value
        elif command == 'Subtract':
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
