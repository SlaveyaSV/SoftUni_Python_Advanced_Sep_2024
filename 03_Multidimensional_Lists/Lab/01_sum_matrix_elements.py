row_count, col_count = list(map(int, input().split(", ")))

matrix = []

for row in range(row_count):
    matrix.append(list(map(int, input().split(", "))))

print(sum(sum(row) for row in matrix))
print(matrix)
