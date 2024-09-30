from collections import deque

packages = list(map(int, input().split()))
couriers = deque(map(int, input().split()))
total_weight_delivered = 0

while packages and couriers:
    package = packages.pop()
    courier = couriers.popleft()

    if courier >= package:
        total_weight_delivered += package
        courier -= 2 * package
        if courier > 0:
            couriers.append(courier)
    else:
        package -= courier
        total_weight_delivered += courier
        packages.append(package)

print(f"Total weight: {total_weight_delivered} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages and not couriers:
    packages_print = ", ".join(list(map(str, packages)))
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {packages_print}")
elif couriers and not packages:
    couriers_print = ", ".join(list(map(str, couriers)))
    print(f"Couriers are still on duty: {couriers_print} but there are no more packages to deliver.")
