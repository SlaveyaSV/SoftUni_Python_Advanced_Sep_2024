number_of_usernames = int(input())
usernames = set()

for _ in range(number_of_usernames):
    username = input()
    usernames.add(username)

print(*usernames, sep="\n")
