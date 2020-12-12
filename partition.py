class Partition:
    def __init__(self, name, floor, room):
        self.name = name
        self.floor = floor
        self.room = room
        self.products = {}

    def __str__(self):
        return f"name : {self.name}, room : {self.room}, floor : {self.floor}"

    def set_name(self, name):
        self.name = name

    def set_floor(self, floor):
        self.floor = floor 

    def set_room(self, room):
        self.room = room


    def get_products(self):
        return f"the contents inside the room are {self.product}"

    def add_products(self, product):
        self.products[product.code] = product

    def withdraw_products(self, code):
        self.product.pop(code)
