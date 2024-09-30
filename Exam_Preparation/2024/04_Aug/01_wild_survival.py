from collections import deque

bees = deque(map(int, input().split()))
bee_eaters = list(map(int, input().split()))

while bees and bee_eaters:
    bee_group = bees.popleft()
    bee_eaters_group = bee_eaters.pop()

    if bee_eaters_group * 7 > bee_group:
        bee_eaters_group -= (bee_group // 7)
        bee_eaters.append(bee_eaters_group)
    elif bee_eaters_group * 7 < bee_group:
        bee_group -= (bee_eaters_group * 7)
        bees.append(bee_group)

print("The final battle is over!")
if not bees and not bee_eaters:
    print("But no one made it out alive!")
elif bees:
    print(f"Bee groups left: {', '.join(list(map(str, bees)))}")
elif bee_eaters:
    print(f"Bee-eater groups left: {', '.join(list(map(str, bee_eaters)))}")
