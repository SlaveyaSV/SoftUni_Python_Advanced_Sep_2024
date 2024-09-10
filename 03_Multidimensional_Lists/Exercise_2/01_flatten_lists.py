matrix = [line.split() for line in input().split("|")[::-1]]
[print(*nums, end=" ") for nums in matrix if nums]
