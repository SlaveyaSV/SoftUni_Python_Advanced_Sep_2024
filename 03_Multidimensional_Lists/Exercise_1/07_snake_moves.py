from collections import deque

rows, cols = list(map(int, input().split()))
word = input()

snake = deque(word)

for row in range(rows):
    while len(snake) < cols:
        snake += word

    if row % 2 == 0:
        print(*[snake.popleft() for _ in range(cols)], sep="")
    else:
        print(*[snake.popleft() for _ in range(cols)][::-1], sep="")
