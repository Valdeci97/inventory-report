from csv import DictReader
from json import load, dumps, loads
from xmltodict import parse
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def import_data(path: str, file_type: str):
        if 'csv' in path:
            with open(path, encoding='utf-8') as csv_file:
                csv_report = DictReader(csv_file)
                csv_list = list(csv_report)
            return Inventory.generate_csv_report(file_type, csv_list)
        if 'json' in path:
            with open(path) as json_file:
                json_report = load(json_file)
            return Inventory.generate_json_report(file_type, json_report)
        if 'xml' in path:
            with open(path, 'r') as xml_file:
                parsed = parse(xml_file.read())
                json_parsed = dumps(parsed)
                xml_report = loads(json_parsed)['dataset']['record']
            return Inventory.generate_xml_report(file_type, xml_report)

    @staticmethod
    def generate_csv_report(file_type: str, csv_file: list):
        if file_type == 'simples':
            return SimpleReport.generate(csv_file)
        elif file_type == 'completo':
            return CompleteReport.generate(csv_file)
        else:
            raise ValueError

    @staticmethod
    def generate_json_report(file_type: str, json_file: list):
        if file_type == 'simples':
            return SimpleReport.generate(json_file)
        elif file_type == 'completo':
            return CompleteReport.generate(json_file)
        else:
            raise ValueError

    @staticmethod
    def generate_xml_report(file_type: str, xml_file: list):
        if file_type == 'simples':
            return SimpleReport.generate(xml_file)
        elif file_type == 'completo':
            return CompleteReport.generate(xml_file)
        else:
            raise ValueError

# Entendendo Python slicing:
# https://stackoverflow.com/questions/509211/understanding-slicing


Inventory.import_data('inventory_report/data/inventory.csv', 'simples')
