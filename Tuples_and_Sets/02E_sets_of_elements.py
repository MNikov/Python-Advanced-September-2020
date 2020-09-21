n, m = [int(x) for x in input().split()]
counter = 0
n_set = set()
m_set = set()

for _ in range(n + m):
    counter += 1
    num = input()
    if counter > n:
        n_set.add(num)
    else:
        m_set.add(num)

intersection = n_set.intersection(m_set)
print('\n'.join(intersection))
