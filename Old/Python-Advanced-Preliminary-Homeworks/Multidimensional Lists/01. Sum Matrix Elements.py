def matrix_sum(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    return total_sum


rows_count, columns_count = [int(x) for x in input().split(', ')]

matrix = []
for _ in range(rows_count):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

print(matrix_sum(matrix))
print(matrix)
