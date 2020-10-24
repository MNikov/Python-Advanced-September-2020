from collections import deque


def solution(food_quantity, sequence):
    orders = deque(sequence)
    print(max(orders))
    is_done = True
    while orders:
        order = orders.popleft()
        if food_quantity >= order:
            food_quantity -= order
        else:
            orders.appendleft(order)
            is_done = False
            print(f'Orders left: {" ".join([str(o) for o in orders])}')
            break

    if is_done:
        print('Orders complete')


quantity = int(input())
orders_list = [int(n) for n in input().split()]
solution(quantity, orders_list)
