def flatten_matrix(rows):
    flattened_matrix = [x for row in [[int(x) for x in input().split(', ')] for _ in range(rows)] for x in row]
    return flattened_matrix


print(flatten_matrix(int(input())))
