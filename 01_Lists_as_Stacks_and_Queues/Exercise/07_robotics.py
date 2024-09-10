from collections import deque


# create dictionary with robot name, processing time and seconds left if the robot is busy(default 0):
def add_robots():
    robots = {}
    for robot in input().split(";"):
        name, processing_time = robot.split("-")
        robots[name] = [int(processing_time), 0]
    return robots


# add products in a queue so we can rotate:
def add_products():
    products = deque()
    while True:
        product = input()
        if product == "End":
            break
        products.append(product)
    return products


# check using strptime from datetime?
def time_to_seconds():
    hours, minutes, seconds = input().split(":")
    time = int(hours) * 60 * 60 + int(minutes) * 60 + int(seconds)
    return time


# check using timedelta from datetime?
def seconds_to_formated_time(time):
    # if we start at 23:59:59 => avoid showing hours > 23:
    time %= (24 * 60 * 60)

    hours = time // (60 * 60)
    minutes = time % (60 * 60) // 60
    seconds = time % (60 * 60) % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


robots_info = add_robots()
starting_time = time_to_seconds()
products_line = add_products()

while products_line:
    starting_time += 1

    # all busy robots decrease the seconds left of their current process:
    for robot_name, info in robots_info.items():
        if info[1] > 0:
            robots_info[robot_name][1] -= 1

    for robot_name, info in robots_info.items():
        if info[1] == 0:
            robots_info[robot_name][1] = robots_info[robot_name][0]
            curr_time = seconds_to_formated_time(starting_time)
            print(f"{robot_name} - {products_line.popleft()} [{curr_time}]")
            break
    else:
        products_line.rotate(-1)
