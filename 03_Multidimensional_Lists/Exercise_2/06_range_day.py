field = []
shooter = []
total_targets = 0
shot_targets = []

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

for row in range(5):
    field.append(input().split())
    if "A" in field[row]:  # finding player's position
        shooter = [row, field[row].index("A")]
    total_targets += field[row].count("x")  # counting all the targets

for _ in range(int(input())):
    command = input().split()

    if command[0] == "move":  # considering going to the new position directly, not step by step
        curr_row = shooter[0] + moves[command[1]][0] * int(command[2])
        curr_col = shooter[1] + moves[command[1]][1] * int(command[2])
        if 0 <= curr_row < 5 and 0 <= curr_col < 5:
            if field[curr_row][curr_col] == ".":
                shooter = [curr_row, curr_col]

    elif command[0] == "shoot":
        curr_row = shooter[0] + moves[command[1]][0]
        curr_col = shooter[1] + moves[command[1]][1]
        while 0 <= curr_row < 5 and 0 <= curr_col < 5:
            if field[curr_row][curr_col] == "x":
                shot_targets.append([curr_row, curr_col])
                field[curr_row][curr_col] = "."
                break
            curr_row += moves[command[1]][0]
            curr_col += moves[command[1]][1]

    if total_targets == len(shot_targets):  # stopping if all the targets are already hit
        print(f"Training completed! All {total_targets} targets hit.")
        break

if total_targets > len(shot_targets):
    print(f"Training not completed! {total_targets-len(shot_targets)} targets left.")

print(*shot_targets, sep="\n")
