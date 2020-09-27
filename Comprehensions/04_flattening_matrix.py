from itertools import chain


def flatten_matrix(matrix):
    return list(chain(*matrix))


print(flatten_matrix([[int(x) for x in input().split(', ')] for _ in range(int(input()))]))
