def create_field(size):
    return [input().split() for _ in range(size)]


def valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


def find_plane(size, matrix):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'p':
                return r, c


def count_targets(size, matrix):
    count = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 't':
                count += 1
    return count


size = int(input())
field = create_field(size)
commands_count = int(input())
plane_row, plane_col = find_plane(size, field)
targets_count = count_targets(size, field)
targets_destroyed = 0
dirs = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}

for _ in range(commands_count):
    command, dir, steps = input().split()
    steps = int(steps)

    if dir == 'up':
        next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps
    elif dir == 'down':
        next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps
    elif dir == 'left':
        next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps
    else:
        next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps

    if command == 'move':
        if valid_cell(next_row, next_col, size):
            if field[next_row][next_col] == '.':
                field[next_row][next_col] = 'p'
                field[plane_row][plane_col] = '.'
                plane_row, plane_col = next_row, next_col

    elif command == 'shoot':
        if valid_cell(next_row, next_col, size):
            if field[next_row][next_col] == 't':
                targets_destroyed += 1
            field[next_row][next_col] = 'x'
        if targets_destroyed == targets_count:
            print(f"Mission accomplished! All {targets_count} targets destroyed.")
            break

if targets_destroyed < targets_count:
    print(f"Mission failed! {targets_count - targets_destroyed} targets left.")

[print(' '.join(row)) for row in field]
