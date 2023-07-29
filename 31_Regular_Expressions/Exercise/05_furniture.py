import re

command = ''
# pattern = r"(?P<price>\d+(?:\.\d+)?)!(?P<quantity>\d+)"
pattern = r">>(?P<product>\w+)<<(?P<price>\d+(?:\.\d+)?)!(?P<quantity>\d+)"
furniture = []
bill = 0

while command != 'Purchase':
    command = input()
    if command == 'Purchase':
        continue
    get_price_quantity = re.search(pattern, command)
    if get_price_quantity:
        product = get_price_quantity.group('product')
        price = get_price_quantity.group('price')
        quantity = get_price_quantity.group('quantity')
        bill += float(price) * int(quantity)
        furniture.append(product)

print("Bought furniture:")
for product in furniture:
    print(product)
print(f"Total money spend: {bill:.2f}")
