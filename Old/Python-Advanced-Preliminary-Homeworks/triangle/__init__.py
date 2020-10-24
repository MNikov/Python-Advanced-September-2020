def draw_triangle(height):
    for n in range(height):
        print(" ".join([str(x) for x in range(1, n + 2)]))
    for n in range(height - 1, 0, -1):
        print(" ".join([str(x) for x in range(1, n + 1)]))
