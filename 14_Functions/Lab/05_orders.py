def orders(product: str, quantity: int) -> float:
    prices = {'water': 1, 'coffee': 1.5, 'coke': 1.4, 'snacks': 2}

    if product in prices:
        price = quantity * prices[product]


try:
    inp_product = input()
    inp_quantity = int(input())

    total_price = orders(inp_product, inp_quantity)
    print(f'{total_price:.2f}')
except ValueError as e:
    print(str(e))

# def orders(product: str, quantity: int) -> float:
#     price = 0
#     if product == 'water':
#         price = quantity * 1
#     elif product == 'coffee':
#         price = quantity * 1.5
#     elif product == 'coke':
#         price = quantity * 1.4
#     elif product == 'snacks':
#         price = quantity * 2
#     return price
#
#
# inp_product = input()
# inp_quantity = int(input())
# print(f'{orders(inp_product, inp_quantity):.2f}')
