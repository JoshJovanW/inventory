class Warehouse:
    def __init__(self):
        self.partitions = []

    def __str__(self):
        return f"{self.partitions}"

    def add_partition(self, partitions):
        self.partitions.append(partitions)

    def find_partition(self):
        print("Please chose a partition to do the action. (look at below to see existing partitions)\n")

        print("existing partitions: \n")
        print("Floor" + "     " + "Name\n")

        for partition in self.partitions:
            print(partition.floor, "     ", partition.name)

        print("Write the partition name.")
        partition_name = input()

        print("Which floor is the partition in?")
        partition_floor = int(input())

        index_of_partition = -1

        for partition in self.partitions:
            if partition.floor == partition_floor and partition.name == partition_name:
                index_of_partition = self.partitions.index(partition)

        return index_of_partition
            
            
