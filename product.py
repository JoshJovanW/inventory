class Product:
    def __init__(self, name, code, quantity):
        self.name = name
        self.code = code
        self.quantity = quantity

    def __str__(self):
        return f"product : {self.name}, stock : {self.quantity} "

    def add_quantity(self, quantity):
        self.quantity += quantity

    def remove_quantity(self, quantity):
            if quantity > self.quantity:
                print("The number you inputed exceeds the amount of products under that code.Try again")
                return False
            else:
                self.quantity -= quantity
                return True


