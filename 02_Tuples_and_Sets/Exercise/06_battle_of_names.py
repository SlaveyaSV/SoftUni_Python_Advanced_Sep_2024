number_of_names = int(input())
odd_set = set()
even_set = set()

for row in range(1, number_of_names + 1):
    name = input()
    ascii_sum = int(sum(ord(char) for char in name) / row)
    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum)
    else:
        odd_set.add(ascii_sum)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)

if odd_set_sum == even_set_sum:
    print(*odd_set.union(even_set), sep=", ")
elif odd_set_sum > even_set_sum:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
