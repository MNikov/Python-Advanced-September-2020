from collections import deque

customer_times = deque([int(x) for x in input().split(', ')])
taxi_times = [int(x) for x in input().split(', ')]
total_time = 0

while True:
    if len(customer_times) == 0:
        print('All customers were driven to their destinations')
        print(f'Total time: {total_time} minutes')
        break
    elif len(customer_times) > 0 and len(taxi_times) == 0:
        print('Not all customers were driven to their destinations')
        print(f'Customers left: {", ".join([str(x) for x in customer_times])}')
        break
    current_driver = taxi_times.pop()
    current_customer = customer_times.popleft()
    if current_driver >= current_customer:
        total_time += current_customer
    else:
        customer_times.appendleft(current_customer)

