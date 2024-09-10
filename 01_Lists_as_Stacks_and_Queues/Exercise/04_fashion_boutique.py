clothes = list(map(int, input().split()))
rack_capacity = int(input())
current_rack = rack_capacity
number_of_racks = 0

while clothes:
    while clothes and clothes[-1] <= current_rack:
        current_rack -= clothes.pop()
    current_rack = rack_capacity
    number_of_racks += 1

print(number_of_racks)
