def collect_names(n):
    names = set()
    for _ in range(n):
        name = input()
        names.add(name)
    return names


def print_set(names):
    [print(n) for n in names]


print_set(collect_names(int(input())))