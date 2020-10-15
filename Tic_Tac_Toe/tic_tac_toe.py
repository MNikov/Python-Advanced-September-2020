def get_player_info():
    p_1['name'] = input('Player one name: ')
    p_2['name'] = input('Player two name: ')
    while p_1['symbol'] not in ('X', 'O'):
        p_1['symbol'] = input(f"{p_1['name']} choose 'X' or 'O': ")
    p_2['symbol'] = 'O' if p_1['symbol'] == 'X' else 'X'


def show_rules():
    print('This is the board numeration: ')
    print('| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |')


def play():
    pos = int(input(f'{current_p["name"]} choose a free position [1-9]: '))
    while pos not in pos_dict or board[pos_dict[pos][0]][pos_dict[pos][1]] != ' ':
        pos = int(input(f'{current_p["name"]} choose a free position [1-9]: '))
    r, c = pos_dict[pos]
    board[r][c] = current_p['symbol']


def switch_players():
    return p_1 if current_p == p_2 else p_2


def check_for_win(symbol):
    for row in board:
        if row.count(symbol) == 3:
            return True
    for col in range(3):
        if all(board[i][col] == symbol for i in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def check_for_tie():
    return not any(" " in row for row in board)


def print_board():
    for row in board:
        print('| ' + ' | '.join([str(x) for x in row]) + ' |')


pos_dict = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
p_1 = {'name': '', 'symbol': ''}
p_2 = {'name': '', 'symbol': ''}
get_player_info()
show_rules()
current_p = p_1

while True:
    play()
    print_board()
    if check_for_win(current_p['symbol']):
        print(f"{current_p['name']} won!")
        break
    if check_for_tie():
        print("Tie!")
        break
    current_p = switch_players()
