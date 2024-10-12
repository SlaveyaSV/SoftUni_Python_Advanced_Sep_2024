import os
import re

from constants import ABSOLUTE_PROJECT_PATH

words_path = os.path.join(ABSOLUTE_PROJECT_PATH, "06_File_Handling", "Lab", "05_word_count", "words.txt")
text_path = os.path.join(ABSOLUTE_PROJECT_PATH, "06_File_Handling", "Lab", "05_word_count", "text.txt")

counter = {}

with open(words_path) as file:
    words = file.read().split()

with open(text_path) as file:
    text = file.read()

output = {}

for word in words:
    regex = rf"\b{word}\b"
    result = re.findall(regex, text, re.IGNORECASE)
    if result:
        output[word] = len(result)

with open("output.txt", "w") as file:
    for word, count in sorted(output.items(), key=lambda kvp: -kvp[1]):
        file.write(f"{word} - {count}\n")
