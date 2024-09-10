presents = int(input())
size = int(input())

neighborhood = []
Santa = []
total_nice_kids = 0
nice_kids_with_presents = 0

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(size):
    neighborhood.append(input().split())
    if "S" in neighborhood[row]:
        Santa = [row, neighborhood[row].index("S")]
        neighborhood[Santa[0]][Santa[1]] = "-"
    total_nice_kids += neighborhood[row].count("V")

while presents > 0:
    command = input()

    if command == "Christmas morning":
        break

    curr_row = Santa[0] + moves[command][0]
    curr_col = Santa[1] + moves[command][1]

    if not (0 <= curr_row < size or 0 <= curr_col < size):
        continue

    Santa = [curr_row, curr_col]

    if neighborhood[curr_row][curr_col] == "C":
        # There won't be a case where the cookie is on the border of the matrix.
        # No instruction if Santa runs out of presents during the "cookie" moves - excluding it as an option
        for move in moves.values():
            move_row = curr_row+move[0]
            move_col = curr_col+move[1]
            if neighborhood[move_row][move_col] in "XV":
                if neighborhood[move_row][move_col] == "V":
                    nice_kids_with_presents += 1
                presents -= 1
                neighborhood[move_row][move_col] = "-"

    elif neighborhood[curr_row][curr_col] == "V":
        nice_kids_with_presents += 1
        presents -= 1

    neighborhood[curr_row][curr_col] = "-"

neighborhood[Santa[0]][Santa[1]] = "S"

if not presents and total_nice_kids > nice_kids_with_presents:
    print("Santa ran out of presents!")

[print(*line) for line in neighborhood]

if total_nice_kids > nice_kids_with_presents:
    print(f"No presents for {total_nice_kids-nice_kids_with_presents} nice kid/s.")
else:
    print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
