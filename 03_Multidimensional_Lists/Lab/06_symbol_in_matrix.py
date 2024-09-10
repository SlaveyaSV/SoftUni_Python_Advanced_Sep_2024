size = int(input())
matrix = [list(input()) for _ in range(size)]
symbol = input()
location = ()

for row in range(size):
    for col in range(size):
        if matrix[row][col] == symbol:
            location = (row, col)
            break
    if location:
        break


if location:
    print(location)
else:
    print(f"{symbol} does not occur in the matrix")


# Solution with exit() - terminating the program, not executing anything afterward:
# for row in range(size):
#     for col in range(size):
#         if matrix[row][col] == symbol:
#             location = (row, col)
#             print(location)
#             exit()
#
# print(f"{symbol} does not occur in the matrix")
