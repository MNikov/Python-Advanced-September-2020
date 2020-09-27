def create_even_matrix():
    return [[int(x) for x in input().split(', ') if int(x) % 2 == 0] for _ in range(int(input()))]


print(create_even_matrix())
