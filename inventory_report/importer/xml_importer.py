from xmltodict import parse
from json import dumps, loads
from .importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        if 'xml' not in path:
            raise ValueError('Arquivo inválido')
        with open(path, 'r') as file:
            parsed_xml = parse(file.read())
            json_parsed = dumps(parsed_xml)
            xml_list = loads(json_parsed)['dataset']['record']
        return xml_list
