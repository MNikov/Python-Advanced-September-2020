def get_magic_triangle(n):
    wanted_triangle = [[1] * count for count in range(1, n + 1)]
    for row in range(2, n):
        for column in range(1, row):
            wanted_triangle[row][column] = \
                wanted_triangle[row - 1][column] + wanted_triangle[row - 1][column - 1]
    return wanted_triangle


print(get_magic_triangle(5))
