from sys import maxsize

row_count, col_count = list(map(int, input().split(", ")))
matrix = [list(map(int, input().split(", "))) for _ in range(row_count)]
sub_matrix_size = 2
max_sub_matrix = []
max_matrix_sum = -maxsize

for row in range(row_count-sub_matrix_size+1):
    for col in range(col_count-sub_matrix_size+1):
        current_sub_matrix = [matrix[row+n][col:col+sub_matrix_size] for n in range(sub_matrix_size)]
        current_sum = sum([sum(sub_row) for sub_row in current_sub_matrix])
        if current_sum > max_matrix_sum:
            max_matrix_sum = current_sum
            max_sub_matrix = current_sub_matrix

for max_sub_row in max_sub_matrix:
    print(*max_sub_row)
print(max_matrix_sum)
