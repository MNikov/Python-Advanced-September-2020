def create_matrix(size):
    return [[x for x in input()] for _ in range(size)]


def find_the_snake(matrix, size):
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'S':
                return r, c


def find_the_burrows(matrix, size):
    burrows = []
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == 'B':
                burrows.append((r, c))
    return burrows


def is_in_territory(row, col, size):
    return 0 <= row < size and 0 <= col < size


def print_matrix(matrix):
    return [print(''.join(row)) for row in matrix]


size = int(input())
field = create_matrix(size)
snake_row, snake_col = find_the_snake(field, size)
burrows_coordinates = find_the_burrows(field, size)
food_collected = 0
while True:
    command = input()
    if command == 'left':
        next_row, next_col = snake_row, snake_col - 1
    elif command == 'right':
        next_row, next_col = snake_row, snake_col + 1
    elif command == 'up':
        next_row, next_col = snake_row - 1, snake_col
    elif command == 'down':
        next_row, next_col = snake_row + 1, snake_col
    if not is_in_territory(next_row, next_col, size):
        field[snake_row][snake_col] = '.'
        print('Game over!')
        break
    else:
        field[snake_row][snake_col] = '.'
    if field[next_row][next_col] == '-':
        field[next_row][next_col] = 'S'
        snake_row, snake_col = next_row, next_col
    elif field[next_row][next_col] == '*':
        food_collected += 1
        field[next_row][next_col] = 'S'
        if food_collected == 10:
            print("You won! You fed the snake.")
            break
        snake_row, snake_col = next_row, next_col
    elif field[next_row][next_col] == 'B':
        field[next_row][next_col] = '.'
        burrows_coordinates.remove((next_row, next_col))
        next_row = burrows_coordinates[0][0]
        next_col = burrows_coordinates[0][1]
        field[next_row][next_col] = 'S'
        snake_row, snake_col = next_row, next_col


print(f'Food eaten: {food_collected}')
print_matrix(field)
