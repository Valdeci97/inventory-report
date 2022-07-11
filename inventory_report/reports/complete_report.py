from collections import Counter
from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, data: list):
        fabrication_date = [row['data_de_fabricacao'] for row in data]
        dead_line_date = [row['data_de_validade'] for row in data]
        companies = [row['nome_da_empresa'] for row in data]
        companies_products = Counter(companies).most_common()
        most_common_company = Counter(companies).most_common()[0][0]
        return (
          f'Data de fabricação mais antiga: {min(fabrication_date)}\n'
          f'Data de validade mais próxima: {min(dead_line_date)}\n'
          f'Empresa com mais produtos: {most_common_company}\n'
          f'{self.product_reporter_formatter(self, companies_products)}'
        )

    def product_reporter_formatter(self, products: list):
        report = 'Produtos estocados por empresa:\n'
        for product in products:
            report += f'- {product[0]}: {product[1]}\n'
        return report
