from datetime import datetime

class Log:
    def __init__(self):
        self.records = []

    def __str__(self):
        return f"{self.records}"

    def add_record(self, description):
        time = datetime.now()
        date_and_time = time.strftime("%d/%m/%Y %H:%M:%S")
        statement = ("[" + date_and_time + "]" + "  " + description)
        self.records.append(statement)

