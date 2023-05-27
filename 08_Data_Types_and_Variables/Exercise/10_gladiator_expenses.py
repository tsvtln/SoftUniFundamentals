lost_fights, helmet_price, sword_price, shield_price, armor_price = int(input()), float(input()), float(input()), float(input()), float(input()) 
expenses, shield_breaks = 0, 0
for loses in range(1, lost_fights + 1):
    if loses % 2 == 0:
        expenses += helmet_price
    if loses % 3 == 0:
        expenses += sword_price
    if loses % 2 == 0 and loses % 3 == 0:
        expenses += shield_price
        shield_breaks += 1
        if shield_breaks % 2 == 0:
            expenses += armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')
