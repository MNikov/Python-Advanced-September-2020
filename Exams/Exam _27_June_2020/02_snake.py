def find_symbol_in_matrix(matrix, symbol, n):
    for r in range(n):
        for c in range(n):
            if matrix[r][c] == symbol:
                return r, c


def check_valid_cell(n, r, c):
    return 0 <= r < n and 0 <= c < n


def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))


size = int(input())
field = [list(input()) for _ in range(size)]
snake_r, snake_c = find_symbol_in_matrix(field, 'S', size)
food_eaten = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    dir = input()
    next_r, next_c = snake_r + directions[dir][0], snake_c + directions[dir][1]

    if check_valid_cell(size, next_r, next_c):
        field[snake_r][snake_c] = '.'
        if field[next_r][next_c] == '*':
            field[next_r][next_c] = 'S'
            food_eaten += 1
            if food_eaten == 10:
                print('You won! You fed the snake.')
                break
            snake_r, snake_c = next_r, next_c
        elif field[next_r][next_c] == '-':
            field[next_r][next_c] = 'S'
            snake_r, snake_c = next_r, next_c
        elif field[next_r][next_c] == 'B':
            field[next_r][next_c] = '.'
            new_r, new_c = find_symbol_in_matrix(field, 'B', size)
            snake_r, snake_c = new_r, new_c
            field[snake_r][snake_c] = 'S'

    else:
        field[snake_r][snake_c] = '.'
        print('Game over!')
        break

print(f'Food eaten: {food_eaten}')
print_matrix(field)
