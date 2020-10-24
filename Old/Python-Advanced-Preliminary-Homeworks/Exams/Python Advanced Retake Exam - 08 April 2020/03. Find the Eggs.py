def find_strongest_eggs(*args):
    eggs = args[0]
    n = int(args[1])
    sublists = [[] for _ in range(n)]
    strongest_eggs = []
    counter = 0

    for egg in eggs:
        if counter == n:
            counter = 0
        sublists[counter].append(egg)
        counter += 1

    for sublist in sublists:
        mid = len(sublist) // 2
        condition_one = sublist[mid] > sublist[mid - 1] and sublist[mid] > sublist[mid + 1]
        condition_two = sublist[mid + 1] > sublist[mid - 1]
        if condition_one and condition_two:
            strongest_eggs.append(sublist[mid])

    return strongest_eggs


test = ([-1, 7, 3, 15, 2, 12], 2)
print(find_strongest_eggs(*test))

test = ([-1, 0, 2, 5, 2, 3], 2)
print(find_strongest_eggs(*test))

test = ([51, 21, 83, 52, 55], 1)
print(find_strongest_eggs(*test))
