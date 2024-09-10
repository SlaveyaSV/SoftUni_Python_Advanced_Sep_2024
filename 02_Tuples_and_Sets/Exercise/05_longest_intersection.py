def create_set(range_input):
    start, end = list(map(int, range_input.split(",")))
    return set(range(start, end + 1))


number_of_lines = int(input())
max_intersection = set()

for _ in range(number_of_lines):
    range_1, range_2 = input().split("-")

    first_set = create_set(range_1)
    second_set = create_set(range_2)

    curr_intersection = first_set.intersection(second_set)

    if len(curr_intersection) > len(max_intersection):
        max_intersection = curr_intersection

print(f"Longest intersection is {list(max_intersection)} with length {len(max_intersection)}")
