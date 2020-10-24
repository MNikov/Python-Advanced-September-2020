from collections import deque


def filter_color(colors):
    for color in colors:
        if color == 'orange':
            if 'red' not in colors or 'yellow' not in colors:
                colors.remove(color)
        if color == 'purple':
            if 'red' not in colors or 'blue' not in colors:
                colors.remove(color)
        if color == 'green':
            if 'blue' not in colors or 'yellow' not in colors:
                colors.remove(color)
    return colors


pieces = deque(input().split())
main_colors = ('red', 'yellow', 'blue')
secondary_colors = ('orange', 'purple', 'green')
all_colors = main_colors + secondary_colors
colors_found = []

while pieces:
    left_piece = pieces.popleft()
    right_piece = ''
    if pieces:
        right_piece = pieces.pop()
    current_color = left_piece + right_piece
    current_color_flipped = right_piece + left_piece
    if current_color in all_colors:
        colors_found.append(current_color)
    elif current_color_flipped in all_colors:
        colors_found.append(current_color_flipped)
    else:
        if left_piece[:-1] != '':
            pieces.insert(len(pieces) // 2, left_piece[:-1])
        if right_piece[:-1] != '':
            pieces.insert(len(pieces) // 2, right_piece[:-1])

print(filter_color(colors_found))
