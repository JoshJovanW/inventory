class Product:
    def __init__(self, name, code, quantity):
        self.name = name
        self.code = code
        self.quantity = quantity

    def __str__(self):
        return f"product : {self.name}, stock : {self.quantity} "

    def add_quantity(self, quantity):
        self.quantity += quantity

    def add_name(self, name):
        self.name = name
        
    def add_code(self, code):
        self.code = code




