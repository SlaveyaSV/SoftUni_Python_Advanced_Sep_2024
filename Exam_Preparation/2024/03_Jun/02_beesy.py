size = int(input())
field = []
bee_row = 0
bee_col = 0
energy = 15
restore_energy = 30
nectar = 0

for row in range(size):
    field.append([*input()])
    if "B" in field[row]:
        bee_row = row
        bee_col = field[row].index("B")
        field[bee_row][bee_col] = "-"

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while True:
    command = input()

    bee_row = (bee_row + moves[command][0]) % size
    bee_col = (bee_col + moves[command][1]) % size

    position = field[bee_row][bee_col]
    energy -= 1

    if position.isdigit():
        nectar += int(position)
        field[bee_row][bee_col] = "-"
    elif position == "H":
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if energy == 0 and nectar >= 30 and restore_energy:
        energy += (nectar-restore_energy)
        restore_energy = 0
    if energy == 0:
        print("This is the end! Beesy ran out of energy.")
        break

field[bee_row][bee_col] = "B"

[print(*line, sep="") for line in field]
