rows, cols = list(map(int, input().split()))
start = ord("a")

matrix = [[chr(i) + chr(i+j) + chr(i) for j in range(cols)] for i in range(start, start+rows)]

[print(*row) for row in matrix]
