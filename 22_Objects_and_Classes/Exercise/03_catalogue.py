class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        products = Catalogue.products
        products.append(product_name)

    def get_by_letter(self, first_letter: str):
        products = Catalogue.products
        found_list = []
        for product in products:
            if product.startswith(first_letter):
                found_list.append(product)
        return found_list

    def __repr__(self):
        Catalogue.products.sort()
        items = '\n'.join(Catalogue.products)
        return f"Items in the {self.name} catalogue:\n{items}"


"""test case"""
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("C"))
# print(catalogue)
