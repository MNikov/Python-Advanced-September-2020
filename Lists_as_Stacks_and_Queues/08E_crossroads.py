from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
is_crashed = False
total_cars = 0

while True:
    line = input()
    if line == 'END':
        break

    if line == 'green':
        if cars:
            green = green_light
            car_name = cars.popleft()
            current_car = deque(car_name)
            while green > 0:
                if not current_car:
                    if cars:
                        car_name = cars.popleft()
                        current_car = deque(car_name)
                    else:
                        break
                current_car.popleft()
                green -= 1
            if current_car:
                yellow = free_window
                while free_window and current_car:
                    current_car.popleft()
                    free_window -= 1
            if current_car:
                print("A crash happened!\n"f"{car_name} was hit at {current_car.popleft()}.")
                is_crashed = True
                break
    else:
        total_cars += 1
        cars.append(line)

if not is_crashed:
    print("Everyone is safe.\n"f'{total_cars - len(cars)} total cars passed the crossroads.')
