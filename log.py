class Log:
    def __init__(self):
        self.record = []

    def __str__(self):
        return self.record

    def add_record(self, record):
        self.record.append(record)
