def accommodate(*args, **kwargs):
    available_rooms = kwargs
    total_guests = list(args)
    occupied_rooms = {}

    for i in range(len(total_guests)):
        for room, capacity in sorted(available_rooms.items(), key=lambda kvp: (kvp[1], kvp[0])):
            if total_guests[i] <= capacity:
                occupied_rooms[room] = total_guests[i]
                available_rooms[room] = 0
                total_guests[i] = 0
                break

    result = ""
    if occupied_rooms:
        result += f"A total of {len(occupied_rooms)} accommodations were completed!\n"
        for room, count in sorted(occupied_rooms.items()):
            result += f"<Room {room[-3:]} accommodates {count} guests>\n"
    else:
        result += "No accommodations were completed!\n"

    not_accommodated_guests = sum(total_guests)
    if not_accommodated_guests:
        result += f"Guests with no accommodation: {not_accommodated_guests}\n"
    empty_rooms = len(dict(filter(lambda kvp: kvp[1] != 0, available_rooms.items())))
    if empty_rooms:
        result += f"Empty rooms: {empty_rooms}"

    return result


print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))

