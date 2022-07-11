from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, data: list):
        fabrication_date = [row['data_de_fabricacao'] for row in data]
        dead_line_date = [row['data_de_validade'] for row in data]
        companies = [row['nome_da_empresa'] for row in data]
        most_common_company = Counter(companies).most_common()[0][0]
        return (
          f'Data de fabricação mais antiga: {min(fabrication_date)}\n'
          f'Data de validade mais próxima: {min(dead_line_date)}\n'
          f'Empresa com mais produtos: {most_common_company}'
        )
