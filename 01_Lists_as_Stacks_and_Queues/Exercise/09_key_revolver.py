from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = list(map(int, input().split()))
locks = deque(list(map(int, input().split())))
intelligence_value = int(input())

bullets_shot = 0

while bullets and locks:

    bullets_shot += 1

    if bullets.pop() <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if bullets_shot % gun_barrel_size == 0 and bullets:
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence_value - (bullets_shot * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
