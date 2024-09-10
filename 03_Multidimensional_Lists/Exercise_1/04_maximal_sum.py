from sys import maxsize

rows_count, cols_count = list(map(int, input().split()))
matrix = [list(map(int, input().split())) for _ in range(rows_count)]

max_sum = -maxsize
max_sub_matrix = []

for i in range(rows_count-2):
    for j in range(cols_count-2):
        sub_matrix = [matrix[i+x][j:j+3] for x in range(3)]
        sub_sum = sum(sum(row) for row in sub_matrix)
        if sub_sum > max_sum:
            max_sum = sub_sum
            max_sub_matrix = sub_matrix

print(f"Sum = {max_sum}")
[print(*row) for row in max_sub_matrix]
