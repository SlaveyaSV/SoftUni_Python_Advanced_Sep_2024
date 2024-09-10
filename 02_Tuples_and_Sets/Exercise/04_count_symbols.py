text = input()

char_count = {}

for char in text:
    if char not in char_count:
        char_count[char] = text.count(char)

for char, count in sorted(char_count.items()):
    print(f"{char}: {count} time/s")
