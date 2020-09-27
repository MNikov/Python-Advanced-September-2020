def get_matrix_of_palindromes(rows, cols):
    matrix = [[chr(97 + r) + chr(97 + r + c) + chr(97 + r) for c in range(cols)] for r in range(rows)]
    return matrix


rows, cols = [int(x) for x in input().split()]
matrix = get_matrix_of_palindromes(rows, cols)
for row in matrix:
    print(' '.join(row))
