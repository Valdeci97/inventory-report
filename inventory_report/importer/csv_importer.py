from csv import DictReader
from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if 'csv' not in path:
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            csv_data = DictReader(file)
            csv_list = list(csv_data)
        return csv_list
