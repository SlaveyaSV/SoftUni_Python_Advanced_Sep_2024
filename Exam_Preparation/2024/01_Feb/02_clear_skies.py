size = int(input())
airspace = []
j_row = 0
j_col = 0
armor = 300
enemies = 0

for row in range(size):
    airspace.append([*input()])
    if "J" in airspace[row]:
        j_row = row
        j_col = airspace[row].index("J")
        airspace[j_row][j_col] = "-"
    if "E" in airspace[row]:
        enemies += airspace[row].count("E")

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    curr_row = j_row + moves[command][0]
    curr_col = j_col + moves[command][1]

    if not(0 <= curr_row < size and 0 <= curr_col < size):
        continue

    j_row = curr_row
    j_col = curr_col
    position = airspace[j_row][j_col]

    if position == "E":
        if enemies == 1:
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            armor -= 100
            enemies -= 1
            if armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{j_row}, {j_col}]!")
                break
    elif position == "R":
        armor = 300

    airspace[j_row][j_col] = "-"

airspace[j_row][j_col] = "J"

[print(*line, sep="") for line in airspace]
