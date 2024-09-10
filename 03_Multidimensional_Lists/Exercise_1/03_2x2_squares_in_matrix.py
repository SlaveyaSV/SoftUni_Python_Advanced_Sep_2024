row_count, col_count = list(map(int, input().split()))
matrix = [input().split() for _ in range(row_count)]
equal_squares = 0

for i in range(row_count-1):
    for j in range(col_count-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            equal_squares += 1

print(equal_squares)
