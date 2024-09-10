number_of_guests = int(input())
reservation_codes = set()

for _ in range(number_of_guests):
    code = input()
    reservation_codes.add(code)

while True:
    guest = input()

    if guest == "END":
        break

    if guest in reservation_codes:
        reservation_codes.remove(guest)

print(len(reservation_codes))
print(*sorted(reservation_codes), sep="\n")
