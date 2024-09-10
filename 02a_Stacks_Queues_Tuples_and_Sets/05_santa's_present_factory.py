from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

craft_presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

presents = []

while materials and magic_levels:

    total_magic_level = materials[-1] * magic_levels[0]

    if total_magic_level in craft_presents:
        presents.append(craft_presents[total_magic_level])
        new_present = craft_presents[total_magic_level]
        magic_levels.popleft()
        materials.pop()
    elif total_magic_level < 0:
        materials.append(materials.pop() + magic_levels.popleft())
    elif total_magic_level > 0:
        magic_levels.popleft()
        materials[-1] += 15
    else:
        if materials[-1] == 0:
            materials.pop()
        if magic_levels[0] == 0:
            magic_levels.popleft()

if ("Doll" in presents and "Train" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(list(map(str, materials[::-1])))}")
if magic_levels:
    print(f"Magic left: {', '.join(list(map(str, magic_levels)))}")

for present in sorted(set(presents)):
    print(f"{present}: {presents.count(present)}")
