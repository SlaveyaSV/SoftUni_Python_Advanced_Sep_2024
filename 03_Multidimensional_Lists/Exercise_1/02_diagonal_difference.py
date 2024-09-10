matrix_size = int(input())

primary_diagonal = 0
secondary_diagonal = 0

for i in range(matrix_size):
    line = list(map(int, input().split()))
    primary_diagonal += line[i]
    secondary_diagonal += line[-(i+1)]

print(abs(primary_diagonal-secondary_diagonal))
