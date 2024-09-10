def process_command(command, curr_row, curr_col):
    if command == "up" and curr_row != 0:
        curr_row -= 1
    elif command == "down" and curr_row != size-1:
        curr_row += 1
    elif command == "left" and curr_col != 0:
        curr_col -= 1
    elif command == "right" and curr_col != size-1:

        curr_col += 1
    return curr_row, curr_col


size = int(input())
commands = input().split()

game_field = [input().split() for _ in range(size)]
total_coal = 0
miner_row = 0
miner_col = 0

for row in range(size):
    for col in range(size):
        if game_field[row][col] == "s":
            miner_row = row
            miner_col = col
        elif game_field[row][col] == "c":
            total_coal += 1

for current_command in commands:
    miner_row, miner_col = process_command(current_command, miner_row, miner_col)

    if game_field[miner_row][miner_col] == "c":
        total_coal -= 1
        game_field[miner_row][miner_col] = "*"
        if total_coal == 0:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            exit()
    elif game_field[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        exit()

print(f"{total_coal} pieces of coal left. ({miner_row}, {miner_col})")
