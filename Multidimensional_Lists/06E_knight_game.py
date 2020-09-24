def create_field(size):
    field = [[x for x in input()] for _ in range(size)]
    return field


def check_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_knight_kills(row, col, matrix):
    kills = 0
    rows = [-2, -1, -2, -1, 1, 2, 2, 1]
    cols = [-1, -2, 1, 2, 2, 1, -1, -2]
    for i in range(len(rows)):
        if check_valid_cell(row + rows[i], col + cols[i], size) and matrix[row + rows[i]][col + cols[i]] == 'K':
            kills += 1
    return kills


size = int(input())
field = create_field(size)
total_kills = 0

while True:
    most_kills = 0
    knight_r, knight_c = 0, 0
    for r in range(size):
        for c in range(size):
            if field[r][c] == 'K':
                knight_kills = get_knight_kills(r, c, field)
                if knight_kills > most_kills:
                    most_kills = knight_kills
                    knight_r, knight_c = r, c
    if most_kills == 0:
        break
    field[knight_r][knight_c] = '0'
    total_kills += 1

print(total_kills)
