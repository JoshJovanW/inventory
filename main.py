from partition import Partition

from product import Product

NikeShoe = Product("nike shoe", "#123", 5)

AdidasShoe = Product("adidas shoe", "#124", 3)

ReebokShoe = Product("reebok shoe", "#125", 2)

warehouse = Partition(5, 20)

warehouse.add_products(NikeShoe)
warehouse.add_products(AdidasShoe)
warehouse.add_products(ReebokShoe)

warehouse.withdraw_products(ReebokShoe)

for i in warehouse.product:
    print(i)

