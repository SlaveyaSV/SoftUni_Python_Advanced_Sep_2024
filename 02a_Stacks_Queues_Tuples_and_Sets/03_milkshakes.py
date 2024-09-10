from collections import deque

chocolates = list(map(int, input().split(", ")))
cups_of_milk = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    # important to start with the case when both are <=0
    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue
    if chocolates[-1] <= 0:
        chocolates.pop()
        continue
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolates[-1] == cups_of_milk[0]:
        milkshakes += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

print("Great! You made all the chocolate milkshakes needed!" if milkshakes == 5 else "Not enough milkshakes.")
print(f"Chocolate: {', '.join(list(map(str, chocolates))) if chocolates else 'empty'}")
print(f"Milk: {', '.join(list(map(str, cups_of_milk))) if cups_of_milk else 'empty'}")
