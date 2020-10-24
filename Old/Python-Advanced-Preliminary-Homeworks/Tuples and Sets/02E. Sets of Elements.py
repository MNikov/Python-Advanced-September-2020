def fill_sets(n, m):
    n_set = set()
    m_set = set()
    counter = 1
    for _ in range(n + m):
        number = int(input())
        if counter <= n:
            n_set.add(number)
        else:
            m_set.add(number)
        counter += 1
    return n_set.intersection(m_set)


def print_result(result_set):
    [print(i) for i in result_set]


n, m = [int(i) for i in input().split()]
print_result(fill_sets(n, m))
