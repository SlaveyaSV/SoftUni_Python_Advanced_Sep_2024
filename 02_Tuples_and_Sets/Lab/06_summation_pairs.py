numbers = list(map(int, input().split()))
target_num = int(input())

for i in range(len(numbers)):
    if numbers[i] == "":
        continue
    for j in range(i + 1, len(numbers)):
        if numbers[j] == "":
            continue
        if numbers[i] + numbers[j] == target_num:
            print(f"{numbers[i]} + {numbers[j]} = {target_num}")
            numbers[i] = ""
            numbers[j] = ""
            break




