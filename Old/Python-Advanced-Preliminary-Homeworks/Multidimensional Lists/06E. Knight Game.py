def create_matrix(rows_count):
    matrix = []
    for _ in range(rows_count):
        matrix.append([x for x in input()])
    return matrix


def validate_position(position, size):
    row = position[0]
    col = position[1]
    return 0 <= row < size and 0 <= col < size


def get_knight_kills(row, col, size, matrix):
    kills = 0
    rows = [-1, -2, -2, -1, 1, 2, 2, 1]  # coordinates of possible neighbouring K`s
    cols = [-2, -1, 1, 2, 2, 1, -1, -2]
    n = len(rows)  # = len(cols)
    for i in range(n):
        current_pos = [row + rows[i], col + cols[i]]
        if validate_position(current_pos, size) and matrix[current_pos[0]][current_pos[1]] == 'K':
            kills += 1
    return kills


rows_count = int(input())
matrix = create_matrix(rows_count)
total_kills = 0

while True:
    most_kills = 0
    knight_to_kill_coordinates = []
    for row in range(rows_count):
        for col in range(rows_count):
            if matrix[row][col] == 'K':
                killed_knights = get_knight_kills(row, col, rows_count, matrix)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    knight_to_kill_coordinates = [row, col]
    if most_kills == 0:
        break

    knight_to_kill_row = knight_to_kill_coordinates[0]
    knight_to_kill_col = knight_to_kill_coordinates[1]
    matrix[knight_to_kill_row][knight_to_kill_col] = "0"
    total_kills += 1

print(total_kills)
