class Partition:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor
        self.products = {}

    def __str__(self):
        return f"name : {self.name}, floor : {self.floor}"

    def get_products(self):
        return f"the contents inside the room are {self.product}"

    def add_product(self, product):
        self.products[product.code] = product

    def withdraw_product(self, code):
        self.products.pop(code)

    
    
