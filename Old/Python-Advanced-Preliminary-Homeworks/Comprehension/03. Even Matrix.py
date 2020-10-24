def create_matrix_with_even_numbers(rows):
    matrix = [[int(x) for x in input().split(', ') if int(x) % 2 == 0] for _ in range(rows)]
    return matrix


print(create_matrix_with_even_numbers(int(input())))
