import os

extensions = {}


def get_extensions(directory, first_level=False):
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)

        if os.path.isfile(file):
            extension = os.path.splitext(filename)[1]  # same as: filename.split(".")[-1]
            extensions[extension] = extensions.get(extension, []) + [filename]  # same as the usual creating of dict

        elif os.path.isdir(file) and not first_level:
            get_extensions(file, first_level=True)  # using recursion, but with boundary first_level of directory


def sort_extensions():
    result = ""

    sorted_extensions = sorted(extensions.items(), key=lambda kvp: kvp[0])

    for extension_name, file_name in sorted_extensions:
        result += f"{extension_name}\n"
        for name in sorted(file_name):
            result += f"- - - {name}\n"

    return result


def write_output_file(result):
    with open("report.txt", "w") as f:
        f.write(result)


directory_input = input("Enter directory name: ")  # for the current directory -> . (point)

try:
    get_extensions(directory_input)
except FileNotFoundError:
    print("Directory not found")

report = sort_extensions()
write_output_file(report)
