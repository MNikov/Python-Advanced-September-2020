def find_symbol(matrix, symbol):
    for i in range(len(matrix)):
        string = matrix[i]
        if symbol in string:
            return f'({i}, {string.index(symbol)})'
    return None


rows_count = int(input())
matrix = [input() for _ in range(rows_count)]
symbol = input()
result = find_symbol(matrix, symbol)

if result:
    print(result)
else:
    print(f'{symbol} does not occur in the matrix')