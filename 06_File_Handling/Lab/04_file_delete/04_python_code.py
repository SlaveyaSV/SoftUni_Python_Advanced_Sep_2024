import os
from constants import ABSOLUTE_PROJECT_PATH

path = os.path.join(ABSOLUTE_PROJECT_PATH, "06_File_handling", "Lab", "03_file_writer", "my_second_file.txt")

if os.path.exists(path):
    os.remove(path)
else:
    print("File already deleted!")

# try -> except can also be used
