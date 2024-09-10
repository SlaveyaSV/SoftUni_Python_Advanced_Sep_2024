size = int(input())

wonderland = []
Alice = []
tea_bags = 0

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    wonderland.append(input().split())  # creating the game field

    if "A" in wonderland[row]:  # finding Alice's coordinates [row, col] and replace it with "*"
        Alice = [row, wonderland[row].index("A")]
        wonderland[Alice[0]][Alice[1]] = "*"

curr_row = Alice[0]
curr_col = Alice[1]

while True:
    command = input()

    curr_row += moves[command][0]
    curr_col += moves[command][1]

    if not (0 <= curr_row < size and 0 <= curr_col < size):
        break

    if wonderland[curr_row][curr_col] == "R":
        wonderland[curr_row][curr_col] = "*"
        break

    if wonderland[curr_row][curr_col].isdigit():  # nums will be in range(0, 10), no negatives
        tea_bags += int(wonderland[curr_row][curr_col])

    wonderland[curr_row][curr_col] = "*"

    if tea_bags >= 10:
        break

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*line) for line in wonderland]
