class Inventory:
    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.capacity_left = __capacity
        self.items = []

    def add_item(self, item: str):
        if self.capacity_left > 0:
            self.items.append(item)
            self.capacity_left -= 1
        else:
            return "not enough room in the inventory"
        # self.items.append(item) if self.__capacity > len(self.items) else return "not"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        items = ', '.join(self.items)
        return f"Items: {items}.\nCapacity left: {self.capacity_left}"


"""test case"""
# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)
