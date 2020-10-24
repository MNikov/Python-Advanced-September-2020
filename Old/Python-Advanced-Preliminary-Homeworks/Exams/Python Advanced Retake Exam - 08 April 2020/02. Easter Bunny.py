from sys import maxsize


def create_field(size):
    matrix = [[x if x == 'B' or x == 'X' else int(x) for x in input().split()] for _ in range(size)]
    return matrix


def find_bunny(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                return r, c


def valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


size = int(input())
field = create_field(size)
bunny_row, bunny_col = find_bunny(field, size)

sums = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
directions = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
best_sum = -maxsize
best_direction = ''
best_path = ''

for direction in directions:
    current_sum = 0
    current_path = []
    current_row, current_col = bunny_row, bunny_col
    if not valid_cell(current_row + directions[direction][0], current_col + directions[direction][1], size):
        continue
    while valid_cell(current_row, current_col, size):
        current_cell = field[current_row][current_col]
        if current_cell != 'X' and current_cell != 'B':
            current_sum += current_cell
            current_path.append([current_row, current_col])
        elif current_cell == 'X':
            break
        current_row += directions[direction][0]
        current_col += directions[direction][1]

    if current_sum > best_sum:
        best_sum = current_sum
        best_direction = direction
        best_path = current_path

print(best_direction)
[print(cell) for cell in best_path]
print(best_sum)
