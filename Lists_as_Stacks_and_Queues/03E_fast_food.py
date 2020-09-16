from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
is_done = True
print(max(orders))

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)
        print(f'Orders left: {" ".join([str(x) for x in orders])}')
        is_done = False
        break

if is_done:
    print('Orders complete')
