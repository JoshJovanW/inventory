class Log:
    def __init__(self):
        self.records = []

    def __str__(self):
        return f"{self.records}"

    def add_record(self, record):
        self.records.append(record)
