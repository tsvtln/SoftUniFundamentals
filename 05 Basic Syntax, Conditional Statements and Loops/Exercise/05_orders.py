total_price, num_of_orders = 0, int(input())

for order in range(num_of_orders):
    pp_capsule, days, capsules_per_day = float(input()), int(input()), int(input())
    if pp_capsule > 100 or pp_capsule < 0.01 or days > 31 or days < 1 \
            or capsules_per_day > 2000 or capsules_per_day < 1:
        continue
    price = (capsules_per_day * days) * pp_capsule
    total_price += price
    print(f'The price for the coffee is: ${price:.2f}')
print(f'Total: ${total_price:.2f}')
