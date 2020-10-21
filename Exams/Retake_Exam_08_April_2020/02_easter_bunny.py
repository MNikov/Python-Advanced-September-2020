from sys import maxsize


def find_bunny(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                return r, c


def check_valid_cell(size, r, c):
    return 0 <= r < size and 0 <= c < size


deltas = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
size = int(input())
field = [input().split() for _ in range(size)]
br, bc = find_bunny(field, size)
best_dir = ''
best_coord = []
best_sum = -maxsize

for dir in deltas:
    curr_sum = 0
    coord = []
    next_r, next_c = br + deltas[dir][0], bc + deltas[dir][1]
    if not check_valid_cell(size, next_r, next_c):
        continue
    while check_valid_cell(size, next_r, next_c):
        if field[next_r][next_c] == 'X':
            break
        curr_sum += int(field[next_r][next_c])
        coord.append([next_r, next_c])
        next_r, next_c = next_r + deltas[dir][0], next_c + deltas[dir][1]
    if curr_sum > best_sum:
        best_sum = curr_sum
        best_dir = dir
        best_coord = coord

print(best_dir)
for l in best_coord:
    print(l)
print(best_sum)
