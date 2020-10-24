def get_all_queens(matrix):
    queens_coordinates = []
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            if matrix[r][c] == 'Q':
                queens_coordinates.append((r, c))
    return queens_coordinates


def check_valid_cell(matrix, r, c):
    return 0 <= r < len(matrix) and 0 <= c < len(matrix)


board = [input().split() for _ in range(8)]
queens_coordinates = get_all_queens(board)
deltas = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1), 'upleft': (-1, -1),
          'upright': (-1, 1), 'downleft': (1, -1), 'downright': (1, 1)}
killing_queens = []

for coord in queens_coordinates:
    qr, qc = coord
    for dir in deltas:
        next_r, next_c = qr + deltas[dir][0], qc + deltas[dir][1]
        if not check_valid_cell(board, next_r, next_c):
            continue
        while check_valid_cell(board, next_r, next_c):
            if board[next_r][next_c] == 'Q':
                break
            elif board[next_r][next_c] == 'K':
                killing_queens.append([qr, qc])
                break
            next_r, next_c = next_r + deltas[dir][0], next_c + deltas[dir][1]

if killing_queens:
    for c in killing_queens:
        print(c)
else:
    print('The king is safe!')
