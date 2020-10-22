def find_plane(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'p':
                return r, c


def check_valid_cell(size, r, c):
    return 0 <= r < size and 0 <= c < size


def get_all_targets(matrix, size):
    count = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 't':
                count += 1
    return count


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))


size = int(input())
field = [input().split() for _ in range(size)]
pr, pc = find_plane(field, size)
targets_count = get_all_targets(field, size)
targets_shot = 0
commands_count = int(input())

for _ in range(commands_count):
    command, dir, steps = input().split()
    steps = int(steps)
    if command == 'move':
        old_r, old_c = pr, pc
        if dir == 'up':
            pr -= steps
        elif dir == 'down':
            pr += steps
        elif dir == 'left':
            pc -= steps
        else:
            pc += steps
        if check_valid_cell(size, pr, pc):
            if field[pr][pc] == '.':
                field[old_r][old_c] = '.'
                field[pr][pc] = 'p'
            else:
                pr, pc = old_r, old_c
        else:
            pr, pc = old_r, old_c
    elif command == 'shoot':
        r_to_shoot = pr
        c_to_shoot = pc
        if dir == 'up':
            r_to_shoot -= steps
        elif dir == 'down':
            r_to_shoot += steps
        elif dir == 'left':
            c_to_shoot -= steps
        else:
            c_to_shoot += steps
        if check_valid_cell(size, r_to_shoot, c_to_shoot):
            if field[r_to_shoot][c_to_shoot] == 't':
                targets_shot += 1
            field[r_to_shoot][c_to_shoot] = 'x'
            if targets_shot == targets_count:
                print(f'Mission accomplished! All {targets_count} targets destroyed.')
                break

if targets_shot < targets_count:
    print(f'Mission failed! {targets_count - targets_shot} targets left.')
print_matrix(field)

# def create_field(size):
#     return [input().split() for _ in range(size)]
#
#
# def valid_cell(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
#
# def find_plane(size, matrix):
#     for r in range(size):
#         for c in range(size):
#             if matrix[r][c] == 'p':
#                 return r, c
#
#
# def count_targets(size, matrix):
#     count = 0
#     for r in range(size):
#         for c in range(size):
#             if matrix[r][c] == 't':
#                 count += 1
#     return count
#
#
# size = int(input())
# field = create_field(size)
# commands_count = int(input())
# plane_row, plane_col = find_plane(size, field)
# targets_count = count_targets(size, field)
# targets_destroyed = 0
# dirs = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
#
# for _ in range(commands_count):
#     command, dir, steps = input().split()
#     steps = int(steps)
#
#     if dir == 'up':
#         next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps
#     elif dir == 'down':
#         next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps
#     elif dir == 'left':
#         next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps
#     else:
#         next_row, next_col = plane_row + dirs[dir][0] * steps, plane_col + dirs[dir][1] * steps
#
#     if command == 'move':
#         if valid_cell(next_row, next_col, size):
#             if field[next_row][next_col] == '.':
#                 field[next_row][next_col] = 'p'
#                 field[plane_row][plane_col] = '.'
#                 plane_row, plane_col = next_row, next_col
#
#     elif command == 'shoot':
#         if valid_cell(next_row, next_col, size):
#             if field[next_row][next_col] == 't':
#                 targets_destroyed += 1
#             field[next_row][next_col] = 'x'
#         if targets_destroyed == targets_count:
#             print(f"Mission accomplished! All {targets_count} targets destroyed.")
#             break
#
# if targets_destroyed < targets_count:
#     print(f"Mission failed! {targets_count - targets_destroyed} targets left.")
#
# [print(' '.join(row)) for row in field]
