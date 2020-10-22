def find_player(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'P':
                return r, c


def check_valid_cell(size, r, c):
    return 0 <= r < size and 0 <= c < size


string = input()
size = int(input())
field = [list(input()) for _ in range(size)]
m = int(input())
pr, pc = find_player(field)
deltas = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(m):
    command = input()
    next_r, next_c = pr + deltas[command][0], pc + deltas[command][1]
    if check_valid_cell(size, next_r, next_c):
        if field[next_r][next_c] != '-':
            string += field[next_r][next_c]
        field[next_r][next_c] = 'P'
        field[pr][pc] = '-'
        pr, pc = next_r, next_c
    else:
        if len(string) > 0:
            string = string[:-1]

print(string)
for row in field:
    print(''.join(row))
