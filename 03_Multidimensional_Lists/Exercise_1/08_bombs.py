size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

bombs = input().split()

for bomb in bombs:
    row, col = list(map(int, bomb.split(",")))
    row_start = row-1 if row != 0 else 0
    row_end = row+1+1 if row != size-1 else size
    col_start = col-1 if col != 0 else 0
    col_end = col+1+1 if col != size-1 else size

    bomb_amount = matrix[row][col]
    if bomb_amount <= 0:
        continue

    for row in range(row_start, row_end):
        for col in range(col_start, col_end):
            if matrix[row][col] > 0:
                matrix[row][col] -= bomb_amount

actives = [col for row in matrix for col in row if col > 0]

print(f"Alive cells: {len(actives)}\nSum: {sum(actives)}")
[print(*line) for line in matrix]
