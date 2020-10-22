def get_magic_triangle(n):
    results = []  # a container to collect the rows
    for _ in range(n):
        row = [1]  # a starter 1 in the row
        if results:  # then we're in the second row or beyond
            last_row = results[-1]  # reference the previous row
            # this is the complicated part, it relies on the fact that zip
            # stops at the shortest iterable, so for the second row, we have
            # nothing in this list comprension, but the third row sums 1 and 1
            # and the fourth row sums in pairs. It's a sliding window.
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            # finally append the final 1 to the outside
            row.append(1)
        results.append(row)  # add the row to the results.
    return results


get_magic_triangle(5)

# def get_magic_triangle(rows):
#     triangle = [[1] * i for i in range(1, rows + 1)]
#     for row in range(2, rows):
#         for col in range(1, row):
#             triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]
#     return triangle

# def get_magic_triangle(n:int):
#     list = []
#     number = 0
#     for i in range(n):
#         number = 0
#         transition_list = []
#         if len(list) == 0:
#             list.append([i+1])
#         elif i == 1:
#                 number = list[0][0]
#                 transition_list.append(number)
#                 nummber = list[0][0]
#                 transition_list.append(number)
#                 list.append(transition_list)
#         else:
#             for ix in range(i+1):
#                 if ix == 0 or ix == i:
#                     transition_list.append(1)
#                 else:
#                     number = list[i-1][ix-1] + list[i-1][ix]
#                     transition_list.append(number)
#             list.append(transition_list)
#     return list
#
#
# print(get_magic_triangle(7))


# def get_magic_triangle(level):
#     triangle = [[] for _ in range(level)]
#     for i in range(0, level):
#         for j in range(0, i + 1):
#             if j == 0 or j == i:
#                 triangle[i].append(1)
#             else:
#                 triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
#     return triangle
