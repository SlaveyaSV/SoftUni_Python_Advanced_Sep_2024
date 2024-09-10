from collections import deque

expression = input().split()
numbers = deque()

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}

for char in expression:
    if char not in operators:
        numbers.append(int(char))
    else:
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            numbers.appendleft(operators[char](first_num, second_num)) # appendleft !!!

print(*numbers)
