def make_palindrome_matrix(rows, cols):
    matrix = [[f'{chr(97 + r)}{chr(97 + c + r)}{chr(97 + r)}' for c in range(cols)] for r in range(rows)]
    return [print(" ".join(row)) for row in matrix]


rows_count, columns_count = [int(x) for x in input().split()]
make_palindrome_matrix(rows_count, columns_count)
