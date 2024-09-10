size = int(input())

game = []
bunny = []

max_sum = float("-inf")
max_positions = []
max_direction = ""

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    game.append(input().split())  # creating the game field
    if "B" in game[row]:  # finding bunny's coordinates [row, col]
        bunny.append(row)
        bunny.append(game[row].index("B"))

for direction, move in moves.items():  # iterating through every direction
    curr_positions = []
    curr_sum = 0

    curr_row = bunny[0] + move[0]
    curr_col = bunny[1] + move[1]

    while 0 <= curr_row < size and 0 <= curr_col < size:  # making sure to be in the game field boundaries
        if game[curr_row][curr_col] != "X":
            curr_positions.append([curr_row, curr_col])  # appending them as a list to use it in the print below
            curr_sum += int(game[curr_row][curr_col])
            curr_row += move[0]
            curr_col += move[1]
        else:
            break  # if "X" => break the while loop (the current move) and continue with the next move

    if curr_sum >= max_sum:  # checking if the sum for this move is bigger than the current max sum
        max_sum = curr_sum
        max_positions = curr_positions
        max_direction = direction

print(max_direction)
[print(position) for position in max_positions]
print(max_sum)
