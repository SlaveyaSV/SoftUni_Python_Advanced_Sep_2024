def boarding_passengers(ship_capacity, *args):
    ship = {}
    boarded_passengers = 0
    total_passengers = sum(int(group[0]) for group in args)

    for passengers, benefit_program in args:
        if boarded_passengers + passengers <= ship_capacity:
            if benefit_program not in ship:
                ship[benefit_program] = 0
            ship[benefit_program] += passengers
            boarded_passengers += passengers
        if ship_capacity == boarded_passengers:
            break

    result = "Boarding details by benefit plan:\n"
    for program, guests in sorted(ship.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        result += f"## {program}: {guests} guests\n"

    if total_passengers == boarded_passengers:
        result += "All passengers are successfully boarded!"
    elif total_passengers > boarded_passengers:
        if ship_capacity == boarded_passengers:
            result += "Boarding unsuccessful. Cruise ship at full capacity."
        else:
            result += f"Partial boarding completed. Available capacity: {ship_capacity - boarded_passengers}."

    return result


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'),
                          (15, 'Diamond'), (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'),
                          (31, 'Platinum'), (20, 'Diamond')))
