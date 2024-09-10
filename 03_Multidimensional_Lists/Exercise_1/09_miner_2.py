size = int(input())
commands = input().split()

game_field = []
total_coal = 0
miner_row = 0
miner_col = 0

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row in range(size):
    game_field.append(input().split())

    if "s" in game_field[row]:
        miner_row, miner_col = row, game_field[row].index("s")

    total_coal += game_field[row].count("c")

for command in commands:
    curr_row, curr_col = miner_row + directions[command][0], miner_col + directions[command][1]

    if not (0 <= curr_row < size and 0 <= curr_col < size):
        continue

    miner_row, miner_col = curr_row, curr_col

    if game_field[miner_row][miner_col] == "c":
        total_coal -= 1
        game_field[miner_row][miner_col] = "*"
        if total_coal == 0:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            break
    elif game_field[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        break

else:
    print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")
