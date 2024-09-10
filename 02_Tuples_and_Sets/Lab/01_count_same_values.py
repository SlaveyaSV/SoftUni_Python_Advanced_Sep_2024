numbers = tuple(map(float, input().split()))

occurrences = {}

for num in numbers:
    if num not in occurrences:
        occurrences[num] = numbers.count(num)

[print(f"{num:.1f} - {count} times") for num, count in occurrences.items()]
