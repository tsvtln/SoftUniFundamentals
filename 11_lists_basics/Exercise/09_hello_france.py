collection_of_items = input().split('|')
budget = float(input())
clothes = 50.
shoes = 35.
accessories = 20.50
collected_money = 0
old_prices = 0
for items in collection_of_items:
    item, price = items.split('->')
    price = float(price)
    if item == 'Clothes' and price <= clothes and price <= budget:
        budget -= price
        old_prices += price
        new_price = price + (price * 0.4)
        collected_money += new_price
        print(f'{new_price:.2f}', end=' ')
    elif item == 'Shoes' and price <= shoes and price <= budget:
        budget -= price
        old_prices += price
        new_price = price + (price * 0.4)
        collected_money += new_price
        print(f'{new_price:.2f}', end=' ')
    elif item == 'Accessories' and price <= accessories and price <= budget:
        budget -= price
        old_prices += price
        new_price = price + (price * 0.4)
        collected_money += new_price
        print(f'{new_price:.2f}', end=' ')
print(f'\nProfit: {collected_money - old_prices:.2f}')
if collected_money + budget >= 150:
    print('Hello, France!')
else:
    print(f'Not enough money.')
