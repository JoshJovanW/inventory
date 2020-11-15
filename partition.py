class Partition:
    def __init__(self, floor, room):
        self.floor = floor
        self.room = room
        self.product = []

    def get_floor(self):
        return f"floor number {self.floor}"

    def get_room(self):
        return f"room number {self.room}"

    def get_products(self):
        return f"the contents inside the room are {self.product}"

    def add_products(self, product):
        self.product.append(product)

    def withdraw_products(self, product):
        self.product.remove(product)

