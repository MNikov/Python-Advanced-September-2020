from collections import deque


def create_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append('')
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


rows_count, cols_count = [int(x) for x in input().split()]
matrix = create_matrix(rows_count, cols_count)
snake = deque(input())

for r in range(rows_count):
    for c in range(cols_count):
        current_c = c
        if r % 2 != 0:
            current_c = cols_count - 1 - c

        snake_letter = snake.popleft()
        matrix[r][current_c] = snake_letter
        snake.append(snake_letter)

print_matrix(matrix)
