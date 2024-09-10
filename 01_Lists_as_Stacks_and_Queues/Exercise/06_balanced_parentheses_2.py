parentheses = input()
pairs = {"(": ")", "{": "}", "[": "]"}
open_parentheses = []

for char in parentheses:
    if char in pairs.keys():
        open_parentheses.append(char)
    elif not open_parentheses:
        open_parentheses.append(char)
        break
    elif char in pairs.values():
        if pairs[open_parentheses.pop()] != char:
            break


if not open_parentheses:
    print("YES")
else:
    print("NO")
