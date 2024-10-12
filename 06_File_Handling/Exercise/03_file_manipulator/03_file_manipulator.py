import os


def create_file(filename):
    open(filename, "w").close()


def add_content(filename, content):
    with open(filename, "a") as file:
        file.write(f"{content[0]}\n")


def replace_string(filename, content):
    try:
        with open(filename, "r+") as file:
            string = file.read()
            file.seek(0)  # pointer goes to 0 position
            file.truncate(0)  # deletes all from 0 position to the end
            file.write(string.replace(content[0], content[1]))
    except FileNotFoundError:
        print("An error occurred")


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("An error occurred")


def process_commands(command):
    command_type, file_name, *args = command.split("-")

    if command_type == "Create":
        create_file(file_name)
    elif command_type == "Add":
        add_content(file_name, args)
    elif command_type == "Replace":
        replace_string(file_name, args)
    elif command_type == "Delete":
        delete_file(file_name)


command_input = input()

while command_input != "End":

    process_commands(command_input)

    command_input = input()
