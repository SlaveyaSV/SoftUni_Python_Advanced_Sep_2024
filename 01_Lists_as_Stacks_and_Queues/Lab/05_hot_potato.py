from collections import deque

kids = deque(input().split())
toss_num = int(input()) - 1

while len(kids) > 1:
    # for kid in range(toss_num):
    #     kids.append(kids.popleft())
    kids.rotate(-toss_num)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")

# kids = deque(input().split())
# toss_num = int(input())
# counter = 0
#
# while len(kids) > 1:
#     counter += 1
#     if counter != toss_num:
#         kids.append(kids.popleft())
#     else:
#         print(f"Removed {kids.popleft()}")
#         counter = 0
#
# print(f"Last is {kids.popleft()}")
