rows_count, columns_count = [int(x) for x in input().split(', ')]

columns_sum = [0] * columns_count
matrix = []

for _ in range(rows_count):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

for row in range(rows_count):
    for col in range(columns_count):
        columns_sum[col] += matrix[row][col]

[print(x) for x in columns_sum]