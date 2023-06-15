price, total, taxes, total_with_taxes = '', 0, 0, 0
REGULAR, SPECIAL, VALID_ORDER = False, False, True
while not REGULAR and not SPECIAL:
    price = input()
    if price == "special" or price == "regular":
        if price == "special":
            SPECIAL = True
            continue
        elif price == 'regular':
            REGULAR = True
            continue
    elif float(price) < 0:
        print('Invalid price!')
    else:
        total += float(price)
        taxes += float(price) * 0.2

if total == 0:
    print('Invalid order!')
    VALID_ORDER = False
elif SPECIAL:
    total_with_taxes = (total + taxes) - ((total + taxes) * 0.1)
else:
    total_with_taxes = total + taxes
if VALID_ORDER:
    print("Congratulations you've just bought a new computer!")
    print(f'Price without taxes: {total:.2f}$')
    print(f'Taxes: {taxes:.2f}$\n-----------')
    print(f'Total price: {total_with_taxes:.2f}$')
