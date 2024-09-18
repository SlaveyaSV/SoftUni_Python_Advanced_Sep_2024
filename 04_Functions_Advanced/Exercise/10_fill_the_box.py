def fill_the_box(height, length, width, *args):
    box_size = height * length * width
    cubes = [num for num in args if num != "Finish"]
    for i in range(args.index("Finish")):
        if cubes[i] <= box_size:
            box_size -= cubes[i]
            cubes[i] = 0
        else:
            cubes[i] -= box_size
            box_size = 0

    if box_size > 0:
        return f"There is free space in the box. You could put {box_size} more cubes."

    cubes_left = sum(cubes)
    if box_size == 0 and cubes_left > 0:
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
