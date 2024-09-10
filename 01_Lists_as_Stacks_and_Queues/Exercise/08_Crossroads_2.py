from collections import deque

green_light = int(input())
free_window = int(input())
cars_queue = deque()
total_cars_passed = 0
command = input()

while command != "END":
    if command != "green":
        cars_queue.append(command)
    else:
        green_seconds_left = green_light

        while green_seconds_left > 0 and cars_queue:
            current_car = cars_queue.popleft()

            total_time = green_seconds_left + free_window

            if len(current_car) > total_time:
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[total_time]}.")
                raise SystemExit

            green_seconds_left -= len(current_car)
            total_cars_passed += 1

    command = input()

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")
