parentheses = input()
doubles = {"(": ")", "{": "}", "[": "]"}
check_stack = []

for char in parentheses:
    if char in doubles.keys():
        check_stack.append(char)
    elif char in doubles.values():
        if check_stack:
            if doubles[check_stack.pop()] != char:
                break
        else:
            check_stack.append(char)
            break


if not check_stack:
    print("YES")
else:
    print("NO")
