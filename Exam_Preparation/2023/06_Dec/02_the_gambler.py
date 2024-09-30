size = int(input())
game_board = []
gambler_row = None
gambler_col = None
money = 100

for row in range(size):
    game_board.append([*input()])
    if "G" in game_board[row]:
        gambler_row = row
        gambler_col = game_board[row].index("G")
        game_board[gambler_row][gambler_col] = "-"

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
game_over = False

command = input()

while command != "end":
    curr_row = gambler_row + moves[command][0]
    curr_col = gambler_col + moves[command][1]

    if not (0 <= curr_row < size and 0 <= curr_col < size):
        game_over = True
        break

    gambler_row = curr_row
    gambler_col = curr_col
    position = game_board[gambler_row][gambler_col]

    if position == "W":
        money += 100
    elif position == "P":
        money -= 200
        if money <= 0:
            game_over = True
            break
    elif position == "J":
        money += 100000
        print(f"You win the Jackpot!")
        break

    game_board[gambler_row][gambler_col] = "-"

    command = input()

game_board[gambler_row][gambler_col] = "G"
if game_over:
    print("Game over! You lost everything!")
else:
    print(f"End of the game. Total amount: {money}$")
    [print(*line, sep="") for line in game_board]
