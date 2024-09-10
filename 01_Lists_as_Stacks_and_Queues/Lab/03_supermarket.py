from collections import deque

queue = deque()

while True:
    customer = input()

    if customer == "End":
        print(f"{len(queue)} people remaining.")
        break

    if customer == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(customer)

