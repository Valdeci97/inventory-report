from .importer.json_importer import JsonImporter
from .importer.csv_importer import CsvImporter
from .importer.xml_importer import XmlImporter
from .inventory.inventory_refactor import InventoryRefactor
import sys


def main():
    if len(sys.argv) <= 2:
        return sys.stderr.write('Verifique os argumentos\n')
    file_path, file_type = sys.argv[1], sys.argv[2]

    if 'csv' in file_path:
        inventory = InventoryRefactor(CsvImporter)
        inventory.import_data(file_path, file_type)
        return print(inventory.check_type(), end='')
    if 'json' in file_path:
        inventory = InventoryRefactor(JsonImporter)
        inventory.import_data(file_path, file_type)
        return print(inventory.check_type(), end='')
    if 'xml' in file_path:
        inventory = InventoryRefactor(XmlImporter)
        inventory.import_data(file_path, file_type)
        return print(inventory.check_type(), end='')
