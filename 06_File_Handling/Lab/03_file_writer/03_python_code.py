with open("my_first_file.txt", "w") as file:
    file.write("I just created my first file!")
# this structure automatically closes the file once done
# when we try to open a non-existing file using "w" or "a", the program creates it in the current directory


# # same code without the "with" structure:
# file = open("my_second_file.txt", "w")
# file.write("I just created my second file!")
# file.close()
