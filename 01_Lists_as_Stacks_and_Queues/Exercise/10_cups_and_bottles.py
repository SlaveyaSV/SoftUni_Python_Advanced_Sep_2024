from collections import deque

cups = deque(list(map(int, input().split())))
bottles = list(map(int, input().split()))

wasted_water = 0

while bottles and cups:
    current_cup = cups.popleft()

    while bottles:
        current_cup -= bottles.pop()
        if current_cup <= 0:
            wasted_water += abs(current_cup)
            break

if cups:
    print(f"Cups: {' '.join(list(map(str, cups)))}")
else:
    print(f"Bottles: {' '.join(list(map(str, bottles)))}")

print(f"Wasted litters of water: {wasted_water}")
