size = int(input())
health = 100
player_row, player_col = 0, 0
maze = []

# creating the maze/matrix and defining the player's position:
for row in range(size):
    maze.append([*input()])
    if "P" in maze[row]:
        player_row = row
        player_col = maze[row].index("P")
        maze[player_row][player_col] = "-"

moves = {"up": (-1, 0), "down": (1, 0), "right": (0, 1), "left": (0, -1)}

# moving throughout the maze/matrix:
while True:
    command = input()

    curr_row = player_row + moves[command][0]
    curr_col = player_col + moves[command][1]

    # checking for invalid moves (out of the maze/matrix):
    if not (0 <= curr_row < size and 0 <= curr_col < size):
        continue

    player_row, player_col = curr_row, curr_col
    position = maze[player_row][player_col]

    if position == "X":
        print("Player escaped the maze. Danger passed!")
        break

    if position == "H":
        health = min(100, health+15)
    elif position == "M":
        health -= 40
        if health <= 0:
            health = 0
            print("Player is dead. Maze over!")
            break  # in this case position will be replaced with "P" after the loop, so no need for "-"

    maze[player_row][player_col] = "-"

# setting the last player' position:
maze[player_row][player_col] = "P"

print(f"Player's health: {health} units")
[print(*line, sep="") for line in maze]
