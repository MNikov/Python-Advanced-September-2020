def create_field(n):
    return [[x for x in input()] for _ in range(n)]


def find_player(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'P':
                return r, c


def check_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


string = input()
size = int(input())
field = create_field(size)
lines_count = int(input())
player_r, player_c = find_player(field, size)
dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

for _ in range(lines_count):
    dir = input()
    next_r = player_r + dirs[dir][0]
    next_c = player_c + dirs[dir][1]
    if not check_valid_cell(next_r, next_c, size):
        if len(string) > 0:
            string = string[:-1]
    else:
        if field[next_r][next_c] != '-':
            string += field[next_r][next_c]
        field[next_r][next_c] = 'P'
        field[player_r][player_c] = '-'
        player_r, player_c = next_r, next_c

print(string)
[print(''.join(row)) for row in field]
