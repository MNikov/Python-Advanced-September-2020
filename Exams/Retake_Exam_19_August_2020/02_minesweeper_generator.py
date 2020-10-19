def create_field(n):
    matrix = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        matrix.append(row)
    return matrix


def check_valid_cell(r, c, size):
    return 0 <= r < size and 0 <= c < size


def increase_cells(r, c):
    rows = [-1, -1, 0, 1, 1, 1, 0, -1]
    cols = [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(8):
        next_r, next_c = r + rows[i], c + cols[i]
        if check_valid_cell(next_r, next_c, size) and field[next_r][next_c] != '*':
            field[next_r][next_c] += 1


def print_field():
    for row in field:
        print(' '.join([str(x) for x in row]))


size = int(input())
bombs_count = int(input())
field = create_field(size)
for _ in range(bombs_count):
    tokens = input()[1:-1].split(', ')
    br = int(tokens[0])
    bc = int(tokens[1])
    if check_valid_cell(br, bc, size):
        field[br][bc] = '*'
        increase_cells(br, bc)

print_field()
