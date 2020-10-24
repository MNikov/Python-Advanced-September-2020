def create_field(size):
    return [input().split() for _ in range(size)]


def check_valid_cell(row, col, size):
    return 0 <= row < size and 0 <= col < size


def find_santa(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'S':
                return r, c


def find_nice_kids(matrix):
    nice_kids = 0
    for row in matrix:
        nice_kids += row.count('V')
    return nice_kids


presents_count = int(input())
size = int(input())
field = create_field(size)
santa_r, santa_c = find_santa(field, size)
nice_kids_count = find_nice_kids(field)
starting_nice_kids_count = nice_kids_count
dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
is_out_of_presents = False

while True:
    if is_out_of_presents:
        break
    dir = input()
    if dir == 'Christmas morning':
        break
    next_r = santa_r + dirs[dir][0]
    next_c = santa_c + dirs[dir][1]
    if field[next_r][next_c] == 'V':
        nice_kids_count -= 1
        presents_count -= 1
        field[next_r][next_c] = 'S'
        field[santa_r][santa_c] = '-'
        santa_r, santa_c = next_r, next_c
        if nice_kids_count == 0 or presents_count == 0:
            break
    elif field[next_r][next_c] == 'X':
        field[next_r][next_c] = 'S'
        field[santa_r][santa_c] = '-'
        santa_r, santa_c = next_r, next_c
    elif field[next_r][next_c] == '-':
        field[next_r][next_c] = 'S'
        field[santa_r][santa_c] = '-'
        santa_r, santa_c = next_r, next_c
    elif field[next_r][next_c] == 'C':
        field[next_r][next_c] = 'S'
        field[santa_r][santa_c] = '-'
        santa_r, santa_c = next_r, next_c
        for r, c in dirs.values():
            current_r, current_c = santa_r + r, santa_c + c
            if check_valid_cell(current_r, current_c, size):
                if field[current_r][current_c] in ('V', 'X'):
                    presents_count -= 1
                    if field[current_r][current_c] == 'V':
                        nice_kids_count -= 1
                    if presents_count == 0:
                        is_out_of_presents = True
                    field[current_r][current_c] = '-'

if presents_count == 0 and nice_kids_count > 0:
    print("Santa ran out of presents!")

[print(' '.join(row)) for row in field]

if nice_kids_count == 0:
    print(f"Good job, Santa! {starting_nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")
