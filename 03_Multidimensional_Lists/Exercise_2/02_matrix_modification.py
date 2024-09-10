size = int(input())
matrix = [list(map(int, input().split())) for _ in range(size)]

while True:
    command_input = input()

    if command_input == "END":
        break

    command = command_input.split()[0]
    row, col, value = list(map(int, command_input.split()[1:]))

    if not (0 <= row < size and 0 <= col < size):
        print("Invalid coordinates")
    elif command == "Add":
        matrix[row][col] += value
    elif command == "Subtract":
        matrix[row][col] -= value

[print(*line) for line in matrix]
