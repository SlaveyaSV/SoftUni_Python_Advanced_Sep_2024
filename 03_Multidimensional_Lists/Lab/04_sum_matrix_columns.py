row_count, col_count = list(map(int, input().split(", ")))

matrix = [list(map(int, input().split())) for _ in range(row_count)]

for col in range(col_count):
    column_sum = 0
    for row in matrix:
        column_sum += row[col]
    print(column_sum)
