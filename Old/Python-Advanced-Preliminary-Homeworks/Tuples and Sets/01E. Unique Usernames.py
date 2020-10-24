def collect_names(number):
    names = set()
    for _ in range(number):
        name = input()
        names.add(name)
    return names


def print_result(names):
    [print(n) for n in names]


print_result(collect_names(int(input())))