def orders(product: str, quantity: int) -> float:
    if product == 'water':
        price = quantity * 1
        return price
    elif product == 'coffee':
        price = quantity * 1.5
        return price
    elif product == 'coke':
        price = quantity * 1.4
        return price
    elif product == 'snacks':
        price = quantity * 2
        return price


inp_product = input()
inp_quantity = int(input())
print(f'{orders(inp_product, inp_quantity):.2f}')

