from .inventory_iterator import InventoryIterator
from collections.abc import Iterable
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from ..importer.importer import Importer


class InventoryRefactor(Iterable):
    def __init__(self, importer: Importer):
        self.importer = importer
        self.data = []
        self.type = ''

    def import_data(self, path, file_type):
        self.data.extend(self.importer.import_data(path))
        self.type = file_type

    def check_type(self):
        if self.type == 'simples':
            return SimpleReport.generate(self.data)
        return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
