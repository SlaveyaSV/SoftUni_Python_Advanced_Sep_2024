symbols_for_replace = ("-", ",", ".", "!", "?")

with open("text.txt") as file:
    lines = file.readlines()

for line in range(0, len(lines), 2):
    for symbol in symbols_for_replace:
        lines[line] = lines[line].replace(symbol, "@")
    print(" ".join(lines[line].split()[::-1]))
