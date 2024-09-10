matrix_size = int(input())
matrix = [list(map(int, input().split(", "))) for _ in range(matrix_size)]
primary_diagonal = [matrix[x][x] for x in range(matrix_size)]
secondary_diagonal = [matrix[x][-(x+1)] for x in range(matrix_size)]

print(f"Primary diagonal: {', '.join(list(map(str, primary_diagonal)))}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(list(map(str, secondary_diagonal)))}. Sum: {sum(secondary_diagonal)}")
