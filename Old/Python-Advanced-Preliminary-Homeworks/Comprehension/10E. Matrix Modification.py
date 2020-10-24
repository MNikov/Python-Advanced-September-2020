def create_matrix(size):
    return [[int(x) for x in input().split()] for _ in range(size)]


def check_coordinates(row, col, size):
    return 0 <= row < size and 0 <= col < size


def modify_matrix(matrix, size):
    while True:
        line = input()
        if line == 'END':
            [print(' '.join([str(x) for x in row])) for row in matrix]
            break
        command, row, col, value = line.split()
        row, col, value = int(row), int(col), int(value)
        if check_coordinates(row, col, size):
            if command == 'Add':
                matrix[row][col] += value
            else:
                matrix[row][col] -= value
        else:
            print('Invalid coordinates')


size = int(input())
matrix = create_matrix(size)
modify_matrix(matrix, size)
