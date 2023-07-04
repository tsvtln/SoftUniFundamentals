products_entry, products_requested, products_db = input().split(), input().split(), dict()
for product in range(0, len(products_entry), 2):
    products_db[products_entry[product]] = int(products_entry[product + 1])
for search in products_requested:
    print(f"We have {products_db[search]} of {search} left") if search in products_db else\
        print(f"Sorry, we don't have {search}")
