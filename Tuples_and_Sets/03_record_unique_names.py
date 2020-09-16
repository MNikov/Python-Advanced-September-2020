def extract_unique_names(n):
    names = set()
    for _ in range(n):
        name = input()
        names.add(name)
    [print(n) for n in names]


extract_unique_names(int(input()))
