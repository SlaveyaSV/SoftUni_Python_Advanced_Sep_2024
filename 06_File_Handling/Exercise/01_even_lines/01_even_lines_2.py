import re


def read_text():
    with open("text.txt") as file:
        return file.readlines()


def print_even_lines():
    lines = read_text()
    for i in range(0, len(lines), 2):
        line = reversed(re.sub("[-,.!?]", "@", lines[i]).split())
        print(*line)


print_even_lines()
