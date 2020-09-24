from sys import maxsize


def create_matrix(rows_count):
    matrix = []
    for _ in range(rows_count):
        matrix.append([int(x) for x in input().split()])
    return matrix


def find_max_sum_and_best_sub_matrix(matrix, rows_count, columns_count):
    max_sum = -maxsize
    for row in range(rows_count - 2):
        for col in range(columns_count - 2):
            current_sum = 0
            sub_matrix = []
            row_counter = 0
            for r in range(row, row + 3):
                sub_matrix.append([])
                for c in range(col, col + 3):
                    sub_matrix[row_counter].append(matrix[r][c])
                    current_sum += matrix[r][c]
                row_counter += 1
            if current_sum > max_sum:
                max_sum = current_sum
                best_sub_matrix = sub_matrix
    return max_sum, best_sub_matrix


rows_count, columns_count = [int(x) for x in input().split()]
current_matrix = create_matrix(rows_count)
max_sum, best_sub_matrix = find_max_sum_and_best_sub_matrix(current_matrix, rows_count, columns_count)
print(f'Sum = {max_sum}')
for row in best_sub_matrix:
    print(' '.join([str(x) for x in row]))
