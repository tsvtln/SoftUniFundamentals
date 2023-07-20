products = dict()
command = ''


def split_values(dictionary, key, separator=' '):
    if key in dictionary:
        value = dictionary[key]
        splited_values = value.split(separator)
        return [float(val) for val in splited_values]


while command != 'buy':
    command = input()
    if command == 'buy':
        continue
    product, price, quantity = command.split()
    if product not in products:
        products[product] = f"{price} {quantity}"
        continue
    if product in products:
        price_d, quantity_d = split_values(products, product)
        price, quantity = float(price), int(quantity)
        if price_d != price:
            price_d = price
        quantity_d += quantity
        crnt_pq = f"{price_d} {quantity_d}"
        products[product] = crnt_pq

for print_prices in products:
    price, quantity = split_values(products, print_prices)
    print(f"{print_prices} -> {price * quantity:.2f}")
