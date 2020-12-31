from menu import Menu
from partition import Partition
from product import Product
from warehouse import Warehouse
from abbreviations import abrev
from log import Log

Menu()

tesco = Warehouse()

finish_process = False

log_book = Log()

while finish_process == False:
    print("\n")

    print("what do you want to do? Write the abbreviations for the action (look at the table below)\n")

    abrev()

    action = input()

    print("\n")

    if action == "SP":
        print("What do you want to call it? ")
        partition_name = input()

        print("which floor do you want it to be on? (write the number)")
        partition_floor = int(input())

        storage_partition = Partition(partition_name, partition_floor)
        tesco.add_partition(storage_partition)

        print("The partition " + partition_name + " has been created.")
        
        log_book.add_record("The partition " + partition_name + " has been created.")

        print("here are the existing partitions inside the warehouse: \n")

        print("Floor" + "     " + "Name\n")

        for partition in tesco.partitions:
            print(partition.floor, "     ", partition.name)

        print("\n")

    elif action == "ADD":
        index_of_partition = tesco.find_partition()
    
        if index_of_partition == -1:
            print("This partition does not exist.")
            continue

        print("what is the product code?")
        product_code = str(input())

        product_exist = False
        for product in tesco.partitions[index_of_partition].products:
            if product == product_code:
                product_exist = True
                
        if product_exist == False:
            print("The product under this code doesn't exist.")

            print("what is the product name?")
            product_name = input()

            print("what is the product quantity?")
            product_quantity = int(input())

            new_product = Product(product_name, product_code, product_quantity)

            tesco.partitions[index_of_partition].add_product(new_product)

            print("The product has been added to the partition.")

            log_book.add_record("The product " + product_code + " " + "has been added to the partition" + " " + tesco.partitions[index_of_partition].name)
            continue

        print("This product exists.")
        print("How much quantity do you want to add?")
        product_quantity = int(input())

        product.add_quantity(product_quantity)
        print("The quantity of the product has been added.")

        log_book.add_record("The product " + product_code+ "quantity has been added to the partition" + tesco.partitions[index_of_partition].name)


    elif action == "WD":
        index_of_partition = tesco.find_partition()

        if index_of_partition == -1:
            print("This partition does not exists.")
            continue

        print("what is the product code?")
        product_code = str(input())

        product_exist = False
        product_key = None
        for product in tesco.partitions[index_of_partition].products:
            if product == product_code:
                product_exist = True
                product_key = product_code
                print(f"There are {tesco.partitions[index_of_partition].products[product].quantity} of the product inside this partition.")


        if product_exist == False:
            print("The product under that code does not exist.")
            continue

        print("Do you want to withdraw some or all of it? ")
        print("Type 'specific' or 'all'.\n")

        withdraw_action = input()

        if withdraw_action == "specific":
            print("How much quantity do you want to remove?")
            quantity_to_remove = int(input())

            action_done = tesco.partitions[index_of_partition].products[product_key].remove_quantity(quantity_to_remove)
            
            if action_done == True:
                print("The quantity of the product " + product_code + " has been removed from" + " " + tesco.partitions[index_of_partition].name)

                log_book.add_record("The quantity of the product " + product_code + " has been removed from" + " " + tesco.partitions[index_of_partition].name)
                continue

        elif withdraw_action == "all":
            tesco.partitions[index_of_partition].withdraw_product(product_code)
            print("The product " + product_code + " has been withdrawed from " + tesco.partitions[index_of_partition].name)

            log_book.add_record("The product " + product_code + " has been withdrawed from " + tesco.partitions[index_of_partition].name)
            continue

        else:
            print("This option is not available.")
            continue
       
    elif action == "CQ":
        total_quantity_of_item = 0

        print("what is the code of the product? .")
        product_code = str(input())
        
        product_exist = False
        product_key = None
        for partition in tesco.partitions:
            for product in partition.products:
                if product == product_code:
                    product_exist = True
                    product_key = product_code
                    total_quantity_of_item += partition.products[product_code].quantity

        if product_exist == False:
            print("The product under that code doesnt exist.")
            continue

        print("\n")
        print ("The total quantity of the item " + product_code + " under that code is ", total_quantity_of_item)

    elif action == "CI":
        index_of_partition = tesco.find_partition()
    
        if index_of_partition == -1:
            print("This partition does not exist.")
            continue

        for product in tesco.partitions[index_of_partition].products:
            print(tesco.partitions[index_of_partition].products[product].name, "quantity:", tesco.partitions[index_of_partition].products[product].quantity)
            

    elif action == "CP":
        print("here are the existing partitions inside the warehouse: \n")

        print("Floor" + "     " + "Name\n")

        for partition in tesco.partitions:
            print(partition.floor, "     ", partition.name)

        print("\n")

    elif action == "LOG":
        for record in log_book.records:
            print(record)

        print("\n")

    elif action == "END":
        print("Thank you for using this programme")
        finish_process = True

    else:
        print("This action is not available. Pls try again.")
        finish_process = True
