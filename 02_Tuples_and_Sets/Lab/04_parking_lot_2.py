def add_car(parking_set, car):
    parking_set.add(car_number)


def remove_car(parking_set, car):
    if car in parking_set:
        parking_set.remove(car_number)


number_of_commands = int(input())

parking = set()

mapper = {
    "IN": add_car,
    "OUT": remove_car
}

for _ in range(number_of_commands):
    direction, car_number = input().split(", ")

    mapper[direction](parking, car_number)

if parking:
    print(*parking, sep="\n")
else:
    print("Parking Lot is Empty")
