from collections import deque
from functools import reduce

expression = deque(input().split())
numbers = []

while expression:
    char = expression.popleft()
    if char not in "+-*/":
        numbers.append(int(char))
    else:
        if char == "+":
            numbers = [reduce(lambda x, y: x + y, numbers)]
        elif char == "-":
            numbers = [reduce(lambda x, y: x - y, numbers)]
        elif char == "*":
            numbers = [reduce(lambda x, y: x * y, numbers)]
        elif char == "/":
            numbers = [reduce(lambda x, y: x // y, numbers)]

print(*numbers)
