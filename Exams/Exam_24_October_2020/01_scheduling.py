jobs = [int(x) for x in input().split(', ')]
idx = int(input())
cycles = 0

while True:
    min_index = jobs.index(min(jobs))
    cycles += jobs.pop(min_index)
    if min_index == idx:
        print(cycles)
        break
    elif min_index < idx:
        idx -= 1
    elif min_index > idx:
        continue
