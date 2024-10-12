import os
from constants import ABSOLUTE_PROJECT_PATH  # the file "constants" must always be in the main project directory

try:
    path = os.path.join(ABSOLUTE_PROJECT_PATH, "06_File_Handling", "Lab", "01_file_opener", "text.txt")
    # we join/write the path from the "absolute" project directory of the project to the file
    file = open(path)
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")

try:
    path = os.path.join("text.txt")  # works when the text file is in the same directory as the py file
    file = open(path)
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")

try:
    path = os.path.join("..", "..", "test_text.txt")
    # going back to a file outside the directory with the correct amount of ".."
    file = open(path)
    print("File found")
    file.close()
except FileNotFoundError:
    print("File not found")
