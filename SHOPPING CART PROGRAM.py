ITEMS = []
PRICES = []
TOTAL = 0

while True:
    food = input("ENTER THE FOOD YOU WOULD LIKE TO BUY(type q to quit): ")
    if food.lower() == "q":
     break

    else:
         ITEMS.append(food)
         price = float(input(f"ENTER THE PRICE OF THE {food} :$ "))
         PRICES.append(price)

print("-----YOUR CART-----")
for x in ITEMS :
    print(x,end=" ,")

for y in PRICES :
      TOTAL= y + TOTAL
print()
print(f"YOUR TOTAL BILL IS ${TOTAL}")

