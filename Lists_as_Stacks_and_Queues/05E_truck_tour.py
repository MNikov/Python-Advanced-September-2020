from collections import deque


def find_start(number):
    pumps = deque()

    for _ in range(number):
        fuel, distance = input().split()
        fuel = int(fuel)
        distance = int(distance)
        pumps.append([fuel, distance])

    for i in range(number):
        is_success = True
        total_fuel = 0
        for _ in range(number):
            current_fuel, current_distance = pumps.popleft()
            total_fuel += current_fuel - current_distance
            if total_fuel < 0:
                is_success = False
            pumps.append([current_fuel, current_distance])

        if is_success:
            print(i)
            break

        pumps.append(pumps.popleft())


find_start(int(input()))
