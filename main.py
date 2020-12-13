from menu import Menu

from partition import Partition

from product import Product

from warehouse import Warehouse

from abbreviations import abrev

Menu()

tesco = Warehouse()

finish_process = False

object_1 = Product("object1", 123, 10)

object_2 = Product("object2", 124, 7)




while finish_process == False:
    print("what do you want to do? Write the abbreviations for the action (look at the table below)\n")

    abrev()

    action = input()

    if action == "SP":
        print("What do you want to call it? ")
        partition_name = input()

        print("which floor do you want it to be on? (write the number)")
        partition_floor = int(input())

        storage_partition = Partition(partition_name, partition_floor)
        tesco.add_partition(storage_partition)

        print("The partition has been created.")
        print("here are the existing partitions inside the warehouse: \n")

        print("Floor" + "     " + "Name\n")

        for partition in tesco.partitions:
            print(partition.floor, "     ", partition.name)

        storage_partition.add_products(object_1)
        storage_partition.add_products(object_2)

    elif action == "ADD":
        print("In which partition do you want to add the product? (look at below to see existing partitions)\n")

        print("existing partitions: \n")
        print("Floor" + "     " + "Name\n")

        for partition in tesco.partitions:
            print(partition.floor, "     ", partition.name)

        partition_name = input()

        print("Which floor is the partition in? \n")
        partition_floor = int(input())

        for partition in tesco.partitions:
            if partition_name == partition.name and partition_floor == partition.floor:
                print("what is the code of the product? (it will check if the product already exist)")
                product_code = input()

                for key in partition.products:
                    if product_code == partition.products[key].code:
                        print("This product exists.")
                        print("How much quantity do you want to add?")
                        product_quantity = int(input())

                        partition.products[key].add_quantity(product_quantity)
                        print("The quantity of the product have been added")
                        break

                    else:
                        print("what is the name of the product? ")
                        new_product_name = input()

                        print("what is the code of the product? ")
                        new_product_code = input()

                        print("what is the quantity of the product? ")
                        new_product_quantity = int(input())

                        new_product = Product(
                            new_product_name, new_product_code, new_product_quantity)

                        partition.add_products(new_product)
                        print("THe product has been added.")
                        break

            else:
                print("This is not a valid partition.")
                break

    elif action == "WD":
        pass

    elif action == "CQ":
        pass

    elif action == "CI":
        pass

    elif action == "LOG":
        pass

    elif action == "END":
        print("Thank you for using this programme")
        finish_process = True

    else:
        print("This action is not available. Pls try again.")
        finish_process = True

