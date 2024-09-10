from collections import deque

pumps_count = int(input())
pumps = deque()


for _ in range(pumps_count):
    pumps.append(list(map(int, input().split())))

for attempt in range(pumps_count):
    fuel_in_tank = 0
    attempt_failed = False

    for fuel, distance in pumps:
        fuel_in_tank += (fuel - distance)
        if fuel_in_tank < 0:
            attempt_failed = True
            break

    if attempt_failed:
        pumps.rotate(-1)
    else:
        print(attempt)
        break
