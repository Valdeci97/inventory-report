from json import load
from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path: str):
        if 'json' not in path:
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            json_data = load(file)
        return json_data
