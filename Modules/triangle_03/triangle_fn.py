def draw_triangle(height):
    for n in range(height):
        print(" ".join([str(x) for x in range(1, n + 2)]))
    for n in range(height - 1, 0, -1):
        print(" ".join([str(x) for x in range(1, n + 1)]))

# def draw_triangle(size):
#     for i in range(1, size + 1):
#         for j in range(1, i + 1):
#             print(j, end=' ')
#         print('\r')
#
#     for k in range(size - 1, 0, -1):
#         for l in range(k, 0, -1):
#             print(l, end=' ')
#         print('\r')
