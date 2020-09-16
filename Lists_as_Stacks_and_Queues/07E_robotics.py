from collections import deque


def rotate_clock(h, m, s):
    s += 1
    if s == 60:
        s = 0
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    return h, m, s


robots = input().split(';')
h, m, s = [int(x) for x in input().split(':')]
available_robots = deque([[r.split('-')[0], int(r.split('-')[1])] for r in robots])
working_robots = deque()
robots_dict = {r[0]: r[1] for r in available_robots}
products = deque()

while True:
    product = input()
    if product == 'End':
        break
    products.append(product)

while products:
    h, m, s = rotate_clock(h, m, s)
    product = products.popleft()
    if not available_robots:
        products.append(product)
    else:
        if available_robots:
            robot = available_robots.popleft()
            working_robots.append(robot)
            print(f'{robot[0]} - {product} [{h:02d}:{m:02d}:{s:02d}]')

    for robot in working_robots:
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([robot[0], robots_dict[robot[0]]])
    working_robots = [r for r in working_robots if r[1] > 0]
