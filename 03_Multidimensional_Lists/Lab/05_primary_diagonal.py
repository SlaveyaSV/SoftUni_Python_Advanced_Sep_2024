size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]
primary_diagonal_sum = sum([matrix[x][x] for x in range(len(matrix))])
print(primary_diagonal_sum)
