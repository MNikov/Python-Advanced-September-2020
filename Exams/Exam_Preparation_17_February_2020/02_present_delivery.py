def find_santa(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'S':
                return r, c


def count_good_kids(matrix, size):
    count = 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'V':
                count += 1
    return count


def check_valid_cell(size, r, c):
    return 0 <= r < size and 0 <= c < size


presents = int(input())
size = int(input())
field = [input().split() for _ in range(size)]
sr, sc = find_santa(field, size)
good_kids = count_good_kids(field, size)
good_kids_starting_count = good_kids

deltas = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while presents > 0:
    dir = input()
    if dir == 'Christmas morning':
        break
    next_r, next_c = sr + deltas[dir][0], sc + deltas[dir][1]
    if check_valid_cell(size, next_r, next_c):
        if field[next_r][next_c] == 'V':
            field[sr][sc] = '-'
            field[next_r][next_c] = 'S'
            presents -= 1
            good_kids -= 1
            sr, sc = next_r, next_c
            if presents == 0 and good_kids > 0:
                print('Santa ran out of presents!')
                break
        elif field[next_r][next_c] == 'X' or field[next_r][next_c] == '-':
            field[sr][sc] = '-'
            field[next_r][next_c] = 'S'
            sr, sc = next_r, next_c
        elif field[next_r][next_r] == 'C':
            field[sr][sc] = '-'
            field[next_r][next_c] = 'S'
            sr, sc = next_r, next_c
            rows = [-1, 0, 1, 0]
            cols = [0, 1, 0, -1]
            for i in range(4):
                row, col = sr + rows[i], sc + cols[i]
                if check_valid_cell(size, row, col):
                    if field[row][col] == 'V' or field[row][col] == 'X':
                        if field[row][col] == 'V':
                            good_kids -= 1
                        field[row][col] = '-'
                        presents -= 1

                        if presents == 0 and good_kids > 0:
                            print('Santa ran out of presents!')
                            break

for row in field:
    print(' '.join(row))

if good_kids <= 0:
    print(f"Good job, Santa! {good_kids_starting_count} happy nice kid/s.")
else:
    print(f"No presents for {good_kids} nice kid/s.")

# def create_neighbourhood(size):
#     return [input().split() for _ in range(size)]
#
#
# def check_valid_cell(row, col, size):
#     return 0 <= row < size and 0 <= col < size
#
#
# def find_santa(matrix, size):
#     for r in range(size):
#         for c in range(size):
#             if matrix[r][c] == 'S':
#                 return r, c
#
#
# def find_nice_kids(matrix):
#     nice_kids = 0
#     for row in matrix:
#         nice_kids += row.count('V')
#     return nice_kids
#
#
# presents_count = int(input())
# neighbourhood_size = int(input())
# neighbourhood = create_neighbourhood(neighbourhood_size)
# santa_row, santa_col = find_santa(neighbourhood, neighbourhood_size)
# nice_kids_count = find_nice_kids(neighbourhood)
# starting_nice_kids_count = nice_kids_count
# dirs = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
# is_out_of_presents = False
#
# while True:
#     if is_out_of_presents:
#         break
#     dir = input()
#     if dir == 'Christmas morning':
#         break
#     next_row = santa_row + dirs[dir][0]
#     next_col = santa_col + dirs[dir][1]
#     if neighbourhood[next_row][next_col] == 'V':
#         nice_kids_count -= 1
#         presents_count -= 1
#         neighbourhood[next_row][next_col] = 'S'
#         neighbourhood[santa_row][santa_col] = '-'
#         santa_row, santa_col = next_row, next_col
#         if nice_kids_count == 0 or presents_count == 0:
#             break
#     elif neighbourhood[next_row][next_col] == 'X':
#         neighbourhood[next_row][next_col] = 'S'
#         neighbourhood[santa_row][santa_col] = '-'
#         santa_row, santa_col = next_row, next_col
#     elif neighbourhood[next_row][next_col] == '-':
#         neighbourhood[next_row][next_col] = 'S'
#         neighbourhood[santa_row][santa_col] = '-'
#         santa_row, santa_col = next_row, next_col
#     elif neighbourhood[next_row][next_col] == 'C':
#         neighbourhood[next_row][next_col] = 'S'
#         neighbourhood[santa_row][santa_col] = '-'
#         santa_row, santa_col = next_row, next_col
#         for r, c in dirs.values():
#             current_row, current_col = santa_row + r, santa_col + c
#             if check_valid_cell(current_row, current_col, neighbourhood_size):
#                 if neighbourhood[current_row][current_col] in ('V', 'X'):
#                     presents_count -= 1
#                     if neighbourhood[current_row][current_col] == 'V':
#                         nice_kids_count -= 1
#                     if presents_count == 0:
#                         is_out_of_presents = True
#                     neighbourhood[current_row][current_col] = '-'
#
# if presents_count == 0 and nice_kids_count > 0:
#     print("Santa ran out of presents!")
#
# [print(' '.join(row)) for row in neighbourhood]
#
# if nice_kids_count == 0:
#     print(f"Good job, Santa! {starting_nice_kids_count} happy nice kid/s.")
# else:
#     print(f"No presents for {nice_kids_count} nice kid/s.")
