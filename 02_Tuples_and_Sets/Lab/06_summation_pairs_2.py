numbers = list(map(int, input().split()))
target = int(input())

targets = set()
values_map = {}

for num in numbers:
    if num in targets:
        targets.remove(num)
        pair = values_map[num]
        del values_map[num]
        print(f"{pair} + {num} = {target}")
    else:
        resulting_num = target - num
        targets.add(resulting_num)
        values_map[resulting_num] = num
