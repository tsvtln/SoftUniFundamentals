food_quantities = input().split()
bakery = {}

for fq in range(0, len(food_quantities), 2):
    bakery[food_quantities[fq]] = int(food_quantities[fq + 1])

print(bakery)
