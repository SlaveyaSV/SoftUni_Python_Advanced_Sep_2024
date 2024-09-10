from collections import deque


def cars_entering_crossroad(green_light_duration, cars_in_queue, entered_cars):
    green_seconds_left = green_light_duration
    while green_seconds_left > 0:
        if cars_in_queue:
            current_car = cars_in_queue.popleft()
        else:
            break
        entered_cars.append(current_car)
        green_seconds_left -= len(current_car)
    return entered_cars


def cars_exiting_crossroad(entered_cars, green_light_duration, free_window_duration, total_cars):
    total_time = green_light_duration + free_window_duration
    is_crash = False

    for car in entered_cars.copy():
        for char in car:
            if total_time == 0:
                is_crash = True
                print("A crash happened!")
                print(f"{car} was hit at {char}.")
                break
            else:
                total_time -= 1
        if is_crash:
            break
        else:
            total_cars.append(entered_cars.popleft())
    return is_crash


green_light = int(input())
free_window = int(input())

cars_queue = deque()
cars_in_crossroad = deque()
total_cars_passed = []

while True:
    command = input()

    if command == "END":
        print("Everyone is safe.")
        print(f"{len(total_cars_passed)} total cars passed the crossroads.")
        break

    if command != "green":
        cars_queue.append(command)
    else:
        cars_entering_crossroad(green_light, cars_queue, cars_in_crossroad)

        if cars_exiting_crossroad(cars_in_crossroad, green_light, free_window, total_cars_passed):
            break
