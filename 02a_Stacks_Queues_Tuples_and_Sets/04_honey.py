from collections import deque

working_bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
honey_making_process = deque(input().split())

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
}

total_honey = 0

while working_bees and nectar:
    if working_bees[0] <= nectar[-1]:
        if honey_making_process[0] == "/" and nectar[-1] == 0:
            working_bees.popleft()
            nectar.pop()
            honey_making_process.popleft()
        else:
            total_honey += abs(operators[honey_making_process.popleft()](working_bees.popleft(), nectar.pop()))
    else:
        nectar.pop()

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(list(map(str, working_bees)))}")
if nectar:
    print(f"Nectar left: {', '.join(list(map(str, nectar)))}")
