rom menu import Menu

from partition import Partition

from product import Product

from warehouse import Warehouse

from abbreviations import abrev

Menu()

tesco = Warehouse()

finish_process = False

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
                product_code = int(input())

                if partition.products != {}:
                    for key in partition.products:
                        if product_code == partition.products[key].code:
                            print("This product exists.")
                            print("How much quantity do you want to add?")
                            product_quantity = int(input())

                            partition.products[key].add_quantity(
                                product_quantity)
                            print("The quantity of the product have been added")
                            break

                else:
                    print("The product under that code doesn't exist. create a new one.")

                    print("what is the name of the product? ")
                    new_product_name = input()

                    print("what is the code of the product? ")
                    new_product_code = int(input())

                    print("what is the quantity of the product? ")
                    new_product_quantity = int(input())

                    new_product = Product(new_product_name, new_product_code, new_product_quantity)

                    partition.add_products(new_product)
                    print("THe product has been added.")
                    break

            else:
                print("This is not a valid partition.")
                break

    elif action == "WD":
        print("In which partition do you want to withdraw the product? (look at below to see existing partitions)\n")

        print("existing partitions: \n")
        print("Floor" + "     " + "Name\n")

        for partition in tesco.partitions:
            print(partition.floor, "     ", partition.name)

        partition_name = input()

        print("Which floor is the partition in?")
        partition_floor = int(input())

        for partition in tesco.partitions:
            if partition_name == partition.name and partition_floor == partition.floor:
                print("what is the code of the product?")
                product_code = int(input())

                if partition.products != {}:
                    for key in partition.products:
                        if product_code == partition.products[key].code:
                            print("do you want to remove a specific quantity or all of it?\n")
                            print("Type 'specific' for the first option and 'all' for the latter")
                            withdraw_option = input()

                            if withdraw_option == "specific":
                                print("How much quantity do you want to remove?")
                                quantity_to_remove = int(input())

                                partition.products[key].remove_quantity(
                                    quantity_to_remove)
                                print("The quantity of the product has been removed")
                                break

                            elif withdraw_option == "all":
                                partition.withdraw_products(product_code)
                                print("Your product has been withdrawed.")
                                break

                            else:
                                print("The option is not available please try again. ")
                                break

                        else:
                            print("The product does'nt exist please try another one.")
                            break

                else:
                    print("There are no products in this partition with that code please try another one.")
                    break

            else:
                continue
                print("That is not a valid partition")
                break

    elif action == "CQ":
        total_quantity_of_item = 0

        print("what is the code of the product?")
        product_code = int(input())

        for partition in tesco.partitions:
            for key in partition.products:
                if product_code == partition.products[key].code:
                    total_quantity_of_item += partition.products[key].quantity

        print("The total quantity of the item under that code is" + total_quantity_of_item)
        print("note if the quantity is 0 then it could be the product under that code does'nt exist")


    elif action == "CI":
        print("In which partition do you want to add the product? (look at below to see existing partitions)\n")

        print("existing partitions: \n")
        print("Floor" + "     " + "Name\n")

        for partition in tesco.partitions:
            print(partition.floor, "     ", partition.name)

        partition_name = input()

        print("Which floor is the partition in?")
        partition_floor = int(input())

        for partition in tesco.partitions:
            if partition_name == partition.name and partition_floor == partition.floor:
                if partition.products != {}:
                    for key in partition.products:
                        print(partition.products[key].name)
                        break
                else:
                    print("there are no products in this partition.")
                    break
            else:
                print("this is not a valid partition.")

    elif action == "LOG":
        pass

    elif action == "END":
        print("Thank you for using this programme")
        finish_process = True

    else:
        print("This action is not available. Pls try again.")
        finish_process = True
