from collections import deque

food_quantity = int(input())
orders = deque(list(map(int, input().split())))

print(max(orders))

while orders and orders[0] <= food_quantity:
    food_quantity -= orders.popleft()

if orders:
    # print(f"Orders left: {' '.join(list(map(str, orders)))}")
    print("Orders left:", *orders)
else:
    print("Orders complete")
