import os
from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "06_File_Handling", "Lab", "02_file_reader", "numbers.txt")

total = 0

try:
    file = open(path)
    lines = file.readlines()
    for line in lines:
        # number = int(line[:-1])  # avoids the empty sign (\n)
        # total += number
        total += int(line)  # works fine in this case
    print(total)
    file.close()
except FileNotFoundError:
    print("File not found")
