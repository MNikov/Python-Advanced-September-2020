from collections import deque


def create_matrix(rows_count, columns_count):
    matrix = []
    for _ in range(rows_count):
        row = [0] * columns_count
        matrix.append(row)
    return matrix


def fill_matrix_with_snake(matrix, rows_count, columns_count, snake):
    snake = deque(snake)
    for r in range(rows_count):
        for c in range(columns_count):
            current_col = c
            if r % 2 != 0:
                current_col = columns_count - 1 - c
            snake_letter = snake.popleft()
            matrix[r][current_col] = snake_letter
            snake.append(snake_letter)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


rows_count, columns_count = [int(x) for x in input().split()]
snake = input()
matrix = create_matrix(rows_count, columns_count)
fill_matrix_with_snake(matrix, rows_count, columns_count, snake)
print_matrix(matrix)

# -- ALTERNATIVE CODE --
# def create_matrix(rows_count, columns_count):
#     matrix = []
#     for _ in range(rows_count):
#         row = [0] * columns_count
#         matrix.append(row)
#     return matrix
#
#
# def fill_matrix_with_snake(matrix, snake):
#     snake_index = 0
#     for r in range(len(matrix)):
#         for c in range(len(matrix[r])):
#             if snake_index == len(snake):
#                 snake_index = 0
#             matrix[r][c] = snake[snake_index]
#             snake_index += 1
#     return matrix
#
#
# def print_matrix(matrix):
#     for i, row in enumerate(matrix):
#         if i % 2 != 0:
#             print(''.join(row[::-1]))
#         else:
#             print(''.join(row))
#
#
# rows_count, columns_count = [int(x) for x in input().split()]
# matrix = create_matrix(rows_count, columns_count)
# snake = input()
# fill_matrix_with_snake(matrix, snake)
# print_matrix(matrix)
