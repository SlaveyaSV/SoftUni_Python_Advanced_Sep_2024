from collections import deque

water_quantity = int(input())
queue = deque()

while True:
    people = input()

    if people == "Start":
        break

    queue.append(people)

while True:
    command = input().split()

    if command[0] == "End":
        print(f"{water_quantity} liters left")
        break

    if command[0] == "refill":
        water_quantity += int(command[1])
    else:
        if int(command[0]) <= water_quantity:
            print(f"{queue.popleft()} got water")
            water_quantity -= int(command[0])
        else:
            print(f"{queue.popleft()} must wait")
