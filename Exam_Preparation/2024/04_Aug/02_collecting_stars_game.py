size = int(input())
field = []
p_row = 0
p_col = 0
stars = 2

for row in range(size):
    field.append(input().split())
    if "P" in field[row]:
        p_row = row
        p_col = field[row].index("P")
        field[p_row][p_col] = "."

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    curr_row = p_row + moves[command][0]
    curr_col = p_col + moves[command][1]

    if not (0 <= curr_row < size and 0 <= curr_col < size):
        curr_row, curr_col = 0, 0

    position = field[curr_row][curr_col]

    if position == "*":
        stars += 1
        field[curr_row][curr_col] = "."
    elif position == "#":
        stars -= 1

    if field[curr_row][curr_col] == ".":
        p_row, p_col = curr_row, curr_col

    if stars == 10:
        print("You won! You have collected 10 stars.")
        break
    elif stars == 0:
        print("Game over! You are out of any stars.")
        break

field[p_row][p_col] = "P"
print(f"Your final position is [{p_row}, {p_col}]")
[print(*line) for line in field]
