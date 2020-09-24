from collections import deque


def move(position, command, rows, cols, lair):
    x_player, y_player = position
    x_increment, y_increment = command
    x_player_new, y_player_new = x_player + x_increment, y_player + y_increment
    return (x_player, y_player), (x_player_new, y_player_new)


def recalculate_lair(lair, rows, cols, commands_possible):  # bunnies multiply according to rules
    for i in range(rows):
        for j in range(cols):
            if lair[i][j] == "B":
                for command, x_y_increments in commands_possible.items():
                    x_increment, y_increment = x_y_increments
                    new_i, new_j = i + x_increment, j + y_increment
                    is_xy_valid = 0 <= new_i < rows and 0 <= new_j < cols
                    if is_xy_valid and lair[new_i][new_j] != "B":
                        lair[new_i][new_j] = "b"
    for i in range(rows):
        for j in range(cols):
            if lair[i][j] == "b":
                lair[i][j] = "B"
    return lair


def evaluate_position(position, rows, cols, lair):  # evaluate player position
    x_player, y_player = position
    is_player_in_lair = 0 <= x_player < rows and 0 <= y_player < cols

    if is_player_in_lair:
        is_player_alive = lair[x_player][y_player] == "."
        if is_player_alive:
            return "alive"
        else:
            return "dead"
    else:
        return "won"


def lair_string_constructor(lair, rows):
    lair_string = ""
    for i in range(rows):
        lair_string += "".join(lair[i])
        if i < rows - 1:
            lair_string += "\n"
    return lair_string


rows, cols = map(int, input().split())  # get lair dimensions
lair = [[cell for cell in list(input())] for _ in range(rows)]  # construct lair from input

commands_possible = {
    "U": (-1, +0),
    "D": (+1, +0),
    "L": (+0, -1),
    "R": (+0, +1)
}
commands = deque((commands_possible[command] for command in
                  list(input())))  # store commands as coordinate increment tuples in a deque

current_position_player = None
for i in range(rows):  # find player position in lair
    for j in range(cols):
        if lair[i][j] == "P":
            current_position_player = (i, j)
            lair[i][j] = "."
            break
    if current_position_player:
        break

while commands:
    command_current = commands.popleft()  # fetch current command
    old_position_player, current_position_player = move(current_position_player, command_current, rows, cols,
                                                        lair)  # execute player move, get old and new position
    condition_player = evaluate_position(current_position_player, rows, cols,
                                         lair)  # evaluate position after player move
    lair = recalculate_lair(lair, rows, cols, commands_possible)  # bunnies multiply
    if condition_player == "dead":
        print(lair_string_constructor(lair, rows))
        print(f"{condition_player}: {current_position_player[0]} {current_position_player[1]}")
        break
    elif condition_player == "won":
        print(lair_string_constructor(lair, rows))
        print(f"{condition_player}: {old_position_player[0]} {old_position_player[1]}")
        break
    elif condition_player == "alive":
        condition_player = evaluate_position(current_position_player, rows, cols,
                                             lair)  # player condition after bunny multiplication
        if condition_player == "dead":  # can only be "alive" or "dead"
            print(lair_string_constructor(lair, rows))
            print(f"{condition_player}: {current_position_player[0]} {current_position_player[1]}")
            break
