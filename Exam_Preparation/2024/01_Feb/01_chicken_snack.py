from collections import deque

amount_of_money = list(map(int, input().split()))
prices_of_food = deque(map(int, input().split()))
eaten_food = 0

while amount_of_money and prices_of_food:
    money = amount_of_money.pop()
    price = prices_of_food.popleft()

    if money < price:
        continue
    elif money > price and amount_of_money:
        amount_of_money[-1] += (money-price)

    eaten_food += 1

if eaten_food >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_food} foods.")
elif eaten_food == 0:
    print("Henry remained hungry. He will try next weekend again.")
else:
    print(f"Henry ate: {eaten_food} food{'' if eaten_food == 1 else 's'}.")
