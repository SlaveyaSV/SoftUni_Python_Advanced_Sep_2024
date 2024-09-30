from collections import deque

worms = list(map(int, input().split()))
holes = deque(map(int, input().split()))

matches = 0
total_worms = len(worms)

while worms and holes:
    worm = worms.pop()
    hole = holes.popleft()

    if worm != hole:
        worm -= 3
        if worm > 0:
            worms.append(worm)
    else:
        matches += 1

print(f"Matches: {matches}" if matches else "There are no matches.")
if worms:
    print(f"Worms left: {', '.join(list(map(str, worms)))}")
else:
    print(f"Every worm found a suitable hole!" if matches == total_worms else "Worms left: none")
print(f"Holes left: {', '.join(list(map(str, holes)))}" if holes else "Holes left: none")
