def take_current_bunnies(matrix, rows_count, cols_count):
    bunnies = []
    for row in range(rows_count):
        for col in range(cols_count):
            if matrix[row][col] == "B":
                bunnies.append((row, col))
    return bunnies


def spread_bunnies(matrix, rows_count, cols_count):
    for bunny in take_current_bunnies(matrix, rows_count, cols_count):
        if bunny[0] > 0:
            matrix[bunny[0] - 1][bunny[1]] = "B"
        if bunny[0] < rows_count - 1:
            matrix[bunny[0] + 1][bunny[1]] = "B"
        if bunny[1] > 0:
            matrix[bunny[0]][bunny[1] - 1] = "B"
        if bunny[1] < cols_count - 1:
            matrix[bunny[0]][bunny[1] + 1] = "B"


rows, cols = list(map(int, input().split()))

lair = []
player_row = 0
player_col = 0
is_won = False

for curr_row in range(rows):
    lair.append(list(input()))

    if "P" in lair[curr_row]:
        player_row, player_col = curr_row, lair[curr_row].index("P")

commands = list(input())

directions = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}

for command in commands:
    curr_row, curr_col = player_row + directions[command][0], player_col + directions[command][1]
    lair[player_row][player_col] = "."

    spread_bunnies(lair, rows, cols)

    if not (0 <= curr_row < rows and 0 <= curr_col < cols):
        is_won = True
        break

    player_row, player_col = curr_row, curr_col

    if lair[player_row][player_col] == "B":
        break

[print(*line, sep="") for line in lair]
if is_won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")
