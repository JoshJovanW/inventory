from menu import Menu
from partition import Partition
from product import Product
from warehouse import Warehouse
from abbreviations import abrev
from datetime import datetime
from log import Log
Menu()

tesco = Warehouse()

finish_process = False

time = datetime.now()

date_and_time = time.strftime("%d/%m/%Y %H:%M:%S")

log_book = Log()



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

        statement = print("The partition " + partition_name + " has been created at " + date_and_time)
        print(statement)
        log_book.add_record(statement)

        print("here are the existing partitions inside the warehouse: \n")

        print("Floor" + "     " + "Name\n")

        for partition in tesco.partitions:
            print(partition.floor, "     ", partition.name)

    elif action == "ADD":
        tesco.find_partition()

        partition_existence = False
        partition_not_empty = False
        code_exist = False

        for partition in tesco.partitions:
            if partition_name == partition.name and partition_floor == partition.floor:
                partition_existence = True
                print("what is the code of the product?")
                product_code = int(input())

                if partition.products != {}:
                    partition_not_empty = True
                    for key in partition.products:
                        if product_code == partition.products[key].code:
                            code_exist = True
                            print("This product exists.")
                            print("How much quantity do you want to add?")
                            product_quantity = int(input())

                            partition.products[key].add_quantity(product_quantity)
                            statement = print("The quantity of the product have been added to " + partition.name + " at " + date_and_time)
                            print(statement)
                            log_book.add_record(statement)
                            break


        if partition_existence == False:
            print("ERROR! There are no partitions named " , partition_name, " on floor ", partition_floor)
            continue

        if partition_not_empty == False:
            print("ERROR! There are no products in this partition. Please create a product.\n")
            print("what is the name of the product? ")
            new_product_name = input()

            print("what is the code of the product? ")
            new_product_code = int(input())
            code_exist = True

            print("what is the quantity of the product? ")
            new_product_quantity = int(input())

            new_product = Product(new_product_name, new_product_code, new_product_quantity)
             
            for partition in tesco.partitions:
                if partition_name == partition.name and partition_floor == partition.floor:
                    partition.add_products(new_product)
                    statement = print("The product has been added to the partition " + partition.name + " at " + date_and_time)
                    print(statement)
                    log_book.add_record(statement)
                    continue

        if code_exist == False:
            print("ERROR! There are no products under that code. please create a new one.")
            print("what is the name of the product? ")
            new_product_name = input()

            print("what is the code of the product? ")
            new_product_code = int(input())
            code_exist = True

            print("what is the quantity of the product? ")
            new_product_quantity = int(input())

            new_product = Product(new_product_name, new_product_code, new_product_quantity)

            for partition in tesco.partitions:
                if partition_name == partition.name and partition_floor == partition.floor:
                    partition.add_products(new_product)
                    statement = print("The product has been added to the partition " + partition.name + " at " + date_and_time)
                    print(statement)
                    log_book.add_record(statement)
                    continue


    elif action == "WD":
        tesco.find_partition()

        partition_existence = False
        partition_not_empty = False
        code_exist = False

        for partition in tesco.partitions:
            if partition_name == partition.name and partition_floor == partition.floor:
                partition_existence = True
                print("what is the code of the product?")
                product_code = int(input())

                if partition.products != {}:
                    partition_not_empty = True
                    for key in partition.products:
                        if product_code == partition.products[key].code:
                            code_exist = True
                            print("do you want to remove a specific quantity or all of it?\n")
                            print("Type 'specific' for the first option and 'all' for the latter")
                            withdraw_option = input()

                            if withdraw_option == "specific":
                                print("How much quantity do you want to remove?")
                                quantity_to_remove = int(input())

                                partition.products[key].remove_quantity(quantity_to_remove)
                                statement = print("The quantity of the product has been removed at " + date_and_time)
                                log_book.add_record(statement)
                                break

                            elif withdraw_option == "all":
                                partition.withdraw_products(product_code)
                                statement = print("Your product has been withdrawed at " + date_and_time)
                                print(statement)
                                log_book.add_record(statement)
                                break

                            else:
                                print("The option is not available please try again. ")
                                break
        

        if partition_existence == False:
            print("ERROR! There are no partitions named" , partition_name, "on floor", partition_floor)
            continue

        if partition_not_empty == False:
            print("ERROR! There are no products in this partition. Please create a product or choose another one.\n")
            code_exist = True
            continue

        if code_exist == False:
            print("ERROR! There are no products under that code. please choose another one.")
            continue

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
        tesco.find_partition()

        partition_existence = False
        partition_not_empty = False

        for partition in tesco.partitions:
            if partition_name == partition.name and partition_floor == partition.floor:
                partition_existence = True
                if partition.products != {}:
                    partition_not_empty = True
                    for key in partition.products:
                        print(partition.products[key].name)
                        break
        
        if partition_existence == False:
            print("ERROR! There are no partitions named" , partition_name, "on floor", partition_floor)
            continue

        if partition_not_empty == False:
            print("ERROR! There are no products in this partition. Please create a product or choose another one.\n")
            continue

               

    elif action == "LOG":
        pass

    elif action == "END":
        print("Thank you for using this programme")
        finish_process = True

    else:
        print("This action is not available. Pls try again.")
        finish_process = True
