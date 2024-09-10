size = int(input())
matrix = [list(input()) for _ in range(size)]

knights = [(row, col) for row in range(size) for col in range(size) if matrix[row][col] == "K"]
moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

removed_knights = 0

while True:
    attacks_count = []

    for knight in knights:
        curr_knight = 0
        for move in moves:
            curr_row = knight[0] + move[0]
            curr_col = knight[1] + move[1]

            if not (0 <= curr_row < size and 0 <= curr_col < size):
                continue

            if matrix[curr_row][curr_col] == "K":
                curr_knight += 1

        attacks_count.append(curr_knight)

    if sum(attacks_count) == 0:
        break

    max_attack_index = attacks_count.index(max(attacks_count))
    row_rem = knights[attacks_count.index(max(attacks_count))][0]
    col_rem = knights[attacks_count.index(max(attacks_count))][1]

    matrix[row_rem][col_rem] = 0 # what's wrong with this?
    knights.pop(max_attack_index)
    removed_knights += 1

print(removed_knights)

