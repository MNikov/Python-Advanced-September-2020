def fill_table(number):
    periodic_table = set()
    for _ in range(number):
        elements = input().split()
        for element in elements:
            periodic_table.add(element)
    # another approach is to cast the elements to set and use the union method (periodic_table | elements or periodic_table |= elements or .union)
    return periodic_table


def print_table(table):
    [print(e) for e in table]


print_table(fill_table(int(input())))