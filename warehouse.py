class Warehouse:
    def __init__(self):
        self.partitions = []

    def __str__(self):
        return f"{self.partitions}"

    def add_partition(self, partitions):
        self.partitions.append(partitions)

