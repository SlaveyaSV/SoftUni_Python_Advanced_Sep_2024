def even_odd_filter(**kwargs):
    for num_type, num_list in kwargs.items():
        for num in reversed(num_list):
            if num_type == "even" and num % 2 != 0:
                kwargs[num_type].remove(num)
            elif num_type == "odd" and num % 2 == 0:
                kwargs[num_type].remove(num)

    # kwargs = {num_type: [num for num in num_list if num % 2 == (0 if num_type == "even" else 1)]
    #           for num_type, num_list in kwargs.items()}

    return dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

