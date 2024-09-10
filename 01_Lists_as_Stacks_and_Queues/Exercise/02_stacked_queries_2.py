stack = []
queries_count = int(input())

for _ in range(queries_count):
    query = input().split()

    if query[0] == "1":
        stack.append(int(query[1]))
    elif stack:
        if query[0] == "2":
            stack.pop()
        elif query[0] == "3":
            print(max(stack))
        elif query[0] == "4":
            print(min(stack))

print(", ".join(str(num) for num in reversed(stack)))
