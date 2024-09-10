rows_count = int(input())

evens = []

for _ in range(rows_count):
    row = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    evens.append(row)

print(evens)

#  more time-consuming solution:
# matrix = [[int(x) for x in input().split(", ")] for _ in range(rows_count)]
# evens = [[x for x in row if x % 2 == 0] for row in matrix]
# print(evens)
