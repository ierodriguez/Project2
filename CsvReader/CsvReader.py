import csv
from pathlib import Path


def classfactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []
        relative = Path(filepath)
        absolute = relative.absolute()
        with open(absolute) as text_data:
            csv_data = csv.DictReader(text_data)
            for row in csv_data:
                self.data.append(row)
        pass

    def clear_data(self):
        self.data.clear()

    @staticmethod
    def int_con(r):
        for key in r:
            r[key] = r[key]
        return r

    def return_data_as_objects(self):
        objects = []
        for row in self.data:
            objects.append(self.int_con(row))
        return objects
