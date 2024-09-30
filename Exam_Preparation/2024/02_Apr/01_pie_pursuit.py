from collections import deque

contestants = deque(map(int, input().split()))
pies = list(map(int, input().split()))

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()

    if contestant > pie:
        contestants.append(contestant-pie)
    elif contestant < pie:
        pie -= contestant
        if pie == 1 and pies:
            pies[-1] += 1
        else:
            pies.append(pie)

if contestants and not pies:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(list(map(str, contestants)))}")
elif pies and not contestants:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(list(map(str, pies)))}")
elif not (contestants and pies):
    print("We have a champion!")
