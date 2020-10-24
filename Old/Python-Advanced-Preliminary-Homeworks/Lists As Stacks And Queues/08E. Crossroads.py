# РЕШЕНИЕ ОТ УПРАЖНЕНИЕТО ОТ ПРЕДНИЯ МОДУЛ
from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()
total_cars = 0
is_crashed = False

while True:
    line = input()
    if line == 'END':
        print("Everyone is safe.")
        print(f"{total_cars - len(cars)} total cars passed the crossroads.")
        break
    if line == 'green':
        if cars:
            car_name = cars.popleft()
            current_car = deque(car_name)
            green_light = green_light_duration
            while green_light:
                if not current_car:
                    if cars:
                        car_name = cars.popleft()
                        current_car = deque(car_name)
                    else:
                        break
                current_car.popleft()
                green_light -= 1
            if current_car:
                free_window = free_window_duration
                while free_window and current_car:
                    current_car.popleft()
                    free_window -= 1
            if current_car:
                is_crashed = True
                print("A crash happened!")
                print(f"{car_name} was hit at {current_car.popleft()}.")
                break
    else:
        cars.append(line)
        total_cars += 1

