def is_cell_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size


def find_player(matrix, size):
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'P':
                return row, col


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


string = input()
n = int(input())
field = [list(input()) for _ in range(n)]
m = int(input())
pr, pc = find_player(field, n)
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(m):
    direction = input()
    next_r, next_c = pr + directions[direction][0], pc + directions[direction][1]
    if is_cell_valid(next_r, next_c, n):
        if field[next_r][next_c] != '-':
            string += field[next_r][next_c]
        field[pr][pc] = '-'
        pr, pc = next_r, next_c
        field[pr][pc] = 'P'
    else:
        if len(string) >= 1:
            string = string[:-1]

print(string)
print_matrix(field)
