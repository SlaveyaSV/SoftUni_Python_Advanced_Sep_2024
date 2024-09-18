def grocery_store(**kwargs):
    result = []
    for product, quantity in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0])):
        result.append(f"{product}: {quantity}")
    return "\n".join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

