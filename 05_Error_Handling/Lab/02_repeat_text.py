text = input()

try:
    times = int(input())
    print(text * times)
except ValueError as ex:
    print("Variable times must be an integer")
