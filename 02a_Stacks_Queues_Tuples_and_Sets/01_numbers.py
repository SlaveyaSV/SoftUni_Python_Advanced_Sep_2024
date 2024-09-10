def create_set_of_nums(string):
    return set(map(int, string.split()))


sequences = {
    "First": create_set_of_nums(input()),
    "Second": create_set_of_nums(input())
}

number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split(" ", 2)

    if command[0] == "Add":
        numbers = create_set_of_nums(command[2])
        set(sequences[command[1]].add(num) for num in numbers)
        # may use .update()
    elif command[0] == "Remove":
        numbers = create_set_of_nums(command[2])
        set(sequences[command[1]].remove(num) for num in numbers if num in sequences[command[1]])
        # may use .difference_update()
    elif command[0] == "Check":
        print(sequences["First"] <= sequences["Second"] or sequences["Second"] <= sequences["First"])

for sequence in sequences.values():
    print(*sorted(sequence), sep=", ")
