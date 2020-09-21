def create_periodic_table(n):
    table = set()
    for _ in range(n):
        elements = input().split()
        for el in elements:
            table.add(el)
    return table


periodic_table = create_periodic_table(int(input()))
print('\n'.join(periodic_table))
