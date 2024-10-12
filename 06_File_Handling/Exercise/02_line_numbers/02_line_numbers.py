import re
from string import punctuation


def read_text():
    with open("text.txt") as file:
        return file.readlines()


def count_letters_and_punctuations(output):
    lines = read_text()
    for row, line in enumerate(lines):
        letters_count = len(re.findall(r"\w", line))
        punctuation_count = len(re.findall(rf"[{punctuation}]", line))
        output.append(f"Line {row + 1}: {line.strip()} ({letters_count})({punctuation_count})")


def write_output_file(output):
    with open("output.txt", "w") as file:
        for result in output:
            file.write(f"{result}\n")


output_list = []

count_letters_and_punctuations(output_list)
write_output_file(output_list)
